from django.urls import path

# for method 1
from app_name.views import MyCustomViewClass

# for method 2
from app_name.views import custom_function_view, custom_function_view2

urlpatterns = [
    # for method 1
    path('app_url1/',MyCustomViewClass.as_view(),name = 'Custom View'),
    
    # for method 2
    path('app_url2/',custom_function_view,name = 'Function View'),
    
    path('app_url3/',custom_function_view2,name = 'Function View 2'),
]


