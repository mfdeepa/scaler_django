from django.http import HttpResponse, HttpRequest


def say_hello(request):
    return HttpResponse('Hello Deepa!')

def say_hello_with_name(request:HttpRequest,name):
    print(request.headers)
    return HttpResponse(f'Hello World ! :  {name}')