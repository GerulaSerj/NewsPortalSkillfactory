from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Subscription, Category
from datetime import datetime, timedelta
from django.template.loader import render_to_string



@receiver(post_save, sender=Post)
def product_created(instance, created, **kwargs):
    if not created:
        return

    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject = f'Новая новость в категории {instance.category}'

    text_content = (
        f'Заголовок: {instance.name}\n'
        f'Ссылка на новость: http://127.0.0.1{instance.get_absolute_url()}'
    )
    html_content = (
        f'Заголовок: {instance.name}<br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на новость</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

@receiver(post_save, sender=Post)
def notify_subscribers(sender, instance, created, **kwargs):
    if created and instance.__class__.__name__ == 'Post':
        product_created.apply_async(
            (instance.id, instance.title, instance.text),
            countdown=10,
        )


@shared_task
def weekly_news():
    today = datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.object.filter(dateCreation__gte=last_week)
    categories = set(posts.values_list('category__name', flat = True))
    subscribers = set(Category.objects.filter(name__In=categories).values_list('subscriptions', flat = True))

    html_content = render_to_string(
        'daily-post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Weekly news',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )


    msg.attach_alternative(html_content, "text/html")
    msg.send()