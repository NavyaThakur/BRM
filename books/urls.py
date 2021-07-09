from django.urls import path
from books import views
urlpatterns = [
    path('insert/',views.insertBook),
    path('save/',views.insert),
    path('view/',views.viewBooks),
    path('edit/',views.editBooks),
    path('update/',views.edit),
    path('delete/',views.deleteBooks),
    path('search/',views.searchBooks),
    path('searching/',views.search),
    path('login/',views.UserLogin),
    path('logout/',views.UserLogout),
    
]
