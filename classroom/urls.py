"""classroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from classroomapi import views

from classroomapi.endpoint_views import OrganisationView
from classroomapi.endpoint_views import CourseView
from classroomapi.endpoint_views import ResourceView, SingleResourceView
from classroomapi.endpoint_views import SubtitleView
from classroomapi.endpoint_views import HighlightView
from classroomapi.endpoint_views import EventView
from classroomapi.endpoint_views import LinkView
from classroomapi.endpoint_views import ClipView
from classroomapi.endpoint_views import AWSTranscribeView
from classroomapi.endpoint_views import CreatePDFHighlightView

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('organisation/', OrganisationView.as_view()),
    path('organisation/<slug:organisation_id>/', OrganisationView.as_view()),

    path('course/', CourseView.as_view()),
    path('course/<slug:course_id>/', CourseView.as_view()),

    path('resource/<slug:course_id>/', ResourceView.as_view()),
    path('resource/<slug:course_id>/<slug:resource_id>', SingleResourceView.as_view()),

    path('subtitle/<slug:course_id>/<slug:resource_id>/', SubtitleView.as_view()),

    path('highlight/<slug:highlight_id>/', HighlightView.as_view()),

    path('event/<slug:course_id>/', EventView.as_view()),
    path('event/<slug:course_id>/<slug:event_id>', EventView.as_view()),

    path('link/<slug:course_id>/', LinkView.as_view()),

    path('clip/<slug:course_id>/', ClipView.as_view()),

    path('create/resource/pdf_highlight', CreatePDFHighlightView.as_view()),

    path('aws/transcribe_state_change', AWSTranscribeView.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
