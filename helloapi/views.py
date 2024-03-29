# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
import requests, json
# Create your views here.
def navermap(request):
    return render(request, 'navermap.html')
    
def kakaopay(request):
    return render(request, 'kakaopay.html')
    
def ok(request):
    return render(request, 'ok.html')
    
def ready(request):
    url = 'https://kapi.kakao.com/v1/payment/ready'
    headers = {'Authorization': '###kakao api 인증 뭐시기 ###'}
    data = {
        'cid': 'TC0ONETIME',
        'partner_order_id': '123',
        'partner_user_id': '123',
        'item_name': '초코파이',
        'quantity': 1,
        'total_amount': 2200,
        'vat_amount': 200,
        'tax_free_amount': 0,
        'approval_url': 'https://api-jiyeon981225.c9users.io/success',
        'fail_url': 'https://api-jiyeon981225.c9users.io/fail',
        'cancel_url': 'https://api-jiyeon981225.c9users.io/cancel',
    } 
    response = requests.post(url=url, data=data, headers=headers)
    result = response.json()
    request.session['tid'] = result['tid']
    return redirect(result['next_redirect_pc_url'])

def success(request):
    url = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {'Authorization': '###kakao api 인증 뭐시기'}
    data = {
        'cid': 'TC0ONETIME',
        'tid': request.session['tid'],
        'partner_order_id': '123',
        'partner_user_id': '123',
        'pg_token': request.GET['pg_token']
    }
    response = requests.post(url=url, data=data, headers=headers)
    result = response.json()
    item_name = result['item_name']
    item_price = result['amount']['total']
    return render(request, 'ok.html', {'item_name': item_name, 'item_price': item_price})