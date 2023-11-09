import logging
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .celery import app
from django.template import Template, Context

REPORT_TEMPLATE = """
here's how you did till now:

    {% for post in posts %}
    "{{ post.title }}" viewed {{ post.view_count }}times |

    {% endfor %}    
"""


@app.task
def send_view_count_report():
    from media.models import Post
    for user in get_user_model().objects.all():
        posts = Post.objects.filter(author=user)
        if not posts:
            continue

        template = Template(REPORT_TEMPLATE)

        send_mail(
            ' hello ',
            template.render(context=Context({'posts': posts})),
            'testtestdjango@yandex.ru',
            [user.email],
            fail_silently=False
        )


@app.task
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            'пожалуйста верифицируйте свой аккаунт',
            'чтобы верифицировать свой аккаунт: '
            'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
            'testtestdjango@yandex.ru',
            [user.email],
            fail_silently=False
        )
    except UserModel.DoesNotExist:
        logging.warning("была попытка верифицировать пользователя %s" % user_id)
