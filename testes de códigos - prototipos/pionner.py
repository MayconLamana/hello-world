#Código funcionando...
import copy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as gui

a = int (input (print("""Olá seja bem vindo ao programa!! \n
        Esse programa tem como objetivo, abrir o site JW.ORG e procurar automaticamente o assunto
        que desejar, entre eles pode ser:
        1 - Assunto em Destaque
        2 - 1º Artigo na seção 'Em Destaque' 
        3 - 2º Artigo na seção 'Em Destaque'
        4 - 3º Artigo na seção 'Em Destaque'
        5 - Outras opção de artigos na seção 'Em Destaque'-> Inoperante..""")))



nav = webdriver.Chrome()
nav.get("https://jw.org")
time.sleep(3)
nav.maximize_window()
time.sleep(10)

def assuntoEmDestaque():
        assunto = nav.find_element_by_xpath('//*[@id="regionMain"]/div/div/div[2]/div[4]/div/h3/a').text
        nav.find_element_by_xpath('//*[@id="regionMain"]/div/div/div[2]/div[4]/div/h3').click()
        #nav.find_element_by_xpath('//*[@id="primaryNavRegion"]/nav/ul/li[2]/a/span[2]').click()
        time.sleep(10)
        #nav.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div/div[2]/div/div[5]/div[1]/button/span/span[1]').click()
        #time.sleep(3)
        link = nav.current_url
        time.sleep(2)
        #gui.alert(f'o link desse site é: {link}, o link já foi copiado.')
        time.sleep(5)
        a = gui.alert(f'O Assunto é: {assunto} e o link é: {link}')
        time.sleep(10)
        nav.quit()
        print(a)


        #nav.find_elements_by_xpath('//*[@id="p2"]').text
        #verificador0 = nav.find_element_by_id('//*[@id="p1"]')
        #verificador1 = nav.find_element_by_id('//*[@id="p1"]/strong')
        #if (destaque1 == verificador0):
        #        destaque1 = nav.find_element_by_xpath('//*[@id="p1"]').text
        #        gui.alert(f' O destaque é {destaque1} \n ')
        #        nav.quit()
        #        time.sleep(2)
        #        print('{} '.format(destaque1))

      #  elif(destaque1 == verificador1):  
      #          destaque1 = nav.find_element_by_xpath('//*[@id="p1"]/strong').text
      #          gui.alert(f' O destaque é {destaque1} \n ')
      #          nav.quit()
      #          time.sleep(2)
      #          print('{} '.format(destaque1))      


        #if (assunto == '//*[@id="p2}'):         
        #        assunto = nav.find_element_by_xpath('//*[@id="p2"]').text
        #        if (destaque == nav.find_element_by_xpath('//*[@id="p1"]/strong')):
        #                destaque = nav.find_element_by_xpath('//*[@id="p1"]').text
        #        elif(destaque == nav.find_element_by_xpath('//*[@id="p1"]')):
        #                destaque = nav.find_element_by_xpath('//*[@id="p1"]').text    
        #        time.sleep(2)
        #        gui.alert(f' O destaque é {destaque} \n e o assunto é {assunto} ')
        #        nav.quit()
        #        time.sleep(2)
         #       print('{} \n {}'.format(destaque, assunto))

        

def primeiroAssuntoDestaque():
        print('')

def segundoAssuntoDestaque():
       print('')

def terceiroAssuntoDestaque():
       print('')

def outrosArtigos():
       print('')

if (a == 1): 
        assuntoEmDestaque()

elif(a == 2):
        print('')
       
        