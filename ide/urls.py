from django.conf.urls import url
from ide.views import FetchLanguagesView


urlpatterns = [
    url(r'^api/ide', FetchLanguagesView.as_view())
]