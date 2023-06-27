from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     first_name = db.Column(db.String(length=30), nullable=False, unique=False)
#     last_name = db.Column(db.String(length=30), nullable=False, unique=False)
#     email = db.Column(db.String(length=50), nullable=False, unique=True)
#     password_hash = db.Column(db.String(length=50), nullable=False)
#     #tickets = db.relationship('Ticket', backref='owned_user', lazy=True)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True) # If the project gets deleted, all tickets belonging to that project will be deleted too

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
