# from django import forms
# from .models import Booking

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['name', 'email', 'phone', 'service', 'date', 'message']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#             'message': forms.Textarea(attrs={'rows': 4}),
#         }