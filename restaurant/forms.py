from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Booking, Customer, User
from django.forms import ModelForm


class BookingForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    contact_phone = forms.CharField(max_length=15)
    booking_date = forms.DateField(widget=forms.DateInput
                                   (attrs={'type': 'date',
                                    'min': datetime.now().date()}))
    booking_time = forms.CharField(max_length=5)
    number_of_attendees = forms.IntegerField()

    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'email', 'contact_phone',
                  'booking_date', 'booking_time', 'number_of_attendees']


class UserForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    username = forms.CharField(max_length=40)

    class Meta:
        model = User
        fields = ['username']


class ProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=100)
    contact_phone = forms.CharField(max_length=15)
    email = forms.CharField(max_length=40)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'contact_phone', 'email']


class ImageForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Customer
        fields = ['profile_image']
