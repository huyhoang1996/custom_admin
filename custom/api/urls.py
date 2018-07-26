from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^play/book/$', views.play_book),
]
