from django.db import models

class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True, default='')
    isbn_13 = models.CharField(max_length=13, blank=True, default='')
    # book = models.OneToOneField(Book, null=True, blank=True, on_delete=models.CASCADE)
    def __str__ (self):
        return self.isbn_10

class Book(models.Model):
    title = models.CharField(null = False, blank = False, max_length=36, unique = True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    published = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)
    booknumber = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)


    def __str__ (self):
        return self.title
    # Для вывода названий книг в общем списке вместо Book object(1)


class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='characters')

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    book = models.ManyToManyField(Book, related_name='authors')