from django.conf.urls import url

from contest.views import FetchContestsView, FetchProblemsView, CreateContestView

urlpatterns = [
    url(r'^api/contests/$', FetchContestsView.as_view()),
    url(r'^api/contests/problems', FetchProblemsView.as_view()),
    url(r'^api/contests/new', CreateContestView.as_view())
]