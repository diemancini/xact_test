from django.db import models


class Variable(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)


class BooleanValue(Variable):
    value = models.BooleanField()


class StringValue(Variable):
    value = models.CharField(max_length=100)
