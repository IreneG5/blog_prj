from django.conf.urls import url
import views

urlpatterns = [
    url(r'^blog/$', views.post_list),
    url(r'^blog/popular/$', views.popular_post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail, name="views-post-detail"),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', views.edit_post),

]
