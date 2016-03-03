from django.conf.urls import url
from .views import question

urlpatterns = [
    url(r'^frage/(?P<question_id>[0-9]+)$', question, name='question'),
]
