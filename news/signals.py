
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from django.template.loader import render_to_string

from NewsPortal.settings import EMAIL_FROM_COMPLETE
from news.models import Post, SubscribersCategory


@receiver(m2m_changed, sender = Post.categories.through)
def notify_subscribers_category(sender, instance, **kwargs):
	post_obj = instance
	categories_objs = post_obj.categories.all()
	for category in categories_objs:
		sub_cat_rows = SubscribersCategory.objects.filter(
			category = category.id).select_related()
		print(sub_cat_rows, 'subscribers')
		for row in sub_cat_rows:

			subscriber_username_to_send = row.subscriber.username
			subscriber_email_to_send = row.subscriber.email
			if subscriber_username_to_send:
				html_content = render_to_string(
					'emails_template/notification_new_news_category.html',
					{
						'username': row.subscriber.username,
						'category': category,
						'news': instance,
					}
				)
				msg = EmailMultiAlternatives(
					subject = f'Новая статья в твоём любимом разделе {category.category_name}',
					body = instance.text[:50],
					from_email = EMAIL_FROM_COMPLETE,
					to = [subscriber_email_to_send],
				)
				msg.attach_alternative(html_content,
									   "text/html")

				msg.send()


