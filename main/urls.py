from django.urls import path
from main import views

urlpatterns = [
    path('', views.ScheduleListView.as_view(), name="home"),
    path('api/', views.api_root),
    path('schedules/', views.ScheduleList.as_view(), name='schedule-list'),
    path('schedules/<int:pk>/', views.ScheduleDetail.as_view(),
         name='schedule-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
]
