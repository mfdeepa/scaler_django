from django.http import HttpResponse, HttpRequest
import json

from django.shortcuts import get_object_or_404

from .models import User

def users(request : HttpRequest) -> HttpResponse:

    if request.method == 'GET':
        users = User.objects.all()
        serialized_users = [User.name for user in users]
        return HttpResponse(json.dumps(serialized_users))
    if request.method == 'POST':
        body = json.loads(request.body)   # converting string into list
        user = User(name=body['name'], email=body['email'],age=body['age'])
        user.save()
        return HttpResponse(json.dumps({'id':user.id,'name':user.name}))

def get_or_update_or_delete_user(request: HttpRequest, id:int) -> HttpResponse:
    if request.method == 'GET':
        user = get_object_or_404(User, id = id)
        #user = User.objects.get(id=id)
        return HttpResponse(json.dumps({'id':user.id,'name':user.name, 'email': user.email, 'age':user.age}))

    if request.method == 'PUT':
        body = json.loads(request.body)   # converting string into list
        user = get_object_or_404(User, id=id)
#        user = User.objects.get(id)
        user.name = body['name']
        user.email = body['email']
        user.age = body['age']
        user.save()
        return HttpResponse(json.dumps({'id':user.id,'name':user.name}))

    if request.method == 'DELETE':
        #User.objects.all()
        user = get_object_or_404(User, id = id)
        user.delete()
        return HttpResponse(json.dumps({'id': id, 'deleted': True}))


