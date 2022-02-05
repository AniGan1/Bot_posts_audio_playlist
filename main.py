# -*- coding: utf-8 -*-
import readline
import time
import requests


message = """Самый сок """

audio_playlist ='audio_playlist438672703_45_e17ad2b1a0219460ae'


while True:
    with open("tokens.txt", 'r') as tokens:
        owner_token = tokens.readlines()
        for owner_token in owner_token:
            with open("groups.txt", 'r') as groups:
             group = groups.readlines()
             for group in group:
              post = requests.post('https://api.vk.com/method/wall.post?owner_id=-'+ str(group) + '&message=' + message + '&attachments=' + audio_playlist +'&fields=bdate&access_token=' + owner_token + '&v=5.131') 
              print("Пост опубликован ")
              time.sleep(7)
              post = requests.post('https://api.vk.com/method/wall.post?owner_id=-'+ str(group) + '&message=' + message + '&attachments=' + audio_playlist +'&fields=bdate&access_token=' + owner_token+ '&v=5.131') 
              print("Пост опубликован")
              time.sleep(7)
              post = requests.post('https://api.vk.com/method/wall.post?owner_id=-'+ str(group) + '&message=' + message + '&attachments=' + audio_playlist +'&fields=bdate&access_token=' + owner_token + '&v=5.131') 
              print("Пост опубликован")
              time.sleep(7)
    
