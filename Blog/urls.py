from django.urls import path
from . views import  BlogView, BlogDetail
from . models import Blog

urlpatterns= [
    path('', BlogView.as_view(), name='blogs'),
    path('<pk>/',BlogDetail.as_view(), name='detail')

]