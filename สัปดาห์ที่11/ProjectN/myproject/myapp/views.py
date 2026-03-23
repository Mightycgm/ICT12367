from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from myapp.models import Person

# Create your views here.
def index(request):
    all_Person = Person.objects.all()
    return render(request,'index.html',{'all_Person':all_Person})

def about(request):
    return render(request, 'about.html')

def form(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        age = request.POST.get('age')
        if fullname and age:
            Person.objects.create(name=fullname, age=int(age))
            return redirect('index')
    return render(request,'form.html')

def edit_person(request, id):
    person = get_object_or_404(Person, id=id)
    if request.method == 'POST':
        person.name = request.POST.get('fullname')
        person.age = int(request.POST.get('age'))
        person.save()
        return redirect('index')
    return render(request, 'edit.html', {'person': person})

def delete_person(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    return redirect('index')