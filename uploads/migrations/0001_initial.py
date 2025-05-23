# Generated by Django 5.1.6 on 2025-03-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('research_paper', 'Research Paper'), ('thesis', 'Thesis'), ('certificate', 'Certificate'), ('other', 'Other'), ('Report', 'Report')], default='other', max_length=50)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
