from django.conf.urls import url
from users_app import views

urlpatterns=[
    url(r'^$',views.sign_up_view, name='signup'),
    url(r'^users/', views.users, name="users"),

]
