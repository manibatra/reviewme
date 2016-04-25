from django.conf import settings

#importing the django templete renderer
from django.template import loader, Context

#importing requests lib to send mail
import requests




#method to generate emailHTML
def generate_email_HTML(ver_key_url):
	context_dict = {}
	context_dict['ver_key_url'] = ver_key_url

	context = Context(context_dict)

	template = loader.get_template("users/confirm_signup.html")

	return template.render(context)


#method to send the mail to the customer
def send_confirmation_email(customer_email, emailHTML):
		return requests.post(
				settings.MAILGUN_URL + "/messages",
				auth=("api", settings.MAILGUN_API_KEY),
				data={"from": "Deliverawr <mailgun@" + settings.MAILGUN_DOMAIN + ">",
							"to": [customer_email],
							"subject": "Confirm Email Address",
							"html": emailHTML
	})

