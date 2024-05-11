from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/<slug>/', views.post, name = 'post'),
    path('about/', views.about ,name = 'about' ),
    path('category/<slug>/', views.category_Post, name = 'category'), # all posts of category
    path('search/', views.search, name = 'search'),
]


from django.conf.urls import handler404, handler500

handler404 = views.custom_404
handler500 = views.custom_500