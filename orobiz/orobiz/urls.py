from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orobiz/admin_panel/', include('admin_panel.urls')),
    path('orobiz/authentication/', include('authentication.urls')),
    path('orobiz/member_portal/', include('member_portal.urls')),
    path('orobiz/referral_system/', include('referral_system.urls')),
]

# Serve media files in development
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
