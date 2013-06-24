from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    #shared_with = models.ManyToManyField(User)

    def __unicode__(self):
        return "%s <%s's list of %s items>" % (self.title, self.owner.username, self.item_set.count())


class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User)
    todolist = models.ForeignKey(TodoList)
    finished = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    due_on = models.DateField(null=True)
    due_at = models.TimeField(null=True)
    priority = models.IntegerField(default=3)

    def __unicode__(self):
        return "%s <%s:%s>" % (self.title, self.owner.username, self.todolist.title)

