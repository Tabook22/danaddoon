from django.contrib import admin
from django.urls import path, include
#this is important for media files to show properly with problems
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('tutorials/',include('tutorials.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# notice: we added statics(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# to the end of the urlpatterns for media files to show up correctlly
