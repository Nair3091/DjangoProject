from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    code_snippet = models.TextField(blank=True, null=True)  # Add this field
    code_file = models.FileField(upload_to='uploads/', blank=True, null=True)  # Add this field for file upload


class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)  # New field for file upload

    def __str__(self):
        return self.content[:50]
