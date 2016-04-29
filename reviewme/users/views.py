from django.shortcuts import render
from django.conf import settings

#auth related imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

#imports for validation
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.core.urlresolvers import reverse
import json
from .utils import *

#importing the models
from .models import UserVerification
from django.utils.crypto import get_random_string





# Create your views here.
#method to signup the user and login at the same time
def signupUser(request):
	if request.method == "POST":
		try: #checking the validity of first / last name
			# first_name = request.POST['firstName']
			# last_name = request.POST['lastName']
			# if len(first_name) > 30 or len(first_name) < 2:
			# 	raise ValidationError("Invalid length of first name")

			# if len(last_name) > 30 or len(last_name) < 2:
			# 	raise ValidationError("Invalid length of last name")

		    #checking the validity of email
			email = request.POST['email']
			validate_email(email)

		    #checking min pasword length
			password = request.POST['password']
			if len(password) < 6:
				raise ValidationError("Minimum password length should be 6")

		except (KeyError, ValidationError) as e:
			response = {'status' : 0, 'msg' : str(e)}
			return HttpResponse(json.dumps(response), content_type='application/json')

		response = {}

		try:
			user = User.objects.create_user(email, email, password)
			user.first_name = "Test"
			user.last_name = "Subject"
			user.is_active = False
			user.save()

			response = {'status' : 1}

			ver_key = get_random_string(32)
			user_ver_object = UserVerification(user=user, ver_code=ver_key)
			user_ver_object.save()
			user_uuid = user_ver_object.id

			ver_key_url = request.build_absolute_uri("/user/verification-confirm/")
			ver_key_url = ver_key_url + str(user_uuid) + ver_key

			emailHTML = generate_email_HTML(ver_key_url)

			send_confirmation_email(user.email, emailHTML)

		except IntegrityError:
			response = {'status' : 0, 'msg' : 'User with the entered email already exists'}
			return HttpResponse(json.dumps(response), content_type='application/json')

		except:
			response = {'status' : 0, 'msg' : 'Things just blew up. Contact us at manibatra2002@gmail.com'}
			return HttpResponse(json.dumps(response), content_type='application/json')

	else:
		raise Http404()

	return HttpResponse(json.dumps(response), content_type='application/json')


#method to show a view indacting user to confirm
def verification_start(request):
	context = { 'text' : 'A confirmation email has been sent to your email address. Click on the confirmation\
					link in your email to activate your account', 'heading' : 'confirm your email address' }
	return render(request, 'users/verification.html', context)

#view to show when user clicks the confirmation link
def verification_confirm(request, uuid, ver_code):
	user_ver_object = UserVerification.objects.get(id=uuid)
	if ver_code == user_ver_object.ver_code:
		user = user_ver_object.user
		user.is_active = True
		user.save()
		return HttpResponseRedirect(reverse("users:verification_complete"))

	else:
		raise Http404()
	return render(request, 'users/verification.html', context)

#method to complete the verification process
def verification_complete(request):
	context = { 'text' : 'Your email has been confirmed. You can login and start using Delivrawr now.\
					', 'heading' : 'Email Address Confirmed' }
	return render(request, 'users/verification.html', context)

#method to login the user
def loginUser(request):
	if request.method == "POST":
		try: #checking the validity of email
			email = request.POST['emailLogIn']
			validate_email(email)

		 	#checking the validity of password
			password = request.POST['passwordLogIn']
			if len(password) < 6:
				raise ValidationError("Minimum password length should be 6")

		except (KeyError, ValidationError) as e:
			response = {'status' : 0, 'msg' : str(e)}
			return HttpResponse(json.dumps(response), content_type='application/json')

		user = authenticate(username=email, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				response = {'status' : 1}
			else:
				response = {'status' : 0, 'msg' : 'Please confirm your email address to login'}
		else:
			response = {'status' : 0, 'msg' : 'user could not be loged in! try again'}

	else:
		raise Http404()

	return HttpResponse(json.dumps(response), content_type='application/json')


#method to log the user out
def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('home:landing'))

