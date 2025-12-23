from django.db import models
from django.contrib.auth.models import User  

class Task(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Görev Başlığı")
    description = models.TextField(blank=True, null=True, verbose_name="Açıklama")
    
    STATUS_CHOICES = [
        ('yapilacak', 'Yapılacak'),
        ('devam_ediyor', 'Devam Ediyor'),
        ('tamamlandi', 'Tamamlandı'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='yapilacak', verbose_name="Durum")
    
    due_date = models.DateField(null=True, blank=True, verbose_name="Bitiş Tarihi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title