from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


## reference: https://www.django-rest-framework.org/api-guide/views/
"""
After Running the server using python manage.py runserver 
    url1 and url3 supports get and post both
    open: http://127.0.0.1:8000/project_url/app_url1/
    open: http://127.0.0.1:8000/project_url/app_url2/
    open: http://127.0.0.1:8000/project_url/app_url3/
    To run at any other port :
    python manage.py runserver 8027
"""


## Method 1: Class Based Views
class MyCustomViewClass(APIView):
    def get(self,request):
        return Response({"Message": "This is a get request from Class Based Views"})

    def post(self,request):
        return Response({"Message": "This is a post request from Class Based Views","data": request.data})

## response from post method
"""
{
    "Message": "This is a post request from Class Based Views",
    "data": {
        "Key will display here": "Data here"
    }
} 
"""   
    
## Method 2 : Function Based Views
@api_view()
def custom_function_view(request):
    print(request.method)
    ## default in @api_view is get method
    return Response({"Message": "This is a get request from Function Based Views"})    

@api_view(['GET', 'POST'])
def custom_function_view2(request):
    if request.method == 'POST':
        ## any function call for module call will happen here
        ## POST method also support file uploads 
        return Response({"message": "This is a post request from Function Based Views 2", "data": request.data})
    ## other wise its a get request (as of now, other methods are also there like PUT etc.)
    return Response({"message": "This is a get request from Function Based Views 2"})


## response from POST method
"""
{
    "message": "This is a post request from Function Based Views 2",
    "data": {
        "Key will display here": "Data here"
    }
}
"""
