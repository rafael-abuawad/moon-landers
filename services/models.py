from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    image = models.ImageField(upload_to="services")
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    class Areas(models.TextChoices):
        FULLSTACK = "Full-stack Development"
        WEB3 = "Web3 Application"
        API = "RESTful APIs"
        AI = "AI Integration"

    name = models.CharField(max_length=50)
    email = models.EmailField()
    area = models.CharField(
        max_length=22, choices=Areas.choices, default=Areas.FULLSTACK
    )
    content = models.TextField()

    def __str__(self) -> str:
        return f"Message from {self.email}"
