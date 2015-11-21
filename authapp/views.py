from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.template.defaulttags import csrf_token
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from django.http import HttpResponseRedirect
from authapp.forms import LoginForm, SignUpForm
from app1.forms import EmpleadoForm
from app1.models import Empleado

def login_view(request):
    mensaje = ""
    if request.user.is_authenticated() :
        return  HttpResponseRedirect('/')
    else:
        if request.POST :
            form = LoginForm(request.POST)
            if form.is_valid():
			    usuario = form.cleaned_data['usuario']
			    password = form.cleaned_data['password']
			    usuariov = authenticate(username=usuario, password=password)
			    if usuariov is not None and usuariov.is_active:
			        login(request, usuariov)
			        return HttpResponseRedirect('/')
			    else:
			        mensaje ="Usuario y/o Contrasena incorrecta"
        form = LoginForm()
        ctx = {'form':form, 'mensaje':mensaje}
        return render_to_response('authapp/login.html', ctx, RequestContext(request))

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def signup(request):
    if request.POST:  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        empleado_form = EmpleadoForm(request.POST)
        if form.is_valid() and empleado_form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            is_staff = form.cleaned_data["is_staff"]

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.is_staff = is_staff

            # Save new user attributes
            user.save()

            empleado = empleado_form.save(commit=False)
            empleado.user = user
            empleado.save()

            return HttpResponseRedirect('/empleados')  # Redirect after POST
    else:
        form = SignUpForm()
        empleado_form = EmpleadoForm(request.POST)

    data = {
        'form': form, 'empleado_form': empleado_form
    }
    return render_to_response('authapp/signup.html', data, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def ver(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    usuario = get_object_or_404(User, id=empleado.user_id)
    form = SignUpForm(instance=usuario)
    empleado_form = EmpleadoForm(instance=empleado)

    for campo in form.fields:
		form.fields[campo].widget.attrs['disabled'] = True
    for campo in empleado_form.fields:
		empleado_form.fields[campo].widget.attrs['disabled'] = True

    data = {
        'form': form, 'empleado_form': empleado_form, 'id': id
    }
    return render_to_response('authapp/signup.html', data, context_instance=RequestContext(request))


@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def editar(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    usuario = get_object_or_404(User, id=empleado.user_id)
    if request.POST:  # If the form has been submitted...
        form = SignUpForm(request.POST, instance=usuario)  # A form bound to the POST data
        empleado_form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid() and empleado_form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            is_staff = form.cleaned_data["is_staff"]

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields

            # Save new user attributes
            user = form.save(commit=False)
            user.save()

            empleado = empleado_form.save(commit=False)
            empleado.user = user
            empleado.save()

            return HttpResponseRedirect('/empleados')  # Redirect after POST
    else:
        form = SignUpForm(instance=usuario)
        empleado_form = EmpleadoForm(instance=empleado)

    data = {
        'form': form, 'empleado_form': empleado_form
    }
    return render_to_response('authapp/signup.html', data, context_instance=RequestContext(request))
