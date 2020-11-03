from django.shortcuts import render, redirect
from .models import CounterModel

def helloworld(request):
	name = 'John Doe'
	obj = CounterModel.objects.filter(id = 1).first()
	ournumber = obj.number
	context = {'name': name, 'number': ournumber}
	return render(request, 'helloworld/hello.html', context)

def hellostudent(request):
	return render(request, 'helloworld/student.html')

def increment(request):
	obj = CounterModel.objects.filter(id = 1).first()
	obj.number = int(obj.number) + 1
	obj.save()
	return redirect(request.META['HTTP_REFERER'])

def reset(request):
	obj = CounterModel.objects.filter(id = 1).first()
	obj.number = 0
	obj.save()
	return redirect(request.META['HTTP_REFERER'])

def decrement(request):
	obj = CounterModel.objects.filter(id = 1).first()
	obj.number = int(obj.number) - 1
	obj.save()
	return redirect(request.META['HTTP_REFERER'])