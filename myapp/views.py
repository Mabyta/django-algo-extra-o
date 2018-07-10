from django.shortcuts import HttpResponse
from django.core.mail import EmailMessage

def mensajes(request):
    body='prueba de envio de mensajes'
    email_message = EmailMessage(
        subject='Una Mabyta',
        body=body,
        from_email='daydreamsyndrom@gmail.com',
        to=['adriana.lozano@uabc.edu.mx'],
        )
    email_message.content_subtype = 'html'
    email_message.send()
    return HttpResponse('Esta es mi primera vista!')


