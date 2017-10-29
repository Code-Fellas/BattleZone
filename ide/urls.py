from django.conf.urls import url

from ide.views import FetchLanguagesView, SubmissionView

urlpatterns = [
    url(r'^api/ide/$', FetchLanguagesView.as_view()),
    url(r'^api/ide/submit', SubmissionView.as_view())
]