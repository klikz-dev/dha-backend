from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from membersuite.views import MembershipViewSet
from misc.views import AnnouncementViewSet
from qualtrics.views import AnalysisViewSet, ReportViewSet, SurveyViewSet

from . import views

router = routers.DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'analytics', AnalysisViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'memberships', MembershipViewSet)
router.register(r'announcements', AnnouncementViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
