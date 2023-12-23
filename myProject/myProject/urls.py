
from django.contrib import admin
from django.urls import path
from myProject.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signupPage,name='signupPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('signinPage/',signinPage,name='signinPage'),
    path('dashboardPage/',dashboardPage,name='dashboardPage'),
    path('viewBlog/',viewBlog,name='viewBlog'),
    path('addblog/',addblog,name='addblog'),
    path('deleteBlog/<str:myid>',deleteBlog,name='deleteBlog'),
    path('editBlog/<str:myid>',editBlog,name='editBlog'),
    path('updateBlog/',updateBlog,name='updateBlog'),
    path('createBlog/<str:myid>',createBlog,name='createBlog'),
    path('ProfilePage/',ProfilePage,name='ProfilePage'),
    path('EditProfilePage/',EditProfilePage,name='EditProfilePage'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
