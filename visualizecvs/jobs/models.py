from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name = "Vaga"
        verbose_name_plural = "Vagas"

    def __str__(self):
        return self.name


class CV(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    academic_experience = models.TextField(blank=True)
    professional_experience = models.TextField(blank=True)
    jobs = models.ManyToManyField(Job, related_name='cvs')
    social_links = models.TextField(blank=True)
    file = models.FileField(upload_to="cvs", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Currículo"
        verbose_name_plural = "Currículos"

    def __str__(self):
        return self.name
