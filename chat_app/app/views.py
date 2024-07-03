from django.shortcuts import render, redirect
from .models import Group, Message

def home(request):
    if request.method == 'POST':
        name = request.POST['group_names']
        obj = Group.objects.filter(group=name).first()
        if not obj:
            ob = Group.objects.create(group=name)
            ob.save()
        return redirect(f"chat/{name}/")
    return render(request, 'index.html')

def room(request, group_name):
    group = Group.objects.get(group=group_name)
    chat = Message.objects.filter(group=group)
    return render(request, 'room.html', {'group': group_name, 'chat': chat})
