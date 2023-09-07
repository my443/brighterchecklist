from django.core.mail import send_mail
from django.core.mail import EmailMessage, EmailMultiAlternatives

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
    ## Here is a link to how you can send messages from a template: https://stackoverflow.com/questions/3005080/how-to-send-html-email-with-django-with-dynamic-content-in-it

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
