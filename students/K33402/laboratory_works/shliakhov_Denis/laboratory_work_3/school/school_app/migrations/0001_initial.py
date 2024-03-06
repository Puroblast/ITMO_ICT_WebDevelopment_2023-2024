# Generated by Django 5.0.2 on 2024-03-06 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Математика', 'Mathematics'), ('Физика', 'Physics'), ('Музыка', 'Music'), ('Химия', 'Chemistry'), ('Спорт', 'Sport'), ('Английский', 'English'), ('Русский язык', 'Russian'), ('Литература', 'Literature')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('room_number', models.IntegerField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.group')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.group')),
                ('lessons', models.ManyToManyField(through='school_app.Grade', to='school_app.lesson')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='students',
            field=models.ManyToManyField(through='school_app.Grade', to='school_app.student'),
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.student'),
        ),
        migrations.AddField(
            model_name='group',
            name='group_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.teacher'),
        ),
        migrations.CreateModel(
            name='TeachProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ManyToManyField(through='school_app.Lesson', to='school_app.group')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.teacher')),
            ],
            options={
                'unique_together': {('teacher', 'subject')},
            },
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(through='school_app.TeachProcess', to='school_app.subject'),
        ),
        migrations.AddField(
            model_name='subject',
            name='teachers',
            field=models.ManyToManyField(through='school_app.TeachProcess', to='school_app.teacher'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teach_process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.teachprocess'),
        ),
        migrations.AddField(
            model_name='group',
            name='teachProcess',
            field=models.ManyToManyField(through='school_app.Lesson', to='school_app.teachprocess'),
        ),
    ]