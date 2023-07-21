from django.http import HttpResponse
from django.shortcuts import render
from django import forms

from collections import defaultdict

workers = ['Harry', 'Ron']
vacations = {'Harry': 1, 'Ron': 2}
vacations = defaultdict(list)


class AddNewWorker(forms.Form):
    name = forms.CharField(label='New worker')
    filterOption = forms.ChoiceField(widget=forms.RadioSelect, choices=list(enumerate(workers)))


class ChoiseWorker(forms.Form):
    worker = forms.ChoiceField(choices=tuple(enumerate(workers)))
    vacation_start = forms.IntegerField()
    vacation_finish = forms.IntegerField()


def index(request):
    return render(request, 'index.html', context={'workers': workers})


def add_worker(request):
    if request.method == 'POST':
        form = AddNewWorker(request.POST)
        if form.is_valid():
            worker = form.cleaned_data['name']
            workers.append(worker)
        elif ChoiseWorker(request.POST).is_valid():
            print('SSSSSSSSS')
            form = ChoiseWorker(request.POST)
            vacations[workers[int(form.data['worker'])]] += list(
                range(int(form.data['vacation_start']), int(form.data['vacation_finish']) + 1))
            print(vacations)
        else:
            print('ERROROROROOROR')
            return render(request, 'index.html')

    return render(request, 'add_worker.html', context={'form': AddNewWorker(),
                                                       'form2': ChoiseWorker(),
                                                       'workers': workers})


def two(request):
    return HttpResponse('asdasdas')
