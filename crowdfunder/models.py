from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

from datetime import date




CATEGORY_CHOICES = (
    ('tech','tech'),
    ('comics', 'comics'),
    ('game','game'),
    ('food','food'),
    ('music','music'),
)

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=255)
    picture = models.URLField()
    description = models.TextField()
    funding_goal = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    amount_funded = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    number_of_backers = models.IntegerField(default=0)
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default='tech')
    # status_updates =  models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'

    def update_total_funded(self):
        donations = self.donations.aggregate(Sum('donation_amount'))
        self.amount_funded = donations['donation_amount__sum']
        self.save()

    def update_total_backers(self):
        unique_backers = self.donations.values('user').distinct()
        self.number_of_backers = unique_backers.count()
        self.save()

    def is_past_due(self):
        return date.today() > self.end_date

    def days_until_due(self):
        difference = self.end_date - self.start_date
        return difference.days


# class Reward(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(null=True)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='rewards')

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    # reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='donations')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='donations')
    donation_amount = models.DecimalField(decimal_places=2, max_digits=5, default=0)

    def __str__(self):
        return f'{self.donation_amount}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')


