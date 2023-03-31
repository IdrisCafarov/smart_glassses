from django.urls import path
from account.views import *


urlpatterns = [
    path('',index_view, name="index"),
    path('dashboard_user',dashboard_user_view, name="dashboard_user"),
    path('dashboard_admin', dashboard_admin_view, name="dashboard_admin"),
    path('logout/',logout_view, name="logout"),
    path('edit_user/', update_view, name="edit"),
    path('admin_help/',admin_help_view,name="admin_help"),
    path('done/<id>/',make_done_call,name="done"),
    path('user_detail/<slug>',user_details,name="user_detail"),
    path('create_call',CreateCallView.as_view({'post':'create'}),name="create_call")
]
