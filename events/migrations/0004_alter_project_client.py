# Generated by Django 3.2.9 on 2021-12-26 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_project_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='events.client'),
        ),
    ]
