"""
URL configuration for bookr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin, auth
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import profile
# from bookr_admin.admin import admin_site

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('reviews.urls')),
    path('filter_demo/', include('filter_demo.urls')),
    path('book_management/', include('book_management.urls')),

    path('accounts/profile/', profile, name='profile'),
    path("accounts/", include(("django.contrib.auth.urls", "auth"), namespace="accounts")),
    path("accounts/password_reset/done/", auth.views.PasswordResetDoneView.as_view(), name="password_reset_done",),
    path("accounts/reset/done/",  auth.views.PasswordResetCompleteView.as_view(), name="password_reset_complete",),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)