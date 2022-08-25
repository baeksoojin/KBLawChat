from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time
import json
import tensorflow_datasets as tfds
import numpy as np
import re
import pandas as pd

import tensorflow as tf
from tensorflow import keras

from Chatbot.models import Message
import pymysql

def home(request):
    context = {}

    return render(request, "chathome.html", context)


@csrf_exempt
def chatanswer(request):
    context = {}

    questext = request.GET['questext']

    import pickle

    import colorama
    colorama.init()
    from colorama import Fore, Style, Back

     # load tokenizer object
    with open('static/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    START_TOKEN,END_TOKEN=[tokenizer.vocab_size],[tokenizer.vocab_size+1]
    VOCAB_SIZE=tokenizer.vocab_size+2
    MAX_LENGTH=60
   
    data = pd.read_csv('/Users/baeksujin/Desktop/lawchatbot/KBLawChat/project/Chatbot/lawdata.csv',encoding='utf-8') 

    
    def get_data(curs):
        answer_data = "select answer from message where id=(select MAX(id) from message)"
        curs.execute(answer_data)
        answer_data = curs.fetchall()
        
        if len(answer_data)==0:
            return False
        else:
            return answer_data

    def chat(questext):
        message = Message
        message(question = questext, checked=0).save()
        print("저장완료")
        return True

        # answer뽑아내기
    def get_answer():
        last = Message.objects.last()
        print(last.answer)
        return last.answer

    if chat(questext):
        time.sleep(5)
        anstext = get_answer()
        context['answer'] = anstext
        context['flag'] = '0'
    else:
        anstext = "죄송해요. 법률자문이 어렵습니다"
        context['answer'] = anstext
        context['flag'] = '0'
    
    # print(anstext)

    

    return JsonResponse(context, content_type="application/json")

