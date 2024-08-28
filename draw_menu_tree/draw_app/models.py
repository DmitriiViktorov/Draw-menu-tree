from django.db import models


class Menu(models.Model):
    """
    Модель для главных разделов меню.

    Attributes:
        title (CharField): Название главного раздела меню.
    """
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.title)


class MenuItem(models.Model):
    """
    Модель для подразделов меню.

    Attributes:
        title (CharField): Название подраздела меню.
        url (CharField): URL подраздела меню.
        parent (ForeignKey): Родительский подраздел меню.
        menu (ForeignKey): Главный раздел меню, к которому принадлежит подраздел.
        order (IntegerField): Порядок отображения подраздела меню.
    """
    title = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if self.parent:
            self.menu = self.parent.menu
            self.order = self.parent.order + 1
            self.url = self.parent.url + '/' + self.title
        else:
            self.menu = self.menu
            self.order = 0
            self.url = self.menu.title + '/' + self.title
        super(MenuItem, self).save(*args, **kwargs)

    def __lt__(self, other):
        if not isinstance(other, MenuItem):
            return NotImplemented
        return self.title < other.title
