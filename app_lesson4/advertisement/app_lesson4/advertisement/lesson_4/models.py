from django.db import models
from django.db import migrations
class Advertisement(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2,
    )
    auction = models.BooleanField(
        verbose_name="Торг",
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редоктирования"
    )
    from django.contrib import admin

    @admin.display(description="дата создания")
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
    
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:S")
            return format_html(
                "<span>Сегодня в {}</span>",created_time
            )
        
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")


 
    class Meta: 
        db_table = 'Объявления'
    def __str__(self): 
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'