from django.db import models
from django.db.models import IntegerField

FOOD_CHOICES = (
    ("food1", "Первый тип питания"),
    ("food2", "Второй тип питания"),
    ("food3", "Третий тип питания")
)


class HotelBuilding(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'корпус'
        verbose_name_plural = 'Корпуса'


class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'должность'
        verbose_name_plural = 'Должности'


class Staff(models.Model):
    name = models.CharField(max_length=150)
    birthday_date = models.DateTimeField('birthday date')
    passport_serial = models.CharField(max_length=4)
    passport_number = models.CharField(max_length=6)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    tin = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'сотрудника'
        verbose_name_plural = 'Сотрудники'


class Client(models.Model):
    name = models.CharField(max_length=150)
    birthday_date = models.DateTimeField('birthday date')
    passport_serial = models.CharField(max_length=4)
    passport_number = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural = 'Клиенты'


class TypeService(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'тип услуги'
        verbose_name_plural = 'Типы услуг'


class Service(models.Model):
    name = models.CharField(max_length=100)
    type_service = models.ForeignKey(TypeService, on_delete=models.CASCADE)

    cost = models.FloatField(max_length=10)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'услугу'
        verbose_name_plural = 'Услуги'


class Room(models.Model):
    name = models.CharField(max_length=100)
    number_rooms = IntegerField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'комнату'
        verbose_name_plural = 'Комнаты'


class EntryCustomer(models.Model):
    number = models.IntegerField()
    create_date = models.DateTimeField('create document date')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    department = models.ForeignKey(HotelBuilding, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date_arrival = models.DateTimeField('arrival date')
    date_departure = models.DateTimeField('departure date')
    comment = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    food = models.CharField(max_length=9,
                            choices=FOOD_CHOICES,
                            default="food1")
    cost = models.FloatField(max_length=10)
    number_days = models.IntegerField()

    def __str__(self):
        return f"Документ \"Заезд клиента\"№{self.number}"

    def __unicode__(self):
        return self.number

    class Meta:
        verbose_name = 'заезд клиента'
        verbose_name_plural = 'Заезды клиентов'


class DenyRoom(models.Model):
    number = models.IntegerField()
    create_date = models.DateTimeField('create document date')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    department = models.ForeignKey(HotelBuilding, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    deny_reason = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    food = models.CharField(max_length=9,
                            choices=FOOD_CHOICES,
                            default="food1")
    cost_to_deny = models.FloatField(max_length=10)
    days_remaining = models.IntegerField()

    def __str__(self):
        return f"Документ \"Отказ клиента\"№{self.number}"

    def __unicode__(self):
        return self.number

    class Meta:
        verbose_name = 'отказ клиента'
        verbose_name_plural = 'Отказы клиентов'


class DepartureCustomer(models.Model):
    number = models.IntegerField()
    create_date = models.DateTimeField('create document date')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    department = models.ForeignKey(HotelBuilding, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    review = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    food = models.CharField(max_length=9,
                            choices=FOOD_CHOICES,
                            default="food1")
    cost_to_deny = models.FloatField(max_length=10)
    days_remaining = models.IntegerField()

    def __str__(self):
        return f"Документ \"Выезд клиента\"№{self.number}"

    def __unicode__(self):
        return self.number

    class Meta:
        verbose_name = 'выезд клиента'
        verbose_name_plural = 'Выезды клиентов'