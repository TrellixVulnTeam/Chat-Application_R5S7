# Generated by Django 2.1.5 on 2019-02-02 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admindata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(default='null', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='logindata',
            name='username',
        ),
        migrations.AddField(
            model_name='logindata',
            name='usertype',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='logindata',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='logindata',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
