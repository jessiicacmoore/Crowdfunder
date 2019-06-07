from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum




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
    funding_goal = models.DecimalField(decimal_places=1, max_digits=4, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    amount_funded = models.DecimalField(decimal_places=1, max_digits=4, default=0)
    number_of_backers = models.IntegerField(default=0)
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default='tech')
    # status_updates =  models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'

    def update_donation_stats(self):
        self.amount_funded = self.donations.aggregate(Sum('donation_amount'))
        self.number_of_backers = self.donations.count(distinct=True)
        self.save()


class Reward(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='rewards')

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')    
    name = models.CharField(max_length=255)
    commment = models.TextField()

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')

class Donation(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='donations')
    project = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donations")
    donation_amount = models.DecimalField(decimal_places=1, max_digits=4, default=0)
    # reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='donations')

