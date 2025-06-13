from django.shortcuts import render, redirect
from .forms import BookingForm

def home(request):
    # Dummy services data
    services = [
        {
            'name': 'Residential Cleaning',
            'description': 'Complete cleaning of your home including bedrooms, bathrooms, kitchen, and living areas.',
            'icon_class': 'fas fa-home'
        },
        {
            'name': 'Commercial Cleaning',
            'description': 'Professional cleaning services for offices and commercial spaces.',
            'icon_class': 'fas fa-building'
        },
        {
            'name': 'Deep Cleaning',
            'description': 'Thorough cleaning that reaches areas often missed during regular cleaning.',
            'icon_class': 'fas fa-broom'
        },
        {
            'name': 'Move In/Out Cleaning',
            'description': 'Specialized cleaning for when you\'re moving in or out of a property.',
            'icon_class': 'fas fa-truck-moving'
        },
        {
            'name': 'Carpet Cleaning',
            'description': 'Professional carpet cleaning that removes deep stains and odors.',
            'icon_class': 'fas fa-rug'
        },
        {
            'name': 'Window Cleaning',
            'description': 'Interior and exterior window cleaning for crystal clear views.',
            'icon_class': 'fas fa-window-maximize'
        }
    ]

    # Dummy testimonials data
    testimonials = [
        {
            'name': 'Sarah Johnson',
            'content': 'Sparkle Clean transformed my home! The team was professional and thorough. I highly recommend their services.',
            'position': 'Homeowner'
        },
        {
            'name': 'Michael Chen',
            'content': 'Our office has never looked better. The cleaning staff is reliable and does an excellent job every time.',
            'position': 'Office Manager'
        },
        {
            'name': 'David Wilson',
            'content': 'I was amazed at how clean my apartment was after the move-out cleaning. Worth every penny!',
            'position': 'Customer'
        }
    ]

    # Dummy team data
    team = [
        {
            'name': 'Maria Rodriguez',
            'position': 'Lead Cleaner',
            'bio': '5+ years of professional cleaning experience',
            'image': 'images/team1.jpg'
        },
        {
            'name': 'James Wilson',
            'position': 'Commercial Specialist',
            'bio': 'Expert in office and industrial spaces',
            'image': 'images/team2.jpg'
        },
        {
            'name': 'Sophia Chen',
            'position': 'Eco-Cleaning Expert',
            'bio': 'Specializes in green cleaning solutions',
            'image': 'images/team3.jpg'
        }
    ]

    # Dummy stats data
    stats = [
        {'value': '500+', 'label': 'Happy Clients'},
        {'value': '10+', 'label': 'Years Experience'},
        {'value': '50+', 'label': 'Team Members'},
        {'value': '24/7', 'label': 'Support'}
    ]

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # For now, just print the data
            print("Form submitted:", form.cleaned_data)
            return redirect('home')
    else:
        form = BookingForm()

    context = {
        'services': services,
        'testimonials': testimonials,
        'team': team,
        'stats': stats,
        'form': form,
    }
    return render(request, 'index.html', context)