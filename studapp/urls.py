from django.urls import path
from .import views

urlpatterns=[
    #path('index/',views.index,name='index'),
    path('enroll/', views.enroll_student, name='enroll_student'),
    path('students/', views.show_students, name='show_students'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('edit_student/<int:id>/', views.edit_student, name='edit_student'),
    path('login/',views.login,name='login'),
 #   path('delete',views.delete,name='delete'),
    path('logout/', views.logout, name='logout'),
    path('register',views.register,name='register')
]