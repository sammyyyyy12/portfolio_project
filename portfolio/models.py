from django.db import models


# =========================
# PROJECT MODEL
# =========================
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


# =========================
# RESUME VERSION CONTROL MODEL
# =========================
class Resume(models.Model):
    version = models.CharField(max_length=50)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Resume {self.version}"

    class Meta:
        ordering = ['-uploaded_at']
class Poem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title