from django.core.mail import send_mail
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def sendmail_simple():
    send_mail(
        "Subject here",
        "Here is the message.",
        "admin@brighterchecklist.com",
        ["fortyfour-three@teksavvy.com"],
        fail_silently=False,
    )

def sendmail_by_class():
    ## You can also use the EmailMessage class for simple messages.

    email = EmailMultiAlternatives()
    email.from_email = 'admin@brighterchecklist.com'
    email.to = ["fortyfour-three@teksavvy.com"]
    email.subject = 'Welcome to BighterChecklist'
    email.body = 'Welcome to BrighterChecklist.\n Please find your instructions attached.'
    email.attach_alternative('<b>Welcome to BrighterChecklist.</b>Please find your instructions attached.', 'text/html')
    # msg.attach_alternative(html_content, "text/html")

    ## Add an Attachment.
    # file = open(r'C:\Projects\092 BrighterChecklist\misc\sample-pdf.pdf', "rb")
    # email.attach('sample-pdf.pdf', file.read() ,'application/pdf')

    email.send()

def sendemail_with_template(email_to, context):


    ## Here is a link to how you can send messages from a template: https://stackoverflow.com/questions/3005080/how-to-send-html-email-with-django-with-dynamic-content-in-it
    email = EmailMultiAlternatives()
    email.from_email = 'admin@brighterchecklist.com'
    email.to = [email_to]
    email.bcc = ["john@johnv.ca"]
    email.subject = 'Welcome to BighterChecklist'

    html_content = render_to_string('email/welcome_template.html', context)  # render with dynamic value
    text_content = strip_tags(html_content)

    email.body = text_content
    email.attach_alternative(html_content, 'text/html')

    email.send()