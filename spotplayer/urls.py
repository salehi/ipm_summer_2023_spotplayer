from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('spotplayer/', include('token_finder.urls')),
]
