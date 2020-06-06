from django.db import models
from mongoengine import *
from datetime import datetime

connect(db= 'db',
        username= "test",
        password= "test",
        host="mongodb+srv://test:test@cluster0-wp0k4.mongodb.net/test?retryWrites=true&w=majority",
        )
class info(Document):
    COMPANY_NAME = StringField(max_length=200,required=True)
    FRONT_INSIDE_PICTURE = FileField()
    BUSINESS_CARD_IMAGE = FileField()
    uploaded_at = DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.COMPANY_NAME
