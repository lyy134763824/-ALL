from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField('标题',max_length=50,default='',unique=True)
    info = models.CharField('信息',max_length=100,default='')
    pub = models.CharField('出版社',max_length=100,default='')
    price = models.DecimalField('定价',max_digits=7,decimal_places=2,default=0.0)
    make_price = models.DecimalField('零售价格',max_digits=7,decimal_places=2,default=0.0)
    is_active = models.BooleanField('是否活跃',default=True)
    # def __str__(self):
    #     return f'{self.title}_{self.pub}_{self.price}_{self.make_price}'
    class Meta:
        db_table = 'book'

# Create your models here.
class Author(models.Model):
    name = models.CharField('姓名', max_length=11, null=False)
    age = models.IntegerField('年龄',default=1)
    email = models.EmailField('邮箱',null=True)
    class Meta:
        db_table = 'author'

