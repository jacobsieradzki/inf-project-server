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
from classroomapi.endpoint_views import OrganisationView, CoursesView, ResourceView, EventView, LinkView

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('organisation/', OrganisationView.as_view()),
    path('organisation/<slug:organisation_id>/', OrganisationView.as_view()),
    path('course/', CoursesView.as_view()),
    path('course/<slug:course_id>/', CoursesView.as_view()),
    path('resource/<slug:course_id>/', ResourceView.as_view()),
    path('resource/<slug:course_id>/<slug:resource_id>', ResourceView.as_view()),
    path('event/<slug:course_id>/', EventView.as_view()),
    path('event/<slug:course_id>/<slug:event_id>', EventView.as_view()),
    path('links', LinkView.as_view()),


    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
