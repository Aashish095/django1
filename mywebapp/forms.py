from django import forms
from datetime import datetime
from mongoengine import *
class RegistrationForm(forms.Form):  #these will aloud to use all the field
    COMPANY_NAME = StringField(max_length=200,required=True)
    FRONT_INSIDE_PICTURE = FileField()
    BUSINESS_CARD_IMAGE = FileField()
    uploaded_at = DateTimeField(default=datetime.utcnow)