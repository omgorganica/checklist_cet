from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from requests import auth
from .forms import QuestionnaireForm, DateForm
from .models import VehicleUnit, VehicleType, Questionnaire
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib import messages
from .filters import QuestionnaireFilter


def index(request):
    vehicle_type_list = VehicleType.objects.all()
    if request.method == "POST":
        logout(request)
        username = request.POST.get('Login')
        password = 'DNHnxvxF1'
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вход выполнен')
        else:
            messages.error(request, "Неправильный логин")

    params = {
        'vehicle_type_list': vehicle_type_list,
    }
    return render(request, 'checklist/index.html', params)


def inside_vehicle_type(request):
    vehicle_type = request.GET.get('vehicle_type')
    vehicles_list = VehicleUnit.objects.filter(vehicle_type=vehicle_type)
    vehicle_type_name = VehicleType.objects.get(id=vehicle_type)

    params = {
        'vehicles_list': vehicles_list,
        'vehicle_type_name': vehicle_type_name
    }
    return render(request, 'checklist/inside_vehicle_type.html', params)


def questionnaire_new(request):
    vehicle_type = request.GET.get('vehicle_type')
    vehicle_type_name = VehicleType.objects.get(id=vehicle_type)
    vehicle_registred_number = request.GET.get('vehicle_registred_number')
    if request.method == "POST":
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user ="{} {}".format(request.user.first_name, request.user.last_name)
            post.registred_number = vehicle_registred_number
            post.vehicle_type = vehicle_type_name
            post.published_date = datetime.now()
            if post.q1:
                post.total_score += 1
            if post.q2:
                post.total_score += 1
            if post.q3:
                post.total_score += 1
            if post.q4:
                post.total_score += 1
            if post.q5:
                post.total_score += 1
            if post.q6:
                post.total_score += 1
            if post.q7:
                post.total_score += 1
            if post.q8:
                post.total_score += 1
            if post.q9:
                post.total_score += 1
            if post.q10:
                post.total_score += 1
            if post.q12 == '':
                post.total_score += 1
            post.save()
            logout(request)
            return redirect('index')
    else:
        form = QuestionnaireForm()

    return render(request, 'checklist/questionnaire.html', {'form': form, 'vehicle_type_name': vehicle_type_name})


def result_list(request):
    f = QuestionnaireFilter(request.GET, queryset=Questionnaire.objects.order_by('-date'))
    params = {
        'filter': f,
    }
    return render(request, 'checklist/result.html', params)



def specific_result_id(request):
    result_id = request.GET.get('result_id')
    result = Questionnaire.objects.get(id=result_id)
    params = {
        'result': result,
    }
    return render(request, 'checklist/specific_result_id.html', params)


def result_vehicle_type(request):
    vehicle_type = request.GET.get('vehicle_type')
    result = Questionnaire.objects.filter(vehicle_type=vehicle_type).order_by('-date')
    params = {
        'result': result,
        'vehicle_type': vehicle_type
    }
    return render(request, 'checklist/result_vehicle_type.html', params)


def result_vehicle_id(request):
    registred_number = request.GET.get('registred_number')
    result = Questionnaire.objects.filter(registred_number=registred_number).order_by('-date')
    params = {
        'result': result,
        'registred_number': registred_number,
    }
    return render(request, 'checklist/result_vehicle_id.html', params)


def result_by_user(request):
    user = request.GET.get('user')
    result = Questionnaire.objects.filter(user=user).order_by('-date')
    params = {
        'result': result,
        'user': user
    }
    return render(request, 'checklist/result_by_user.html', params)


def _logout(request):
    logout(request)
    return HttpResponseRedirect("/")
