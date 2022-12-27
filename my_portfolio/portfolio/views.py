from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, BadHeaderError

import smtplib, ssl

# Create your views here.
def index(request):
    
    return render(request, 'portfolio/index.html')


# contact section for message

def client(request):

    
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
          # my email to content 
        my_email = "mujjungajets@gmail.com"
        passkey = "sphzoclqlizceyiw" # the passkey to my email
        
        email_from = email
        
        email_string = f'''Subject:   {subject}
                        From: {''.join(email_from)},
                        Name:  {name}
                        Message: '\n' {message}'''
        
        # Create a secure default settings context
        
        context = ssl.create_default_context()
        
        #connect to Gmail's SMTP Outgoing Mail server with such context
        
        # with smtplib.SMTP_SSL("smtp.gmail.com", 587, context=context) as server:
        #     # Provide Gmail's login info
        #     server.login(my_email, passkey)
            
        #     # Send mail with email_from, to_addrs, msg, which were set up
            
        #     server.sendmail(email_from, my_email, email_string)
        
        
        
        send_mail(
            subject,
            email_string, # python formated string
            email, # from email
            [my_email], # my own email as adeveloper
            
        )
    else:
        name = ""
        email = ""
        subject = ""
        message = ""
        
    return HttpResponse("Massege sent successfully")