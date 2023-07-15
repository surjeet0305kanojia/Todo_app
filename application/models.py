from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# title
# status
# date (present)
# user 
# priority


class Todo(models.Model):
    # choices for status 
    status_choice=[
        ('c','completed'),
        ('p','pending')

    ]
    # priorities option
    priority_choice=[
        ('1','1️⃣'),
        ('2','2️⃣'),
        ('3','3️⃣'),
        ('4','4️⃣'),
        ('5','5️⃣'),
        ('6','6️⃣'),
        ('7','7️⃣'),
        ('8','8️⃣'),
        ('9','9️⃣'),
        ('10','🔟')
    ]

    title=models.CharField(max_length=50)
    status=models.CharField(max_length=2 ,choices=status_choice)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    priority=models.CharField(max_length=10 ,choices=priority_choice)


