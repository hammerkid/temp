from django.conf.urls import url
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from guest_book import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_post$', views.add_post, name='add_post'),
    url(r'^check_form', views.check_form, name='check_form'),
    url(r'^thanks', RedirectView.as_view(url='/')),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)