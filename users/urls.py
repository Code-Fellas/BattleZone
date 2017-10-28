from django.conf.urls import url

from users.views import UserCreateView

urlpatterns = [
    url(r'^api/user/create', UserCreateView.as_view())
]