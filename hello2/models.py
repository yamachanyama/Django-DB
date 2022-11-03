from django.db import models
from django.contrib.auth.models import User #Userを使う時にはこのように記載

# Create your models here.
class Message(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=300)
  pub_date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return '<Message:id=' + str(self.id) + ', ' + \
      self.title + '(' + str(self.pub_date) + ')>'

  class Meta:
    # pub_date順に並び変える
    ordering = ('pub_date',)