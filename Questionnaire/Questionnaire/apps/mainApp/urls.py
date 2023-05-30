from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.regist, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('questionnaire_page/<str:name>', views.questionnaire_page, name='questionnaire_page'),
    path('lection_page/<str:lec_id>', views.lection_page, name='lection_page'),
]
