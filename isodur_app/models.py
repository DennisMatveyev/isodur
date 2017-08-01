from django.db import models


class Product1(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    products_photo = models.ImageField(upload_to='products_photo', null=True, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project, null=True, blank=True)
    project_photo = models.ImageField(upload_to='project_photo', null=True, blank=True)
    add_to_slider = models.BooleanField(default=False)


class Partner(models.Model):
    title = models.CharField(max_length=100)
    partner_image = models.ImageField(upload_to='partners', null=True, blank=True)

    def __str__(self):
        return self.title
