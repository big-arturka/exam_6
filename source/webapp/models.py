from django.db import models

DEFAULT_STATUS = "active"
ENTRY_STATUS = (
    (DEFAULT_STATUS, "Активно"),
    ("active", "Активно"),
    ("blocked", "Заблокировано"),
)


class Entry(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор')
    email = models.EmailField(max_length=50, verbose_name='Почта')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    status = models.CharField(max_length=20, verbose_name='Статус', choices=ENTRY_STATUS, default=DEFAULT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return f'{self.author} - {self.status}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
