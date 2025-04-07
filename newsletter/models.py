from django.db import models

from users.models import User


class Recipient(models.Model):
    """ Модель: Получатель рассылок """

    email = models.EmailField(verbose_name="Почта получателя", unique=True, blank=True, null=True)
    fio = models.CharField(max_length=200, verbose_name="ФИО")
    comment = models.TextField(verbose_name="Комментарий", blank=True, null=True)
    owner = models.ForeignKey(User, verbose_name="Автор рассылки", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.fio} - {self.email}"

    class Meta:
        verbose_name = "получатель"
        verbose_name_plural = "получатели"
        ordering = ["fio"]
        permissions = [
            ("can_edit", "Can Edit")
        ]


class Message(models.Model):
    """ Модель: Сообщения """

    name = models.CharField(max_length=50, verbose_name="Тема письма")
    text = models.TextField(verbose_name="Текст сообщения")
    owner = models.ForeignKey(User, verbose_name="Автор рассылки", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"
        ordering = ["name"]


class Newsletter(models.Model):
    """ Модель: Рассылка """

    CREATED = "Создана"
    LAUNCHED = "Запущена"
    FINISHED = "Завершена"

    STATUS_CHOICE = [(CREATED, 'Создана'),
                     (LAUNCHED, 'Запущена'),
                     (FINISHED, 'Завершена')]

    start_mail = models.DateField(verbose_name="Дата начала отправки")
    end_mail = models.DateField(verbose_name="Дата конца отправки")
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, verbose_name="Статус рассылки", default=CREATED)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение")
    recipient = models.ManyToManyField(Recipient, verbose_name="Получатель")
    owner = models.ForeignKey(User, verbose_name="Автор рассылки", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.message}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["start_mail"]
        permissions = [
            ("set_active", "Set active"),
            ("can_edit", "Can Edit")
        ]


class Try(models.Model):
    """ Модель: Рассылка """

    send_time = models.DateTimeField(verbose_name="Дата попытки отправки")
    status = models.CharField(max_length=50, verbose_name="Статус отправки")
    response = models.TextField(verbose_name="Текст ошибки")
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name="Рассылка")

    def __str__(self):
        return f"{self.send_time} - {self.status}"

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"
        ordering = ["send_time"]
        permissions = [
            ("can_edit", "Can Edit")
        ]
