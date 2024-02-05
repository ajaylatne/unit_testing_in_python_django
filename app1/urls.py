from django.urls import path
from .views import demo_view, demo_view1, demo_view2

urlpatterns = [
    path('demo_view/', demo_view, name="demo_url"),
    path('demo_view1/', demo_view1, name="demo_url1"),
    path('demo_view2/', demo_view2, name="demo_url2"),
]
