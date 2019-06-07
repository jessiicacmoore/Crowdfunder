# Generated by Django 2.2.2 on 2019-06-07 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('picture', models.URLField()),
                ('description', models.TextField()),
                ('funding_goal', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('amount_funded', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('number_of_backers', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('tech', 'tech'), ('comics', 'comics'), ('game', 'game'), ('food', 'food'), ('music', 'music')], default='tech', max_length=6)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='crowdfunder.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_amount', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='crowdfunder.Project')),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='crowdfunder.Reward')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='crowdfunder.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
