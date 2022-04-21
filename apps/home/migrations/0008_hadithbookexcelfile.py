# Generated by Django 3.2.6 on 2022-04-12 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_hadithbook_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='HadithBookExcelFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_url', models.FileField(upload_to='')),
                ('HadithBookMainChapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.hadithbookmainchapter')),
                ('HadithBookSubChapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.hadithbooksubchapter')),
                ('Hadithbook', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.hadithbook')),
            ],
        ),
    ]