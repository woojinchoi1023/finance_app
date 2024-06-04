from django.db import models
from django.conf import settings

# Create your models here.
class Exchangerate(models.Model):
  bkpr = models.FloatField()
  cur_nm = models.CharField(max_length=16)
  cur_unit = models.CharField(max_length=16)
  deal_bas_r = models.FloatField()
  kftc_bkpr = models.FloatField()
  kftc_deal_bas_r = models.FloatField()
  ten_dd_efee_r = models.IntegerField()
  ttb = models.FloatField()
  tts = models.FloatField()

class Product(models.Model):
  # baseList
  category = models.IntegerField()  # 예적금 - 0: 예금, 1: 적금
  dcls_month = models.TextField()  # 공시 제출월 [YYYYMM]
  fin_co_no = models.TextField()  # 금융회사 코드
  kor_co_nm = models.TextField()  # 금융회사 명
  fin_prdt_cd = models.TextField()  # 금융상품 코드
  fin_prdt_nm = models.TextField()  # 금융 상품명
  join_way = models.TextField()  # 가입 방법
  spcl_cnd = models.TextField()  # 우대조건
  join_deny = models.TextField()  # 가입제한 - 1: 제한없음, 2: 서민전용, 3: 일부제한
  join_member = models.TextField()  # 가입대상
  etc_note = models.TextField()  # 기타 유의사항
  
  # optionList
  intr_rate_type = models.TextField(null=True)  # 저축 금리 유형
  intr_rate_type_nm = models.TextField(null=True)  # 저축 금리 유형명
  rsrv_type = models.TextField(null=True)  # 적립 유형
  rsrv_type_nm = models.TextField(null=True)  # 적립 유형명
  save_trm = models.TextField()  # 저축 기간 [단위: 개월]
  intr_rate = models.IntegerField(null=True)  # 저축 금리
  intr_rate2 = models.IntegerField(null=True)  # 최고 우대금리

class User_Product(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  product = models.ForeignKey("Product", on_delete=models.CASCADE)
  balance = models.IntegerField()
  profit = models.FloatField()
  created_at = models.DateTimeField()
  
class Question(models.Model):
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)