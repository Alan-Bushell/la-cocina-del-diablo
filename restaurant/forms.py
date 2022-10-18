from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Booking, Customer
from django.forms import ModelForm


class BookingForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    fname = forms.CharField(max_length=40)
    lname = forms.CharField(max_length=100)
    email = forms.EmailField()
    contact_phone = forms.CharField(max_length=15)
    booking_date = forms.DateField(widget=forms.DateInput
                                   (attrs={'type': 'date',
                                    'min': datetime.now().date()}))
    booking_time = forms.CharField(max_length=5)
    pax = forms.IntegerField()

    class Meta:
        model = Booking
        fields = ['fname', 'lname', 'email', 'contact_phone', 'booking_date',
                  'booking_time', 'pax']
