from django.shortcuts import render,redirect
from django.urls import reverse
from accounts.forms import (
	RegistrationFrom, 
	EditProfileForm
	)
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate,login




def register(request):
	if request.method =='POST':
		form = RegistrationFrom(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST.get('username')
			password = request.POST.get('password1')
			user = authenticate(
				request=request,
				username=username,
				password=password
				)
			login(request, user)
			return redirect(reverse('home:home'))
	else:
		form = RegistrationFrom()

	args = {'form': form}
	return render(request, 'accounts/reg_form.html', args)


def view_profile(request, pk=None):
	storage = messages.get_messages(request)
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user
	args = {'user':user, 'messages':storage}
	return render(request, 'accounts/view_profile.html', args)


def edit_profile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect(reverse('accounts:view_profile'))

	else:
		form = EditProfileForm(instance=request.user)

	args = {'form': form}
	return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			messages.success(request, 'Your password has been changed successfully')
			update_session_auth_hash(request, form.user)
			return redirect(reverse('accounts:view_profile'))

	else:
		form = PasswordChangeForm(user=request.user)

	args = {'form': form}
	return render(request, 'accounts/change_password.html', args)
	