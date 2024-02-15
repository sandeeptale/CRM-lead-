# Generated by Django 4.2.7 on 2023-12-25 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0002_plan_team_plan'),
        ('lead', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='lead_description',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='rating',
        ),
        migrations.CreateModel(
            name='LeadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='leadfiles')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_files', to=settings.AUTH_USER_MODEL)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='lead.lead')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_files', to='team.team')),
            ],
        ),
    ]