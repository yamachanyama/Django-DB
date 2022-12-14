import re
from django.db import models
from django.core.validators import ValidationError
from django.contrib.auth import get_user_model

def alpha_only(value):
    if (re.match(r'^[a-zA-Z]*$', value) == None):
        raise ValidationError(
            'Enter only alphabet!', \
            params={'value': value},
        )

class Message(models.Model):
    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="person")
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title + '(' + str(self.pub_date) + ')>'
    
    class Meta:
        ordering = ('pub_date',)

class Comment(models.Model):
    text = models.TextField('コメント内容')
    post = models.ForeignKey(Message, verbose_name='対象記事', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name='親コメント', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]


# from django.core.validators import MinValueValidator

# validators=[MinValueValidator(0)]

