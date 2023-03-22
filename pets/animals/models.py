from django.db import models


class KindOfAnimals(models.Model):
    title = models.CharField(
        'Вид питомца',
        max_length=50,
        unique=True
    )
    description = models.TextField(
        'Описание вида питомца',
    )
    slug = models.SlugField(
        'Слаг питомца для ссылки',
        unique=True,
        max_length=50
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Вид животного'
        verbose_name_plural = 'Виды животных'


class Pets(models.Model):
    breed = models.CharField(
        'Порода питомца',
        max_length=50,
    )
    description = models.TextField(
        'Описание породы питомца'
    )
    kind = models.ForeignKey(
        KindOfAnimals,
        verbose_name='Вид питомца',
        on_delete=models.CASCADE
    )
    slug = models.SlugField(
        'Слаг породы питомца',
        max_length=50,
        unique=True
    )
    image = models.ImageField(
        'Картика питомца',
        upload_to='media/'
    )
    pub_date = models.DateTimeField(
        'Время создания записи',
        auto_now_add=True
    )
    upd_date = models.DateTimeField(
        'Время изменения записи',
        auto_now=True
    )

    def __str__(self):
        return self.breed

    class Meta:
        ordering = ('-pub_date', 'breed')
