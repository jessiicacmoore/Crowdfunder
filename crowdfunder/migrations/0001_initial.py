# Generated by Django 2.2.2 on 2019-06-07 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('owned_project', models.CharField(max_length=255)),
                ('funded_project', models.CharField(max_length=255)),
                ('commment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('picture', models.URLField()),
                ('description', models.TextField()),
                ('funding_goal', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('amount_funded', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('number_of_backers', models.IntegerField()),
                ('status_updates', models.CharField(max_length=255)),
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
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='crowdfunder.Reward')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='crowdfunder.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='crowdfunder.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='crowdfunder.Profile')),
            ],
        ),
    ]
