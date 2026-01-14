from django.db import models
from django.contrib.auth.models import User
# DİKKAT: Eğer arkadaşının app adı 'tasks' değilse, 
# aşağıdaki 'tasks' yazan yeri onun app adı ile değiştir.
from tasks.models import Task 
from django.db.models.signals import post_save
from django.dispatch import receiver
# 1. BİLDİRİMLER MODELİ
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=255, verbose_name="Mesaj")
    is_read = models.BooleanField(default=False, verbose_name="Okundu mu?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Gönderim Tarihi")

    class Meta:
        verbose_name = "Bildirim"
        verbose_name_plural = "Bildirimler"
        ordering = ['-created_at']

    def _str_(self):
        return f"{self.user.username} - {self.message[:30]}"

# 2. ARŞİV DETAY MODELİ (Opsiyonel ama ödev için iyi durur)
class ArchivedTask(models.Model):
    # Arkadaşının Task modeline birebir bağlıyoruz
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name="archive_details")
    archived_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Arşivlenme Tarihi")
    notes = models.TextField(blank=True, null=True, verbose_name="Arşiv Notu")

    def _str_(self):
        return f"Arşiv: {self.task.title}"
    from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Task)
def create_notification_on_complete(sender, instance, created, **kwargs):
    # Eğer görev durumu 'tamamlandi' olarak güncellendiyse
    if instance.status == 'tamamlandi':
        Notification.objects.get_or_create(
            user=instance.user,
            message=f"'{instance.title}' isimli göreviniz tamamlandı ve arşivlendi!"
        )