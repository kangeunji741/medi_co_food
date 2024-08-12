from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class DiseaseCategory(models.Model):
    dcate_id = models.AutoField(primary_key=True, db_comment='질병카테고리 아이디')
    disease_name = models.CharField(max_length=50, db_comment='질병 이름')

    class Meta:
        db_table = 'disease_category'
        verbose_name = '질병 카테고리'
        verbose_name_plural = '질병 카테고리'

    def __str__(self):
        return self.disease_name
        


class Product(models.Model):
    product_id = models.AutoField(primary_key=True, verbose_name='제품 아이디')
    dcate = models.ForeignKey('DiseaseCategory', null=True, blank=True, on_delete=models.SET_NULL, db_index=True)
    element1 = models.CharField(max_length=50, verbose_name='대분류')
    element2 = models.CharField(max_length=50, verbose_name='중분류')
    element3 = models.CharField(max_length=50, verbose_name='소분류')
    product_name = models.CharField(max_length=50, null=True, blank=True)
    manufacturer = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    site_url = models.URLField(max_length=2000, null=True, blank=True)
    image_url = models.URLField(max_length=2000, null=True, blank=True)
    patient_category = models.CharField(max_length=20, null=True, blank=True)
    nutrient_guide = models.IntegerField(null=True, blank=True)
    carbohydrate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    protein = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    na = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sugars = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    calorie = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='칼로리') 


    class Meta:
        db_table = 'products'
        verbose_name = '제품'
        verbose_name_plural = '제품'

    def __str__(self):
        return self.product_name
        


class Like(models.Model):
    like_id = models.AutoField(primary_key=True, db_comment='좋아요 아이디')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, db_comment='회원 아이디')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, db_comment='제품 아이디')
    created_at = models.DateTimeField(auto_now_add=True, db_comment='등록 일자')

    class Meta:
        db_table = 'likes'
        verbose_name = '좋아요'
        verbose_name_plural = '좋아요'
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} likes {self.product.product_name}"

    @staticmethod
    def toggle_like(user, product):
        like, created = Like.objects.get_or_create(user=user, product=product)
        if not created:
            like.delete()
            return False
        return True
