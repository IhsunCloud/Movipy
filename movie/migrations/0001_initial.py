# Generated by Django 4.1.3 on 2022-11-14 22:58

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Firstname')),
                ('last_name', models.CharField(max_length=100, verbose_name='Lastname')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Male'), (2, 'Female')], default=1, verbose_name='Gender')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='crew/avatars/', verbose_name='Avatar')),
                ('is_valid', models.BooleanField(default=True, verbose_name='Is Valid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Crew',
                'verbose_name_plural': 'Crews',
                'ordering': ('-first_name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('is_valid', models.BooleanField(default=True, verbose_name='Is Valid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='Slug')),
                ('description', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('trailer', models.FileField(blank=True, null=True, upload_to='', verbose_name='Trailer')),
                ('thumbnail', models.ImageField(null=True, upload_to='movie/images/', verbose_name='Thumbnail')),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default='D', max_length=1, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='MovieRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('is_valid', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Movie', to='movie.movie')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='MovieCrew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_crew', to='movie.crew')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_crew', to='movie.movie')),
                ('role', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_crew', to='movie.movierole')),
            ],
            options={
                'unique_together': {('movie', 'crew', 'role')},
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='crew',
            field=models.ManyToManyField(related_name='Crew', through='movie.MovieCrew', to='movie.crew'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='movie.genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MovieRole', to='movie.movierole'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('text', models.CharField(max_length=254, verbose_name='Text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='By User')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='movie.comment', verbose_name='Parent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]