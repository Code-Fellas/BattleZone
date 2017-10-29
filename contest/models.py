from django.db import models
# Create your models here.


class Contests(models.Model):
    title = models.CharField(max_length=255,default=None)
    contest_code = models.CharField(max_length=20, unique=True, blank=False)
    date = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    duration = models.BigIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contests'


class Problem(models.Model):
    title = models.CharField(max_length=255,default='A')
    problem_code = models.CharField(max_length=20)
    contest = models.ForeignKey('Contests')
    problem_statement = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'problems'


class Testcases(models.Model):
    problem = models.ForeignKey('Problem')
    input = models.TextField()
    output = models.TextField()
    is_sample = models.BooleanField(default=False)
    marks = models.IntegerField(default=20)

    class Meta:
        db_table = 'testcases'
