from django.conf.urls import url

from users.views import UserCreateView, UserLoginView, UserLogoutView

urlpatterns = [
    url(r'^api/user/create', UserCreateView.as_view()),
    url(r'^api/user/login', UserLoginView.as_view()),
    url(r'^api/user/logout', UserLogoutView.as_view()),
]