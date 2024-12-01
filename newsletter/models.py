from django.db import models


class Recipient(models.Model):
    """ Модель: Получатель рассылок """

    name = models.CharField(max_length=50, verbose_name="Название рассылки", unique=True)
    fio = models.CharField(max_length=200, verbose_name="ФИО")
    comment = models.TextField(verbose_name="Комментарий", blank=True, null=True)

    def __str__(self):
        return f"{self.fio} - {self.name}"

    class Meta:
        verbose_name = "получатель"
        verbose_name_plural = "получатели"
        ordering = ["fio"]


class Message(models.Model):
    """ Модель: Сообщения """

    name = models.CharField(max_length=50, verbose_name="Тема письма")
    text = models.TextField(verbose_name="Текст сообщения")

    def __str__(self):
        return {self.name}

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

    def __str__(self):
        return {self.message}

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["start_mail"]
