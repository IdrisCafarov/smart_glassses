from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser,FormParser
from django.contrib import messages

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('index')



def index_view(request):
    context = {}
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('dashboard_admin')
        else:
            return redirect('dashboard_user')
    next = request.GET.get("next", None)
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            if next:
                return redirect(next)
        return redirect('index')
    else:
        form = LoginForm()


    context['form'] = form
    return render(request, 'index.html', context)



def dashboard_user_view(request):
    context = {}

    # user = get_object_or_404(MyUser, slug=slug, is_user=True)



    # context['user'] = user

    return render(request, "dashboard_user.html",context)


def dashboard_admin_view(request):

    context = {}

    # user = get_object_or_404(MyUser,slug=slug, is_admin=True)

    smart_users = MyUser.objects.filter(is_user=True)

    # context['user'] = user
    context['smart_users'] = smart_users
    return render(request, "dashboard_admin.html",context)



def admin_help_view(request):
    context = {}
    helps = CallHelp.objects.filter(is_done=False).order_by("-date")
    context["helps"] = helps
    return render(request,"admin_help.html",context)

def make_done_call(request,id):
    call = get_object_or_404(CallHelp,id=id)
    call.is_done = True
    call.save()
    return redirect('admin_help')


def user_details(request, slug):
    context = {}
    user = get_object_or_404(MyUser,slug=slug)

    context["user"] = user


    return render(request,"user_detail.html",context)


def update_view(request):
    context = {}

    usr = get_object_or_404(MyUser, id=request.user.id)

    if request.method == 'POST' and 'sub_main' in request.POST:
        form = UpdateForm(request.POST, request.FILES or None, instance=usr)
        print("qaqaaaaa")
        if form.is_valid():

            print("qaqam zor")

            form.save()
            messages.success(request, 'Your informations succesfully updated!')

            return redirect('edit')
    else:
        form = UpdateForm(instance=usr)

    if request.method == 'POST' and 'modal_sub' in request.POST:
        form_modal = UserDiseaseForm(request.POST, request.FILES or None, user=usr)

        if form_modal.is_valid():
            disease = form_modal.save(commit=False)
            disease.user=usr
            disease.save()
            print("qaqam zor")

            form_modal.save()
            messages.success(request, 'You succesfully added an Disease!')
            return redirect('edit')
    else:
        form_modal = UserDiseaseForm(user=usr)

    context['form'] = form
    context['form_modal'] = form_modal
    context['user'] = usr


    return render(request,"edit_user.html",context)


def delete_disease(request,id):
    object = get_object_or_404(UserDisease,id=id)
    object.delete()
    messages.success(request, 'You succesfully deleted an Disease!')

    return redirect('edit')





class CreateCallView(viewsets.ModelViewSet):
    queryset = CallHelp.objects.all()
    # parser_classes = (MultiPartParser, FormParser)
    serializer_class = CreateCallSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status=201)