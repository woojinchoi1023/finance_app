from django.shortcuts import render

import os
import requests
from openai import OpenAI
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .serializers import ExchangerateSerializer, ProductListSerializer, SubscribeSerializer
from .models import Product, User_Product, Question

FILE_PATH = os.path.join(os.path.dirname(__file__), 'train.txt')

# Create your views here.
@api_view(['GET'])
def exchange_rate(request):
    if request.method == 'GET':
        URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
        API_KEY = settings.EXCHANGE_RATE_API_KEY
        res = requests.get(
            url=URL, 
            params={
                'authkey': API_KEY,  
                'data': 'AP01'
            }
        )
        data = res.json()
        for i in range(len(data)):
            info = data[i]
            for key in ['bkpr', 'deal_bas_r', 'kftc_bkpr', 'kftc_deal_bas_r', 'ten_dd_efee_r', 'ttb', 'tts', 'yy_efee_r']:
                if key == 'result':
                    continue
                info[key] = info[key].replace(',', '')
                info[key] = float(info[key])
        serializer = ExchangerateSerializer(data, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'data':[
    {
        "bkpr": 371.0,
        "cur_nm": "아랍에미리트 디르함",
        "cur_unit": "AED",
        "deal_bas_r": 371.11,
        "kftc_bkpr": 371.0,
        "kftc_deal_bas_r": 371.11,
        "ten_dd_efee_r": 0,
        "ttb": 367.39,
        "tts": 374.82
    },
    {
        "bkpr": 902.0,
        "cur_nm": "호주 달러",
        "cur_unit": "AUD",
        "deal_bas_r": 902.78,
        "kftc_bkpr": 902.0,
        "kftc_deal_bas_r": 902.78,
        "ten_dd_efee_r": 0,
        "ttb": 893.75,
        "tts": 911.8
    },
    {
        "bkpr": 3615.0,
        "cur_nm": "바레인 디나르",
        "cur_unit": "BHD",
        "deal_bas_r": 3615.75,
        "kftc_bkpr": 3615.0,
        "kftc_deal_bas_r": 3615.75,
        "ten_dd_efee_r": 0,
        "ttb": 3579.59,
        "tts": 3651.9
    },
    {
        "bkpr": 1009.0,
        "cur_nm": "브루나이 달러",
        "cur_unit": "BND",
        "deal_bas_r": 1009.48,
        "kftc_bkpr": 1009.0,
        "kftc_deal_bas_r": 1009.48,
        "ten_dd_efee_r": 0,
        "ttb": 999.38,
        "tts": 1019.57
    },
    {
        "bkpr": 995.0,
        "cur_nm": "캐나다 달러",
        "cur_unit": "CAD",
        "deal_bas_r": 995.8,
        "kftc_bkpr": 995.0,
        "kftc_deal_bas_r": 995.8,
        "ten_dd_efee_r": 0,
        "ttb": 985.84,
        "tts": 1005.75
    },
    {
        "bkpr": 1489.0,
        "cur_nm": "스위스 프랑",
        "cur_unit": "CHF",
        "deal_bas_r": 1489.32,
        "kftc_bkpr": 1489.0,
        "kftc_deal_bas_r": 1489.32,
        "ten_dd_efee_r": 0,
        "ttb": 1474.42,
        "tts": 1504.21
    },
    {
        "bkpr": 188.0,
        "cur_nm": "위안화",
        "cur_unit": "CNH",
        "deal_bas_r": 188.01,
        "kftc_bkpr": 188.0,
        "kftc_deal_bas_r": 188.01,
        "ten_dd_efee_r": 0,
        "ttb": 186.12,
        "tts": 189.89
    },
    {
        "bkpr": 197.0,
        "cur_nm": "덴마아크 크로네",
        "cur_unit": "DKK",
        "deal_bas_r": 197.77,
        "kftc_bkpr": 197.0,
        "kftc_deal_bas_r": 197.77,
        "ten_dd_efee_r": 0,
        "ttb": 195.79,
        "tts": 199.74
    },
    {
        "bkpr": 1475.0,
        "cur_nm": "유로",
        "cur_unit": "EUR",
        "deal_bas_r": 1475.69,
        "kftc_bkpr": 1475.0,
        "kftc_deal_bas_r": 1475.69,
        "ten_dd_efee_r": 0,
        "ttb": 1460.93,
        "tts": 1490.44
    },
    {
        "bkpr": 1734.0,
        "cur_nm": "영국 파운드",
        "cur_unit": "GBP",
        "deal_bas_r": 1734.07,
        "kftc_bkpr": 1734.0,
        "kftc_deal_bas_r": 1734.07,
        "ten_dd_efee_r": 0,
        "ttb": 1716.72,
        "tts": 1751.41
    },
    {
        "bkpr": 174.0,
        "cur_nm": "홍콩 달러",
        "cur_unit": "HKD",
        "deal_bas_r": 174.67,
        "kftc_bkpr": 174.0,
        "kftc_deal_bas_r": 174.67,
        "ten_dd_efee_r": 0,
        "ttb": 172.92,
        "tts": 176.41
    },
    {
        "bkpr": 8.0,
        "cur_nm": "인도네시아 루피아",
        "cur_unit": "IDR(100)",
        "deal_bas_r": 8.52,
        "kftc_bkpr": 8.0,
        "kftc_deal_bas_r": 8.52,
        "ten_dd_efee_r": 0,
        "ttb": 8.43,
        "tts": 8.6
    },
    {
        "bkpr": 869.0,
        "cur_nm": "일본 옌",
        "cur_unit": "JPY(100)",
        "deal_bas_r": 869.63,
        "kftc_bkpr": 869.0,
        "kftc_deal_bas_r": 869.63,
        "ten_dd_efee_r": 0,
        "ttb": 860.93,
        "tts": 878.32
    },
    {
        "bkpr": 1.0,
        "cur_nm": "한국 원",
        "cur_unit": "KRW",
        "deal_bas_r": 1.0,
        "kftc_bkpr": 1.0,
        "kftc_deal_bas_r": 1.0,
        "ten_dd_efee_r": 0,
        "ttb": 0.0,
        "tts": 0.0
    },
    {
        "bkpr": 4440.0,
        "cur_nm": "쿠웨이트 디나르",
        "cur_unit": "KWD",
        "deal_bas_r": 4440.93,
        "kftc_bkpr": 4440.0,
        "kftc_deal_bas_r": 4440.93,
        "ten_dd_efee_r": 0,
        "ttb": 4396.52,
        "tts": 4485.33
    },
    {
        "bkpr": 290.0,
        "cur_nm": "말레이지아 링기트",
        "cur_unit": "MYR",
        "deal_bas_r": 290.48,
        "kftc_bkpr": 290.0,
        "kftc_deal_bas_r": 290.48,
        "ten_dd_efee_r": 0,
        "ttb": 287.57,
        "tts": 293.38
    },
    {
        "bkpr": 127.0,
        "cur_nm": "노르웨이 크로네",
        "cur_unit": "NOK",
        "deal_bas_r": 127.29,
        "kftc_bkpr": 127.0,
        "kftc_deal_bas_r": 127.29,
        "ten_dd_efee_r": 0,
        "ttb": 126.01,
        "tts": 128.56
    },
    {
        "bkpr": 832.0,
        "cur_nm": "뉴질랜드 달러",
        "cur_unit": "NZD",
        "deal_bas_r": 832.1,
        "kftc_bkpr": 832.0,
        "kftc_deal_bas_r": 832.1,
        "ten_dd_efee_r": 0,
        "ttb": 823.77,
        "tts": 840.42
    },
    {
        "bkpr": 363.0,
        "cur_nm": "사우디 리얄",
        "cur_unit": "SAR",
        "deal_bas_r": 363.44,
        "kftc_bkpr": 363.0,
        "kftc_deal_bas_r": 363.44,
        "ten_dd_efee_r": 0,
        "ttb": 359.8,
        "tts": 367.07
    },
    {
        "bkpr": 126.0,
        "cur_nm": "스웨덴 크로나",
        "cur_unit": "SEK",
        "deal_bas_r": 126.94,
        "kftc_bkpr": 126.0,
        "kftc_deal_bas_r": 126.94,
        "ten_dd_efee_r": 0,
        "ttb": 125.67,
        "tts": 128.2
    },
    {
        "bkpr": 1009.0,
        "cur_nm": "싱가포르 달러",
        "cur_unit": "SGD",
        "deal_bas_r": 1009.48,
        "kftc_bkpr": 1009.0,
        "kftc_deal_bas_r": 1009.48,
        "ten_dd_efee_r": 0,
        "ttb": 999.38,
        "tts": 1019.57
    },
    {
        "bkpr": 37.0,
        "cur_nm": "태국 바트",
        "cur_unit": "THB",
        "deal_bas_r": 37.37,
        "kftc_bkpr": 37.0,
        "kftc_deal_bas_r": 37.37,
        "ten_dd_efee_r": 0,
        "ttb": 36.99,
        "tts": 37.74
    },
    {
        "bkpr": 1363.0,
        "cur_nm": "미국 달러",
        "cur_unit": "USD",
        "deal_bas_r": 1363.1,
        "kftc_bkpr": 1363.0,
        "kftc_deal_bas_r": 1363.1,
        "ten_dd_efee_r": 0,
        "ttb": 1349.46,
        "tts": 1376.73
    }
]})

@api_view(['GET'])
def save(request):
  if request.method == 'GET':
    params = {
      'auth': settings.FINANCE_API_KEY,
      'topFinGrpNo': '020000',
      'pageNo': '1'
    }
    
    for idx, category in enumerate(['deposit', 'saving']):
      API_URL = f'http://finlife.fss.or.kr/finlifeapi/{category}ProductsSearch.json'
      
      response = requests.get(
        url=API_URL,
        params=params
      ).json().get('result').get('baseList')
    
      for res in response:
        for month in ('1', '3', '6', '12', '24', '36'):
          product = Product(
            category=idx,
            dcls_month = res.get('dcls_month'),
            fin_co_no = res.get('fin_co_no'),
            kor_co_nm = res.get('kor_co_nm'),
            fin_prdt_cd = res.get('fin_prdt_cd'),
            fin_prdt_nm = res.get('fin_prdt_nm'),
            join_way = res.get('join_way'),
            spcl_cnd = res.get('spcl_cnd'),
            join_deny = res.get('join_deny'),
            join_member = res.get('join_member'),
            etc_note = res.get('etc_note'),
            save_trm = month,
            )
        
          ans = Product.objects.filter(
            category=idx,
            dcls_month = res.get('dcls_month'),
            fin_co_no = res.get('fin_co_no'),
            kor_co_nm = res.get('kor_co_nm'),
            fin_prdt_cd = res.get('fin_prdt_cd'),
            fin_prdt_nm = res.get('fin_prdt_nm'),
            join_way = res.get('join_way'),
            spcl_cnd = res.get('spcl_cnd'),
            join_deny = res.get('join_deny'),
            join_member = res.get('join_member'),
            etc_note = res.get('etc_note'),
            save_trm = month,
            )
          
          if not ans:
            product.save()
      
    for idx, category in enumerate(['deposit', 'saving']):
      API_URL = f'http://finlife.fss.or.kr/finlifeapi/{category}ProductsSearch.json'
      
      response = requests.get(
        url=API_URL,
        params=params
      ).json().get('result').get('optionList')
    
      for res in response:
        product = Product.objects.filter(
          category=idx,
          dcls_month = res.get('dcls_month'),
          fin_co_no = res.get('fin_co_no'),
          fin_prdt_cd = res.get('fin_prdt_cd'),
          save_trm = res.get('save_trm'),
        )[0]
        
        product.intr_rate_type = res.get('intr_rate_type')
        product.intr_rate_type_nm = res.get('intr_rate_type_nm')
        product.intr_rate = res.get('intr_rate')
        product.intr_rate2 = res.get('intr_rate2')
        
        if res.get('rsrv_type'):
          product.rsrv_type = res.get('rsrv_type')
          product.rsrv_type_nm = res.get('rsrv_type_nm')
        product.save()
    return Response(res, status=status.HTTP_200_OK)
  
@api_view(['GET'])
def get_product(request):
  if request.method == 'GET':
    products = Product.objects.all()
    serializers = ProductListSerializer(products, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@login_required
def subscribe(request):
  if request.method == 'POST':
    product_id = request.data['product']
    product = Product.objects.get(pk=product_id)
    subscribes = User_Product.objects.filter(user=request.user, product=product)
    if subscribes:
      subscribes.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    else:
      serializer = SubscribeSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, product=product)
        return Response(status=status.HTTP_200_OK)
  elif request.method == 'GET':
    product_id = request.GET.get('product')
    product = Product.objects.get(pk=product_id)
    subscribes = User_Product.objects.filter(user=request.user, product=product_id)
    serializer = SubscribeSerializer(subscribes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def subscribe_list(request):
  if request.method == 'GET':
    subscribes = User_Product.objects.filter(user=request.user)
    serializer = SubscribeSerializer(subscribes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
@api_view(['GET'])
def gpt(request):
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
          file_content = f.read()
        f.close()
    except UnicodeDecodeError as e:
        return Response({'error': f'Unicode decode error: {str(e)}'}, status=500)

    if request.method == 'GET':
      # prev_questions = [Question.objects.all().order_by('-created_at')[0].text] 
      prev_questions = [''] 
      query = request.GET.get('query')
      print(query) 
      messages = [{
          "role": "user",
          "content": file_content + '위의 상품들 중에 검색을 하고 싶어.'
          }]
      for question in prev_questions + [query]:
        messages.append({
          "role": "user",
          "content": question
        })
      messages.append({
        "role": "user",
        "content": "마크다운 양식 없이 출력하고, 간략하게 요약해줘."
        })
      
      client = OpenAI(api_key=settings.GPT_KEY)
      completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
        )
      Question.objects.create(text=query)
      return Response({'response': completion.choices[0].message.content})
