# Generated by Django 4.2.3 on 2023-08-08 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chatroom_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('A', 'MORNING MEETING'), ('B', 'NOOON MEETING'), ('C', 'EVENING MEETING')], default='A', max_length=100)),
                ('date', models.DateField(verbose_name='Event Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.user')),
            ],
        ),
    ]