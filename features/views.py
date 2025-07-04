from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.mail import send_mail


def home(request):
    return render(request, 'index.html')







from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from .models import ContactMessage

@require_POST
def contact_view(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    message = request.POST.get("message")

    # Save to database
    contact = ContactMessage.objects.create(
        name=name,
        email=email,
        phone=phone,
        message=message,
    )

    # Build email
    email_subject = f"New Contact Form Submission from {name}"
    email_body = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}

    Message:
    {message}
    """

    # Always try sending, but don't fail if it errors
    email_sent = True
    try:
        send_mail(
            subject=email_subject,
            message=email_body,
            from_email="contact@skkd.com.au",     # Always YOUR domain email
            recipient_list=["contact@skkd.com.au"],
            fail_silently=False,
        )
    except Exception as e:
        email_sent = False

    return JsonResponse({
        "success": True,
        "email_sent": email_sent,
    })
