#!/usr/bin/python3
#
#
import pyttsx3
import os
import time 
import threading
from time import sleep
from googlesearch import search
from selenium import webdriver






engine = pyttsx3.init()
voice_id ='spanish-latin-am'
engine.setProperty('voice',voice_id)
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-50)
string='bienvenido señor bernardo en que puedo ayudarle'
pyr='yo soy viernes la asistente de mydrugs creada por usted para servirle'
yu='comensemos guapo'
gg='no te entiendo guapo'
hub='viernes te amo'
hytur='gusto de verte mi bernardito hermoso'
tutu='no eres mi bernardo cerrare el programa'
gty='solo es una medida preventiva  de seguridad para que solo bernardo acceda al programa'
engine.say(string)
engine.say(pyr)
engine.say(yu)
engine.runAndWait()

print("antes de ingresar debes poner contraseña")
engine.say(gty)
engine.runAndWait()
hyut=input("clave aca guapo: ")
while hyut == hub:
	engine.say(hytur)
	engine.runAndWait()
	break

else:
	engine.say(tutu)
	engine.runAndWait()
	quit()



print("""                     ▄██████▄,     ▄▓████▓▄     ,▄██████▄    '
                    ████▀▀▀▀████µ ▄███▀▀▀▀████ ,████▀▀▀▀████   '
               .   ███▀      └██████▀      ╙██████Γ      ╙███   .
                  ▐███    ▄   └████▀        ╙████Γ   ┌    ███▌
              .   ███Γ   ╟█    ╙██`    ██    └██▌    █▌   └███
                 ]███    ███    ▀    ╓████▄    ▀    ███    ███µ  '
                 ███▌   ▐███▌       ▄██████▌       ▐███▌   ▐███
             '   ███    █████▌     ▓█████████     ]█████    ███   '
                ╫██▌   ▐█████Γ    ╙██████████▌    ╙█████▌   ╙██▌
            '   ███    █████¬      ╟█████████       █████    ███   '
               ▐██▌   j████    ╓    ████████    ╓    ████⌐   ╟██▌
           '   ███    ▓██▀    ▄█▌    ██████¬   ╒█▌    ╙███    ███   '
              ▐███    ██▀    ████─   ╙████▌    ████    ╙██    ╟██▌
          .   ███─   ╟█`    ██████    ╟███    ██████    └█▌    ███   .
             ]███    █    ╓████████    ██    ▓███████▄    █    ███▄  '
             ███▌   "    ▄█████████▌    ─   ▐█████████▄    \   ╘███
             ███        ▓███████████µ       ████████████        ███⌐  '
            ▓██▌       █████████████▀      ╙█████████████       ▐███
        '   ███      ,█████████▀▀─            └╙▀█████████µ      ███   '
           ╟██▌     ╓██████▀╙       ,▄████▄,       ╙▀██████▄     ╟██▌
       '   ███     ▄██▀▀─       ▄▄████████████▄▄       └╙▀██▌     ███   .
          ▐███    ^╙       ,▄█████████████████████▓▄,       ╙▀    ╟██▌  '
       \   ███µ        ▄▄██████████████████████████████▄▄         ███   '
       .   ▐████▄▄▄▄███████████████████████████████████████▓▄╓╓▄▓███Γ
          ]███▀█████▀▀█▀████▀█▀▀▀▀████▀▀▀█████▀███▀████▀▀█████▀▀█████   '
          ▐██▌  ╟██▀  █  ╟█  █  ▄▄  ╙▌  ▄▄  █  ██▌  █  ▄▄  █  ▄▄  ███b  '
          ▐██▌   ╟▀   ██    ██  ██▌ j▌  ▀▀  █  ██▌  ▌  █▀▀▀█▄  ╙▀▀███¬  '
          ▐██▌ jµ  ▄  ███  ███  ██▌ j▌  ▓  ██  ██▌  ▌  █▄  █╙╙██  ╟██▌
          ▐██▌ j████  ███  ███     ,█▌  ██  █▌    ,▄█▄    ▄█▄    ╓███Γ  .
       .   █████████████████████████████████████████████████████████└
        \    └└└─  └└└└ └└└└ └└└└└└─ └└└└└└└└ └╙╙╙└  ─╙╙╙╙─  └╙╙╙─
          '  .   - .  . .         .    . .  ..    . -.     -.     - '""")
print("""



	hecho por _b__kernel



	1.sqlbolivia      2.pagina de mydrugs      3.bot instagram my drugs   4.tu busqueda   5.salir   6.busqueda""")



jota='bolivia.php?id='
opcion =int(input("opcion :    "))
vida=0
yr='excelente opcion jefe'
np='nos pondremos traviesos hoy jefe?'
hu='estas son las paginas web con error sql en bolivia guapo'
lu='entraremos a instagram tenga cuidado jefe '
bd='alguna busqueda para hoy bebe?'
camisanegra='bebe escribe lo que quieres buscar'

xexe='la busqueda a terminado'

def find_click(path):
	browser= webdriver.Chrome(executable_path="./chromedriver")
	element=browser.find_element_by_xpath(path)
	element.click()
	return element
def monalisa():
	engine.say(hu)
	engine.runAndWait()
	print("pruebita nomas es ")
	time.sleep(3)
	for pichi in search(jota):
		print(pichi)
		time.sleep(3)
def prueba():
	engine.say(bd)
	engine.runAndWait()
	time.sleep(3)
	browser=webdriver.Chrome(executable_path="./chromedriver")
	engine.say(camisanegra)
	engine.runAndWait()
	time.sleep(3)
	browser.get("https://www.google.es/")
	time.sleep(30000)


def variable():
	engine.say(yr)
	engine.runAndWait()
	browser3= webdriver.Chrome(executable_path="./chromedriver")
	browser3.get("https://kernelboy34.github.io/_mydrugss/index.html")
	time.sleep(33000)


def puta():
	engine.say(lu)
	engine.runAndWait()
	contrasena=(input("usuario:  "))
	usuario=(input("contrasena:  "))
	browser= webdriver.Chrome(executable_path="./chromedriver")
	browser.get("https://instagram.com")
	time.sleep(3)
	user_input=browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
	user_input.send_keys(contrasena)
	time.sleep(1)
	pass_input= browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
	pass_input.send_keys(usuario)
	time.sleep(1)
	iniciar_session_button= find_click('//*[@id="loginForm"]/div/div[3]/button')
	time.sleep(4)
	browser.get('https://www.instagram.com/direct/inbox/')
	time.sleep(3)
	no_chat=find_click('/html/body/div[4]/div/div/div/div[3]/button[2]')
	time.sleep(2)
	open_chat=find_click('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]/a/div')
	time.sleep(2)
	text_field =browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
	return text_field
	chat= puta()
	enviar_mensaje_button=browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
	chat.send_keys("te adoroooo")
	companero=find_click('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]')
	chat.send_keys("no olvides que te quiero")
	companero2=find_click('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]')
	chat.send_keys("bebe <3")
	companero3=find_click('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]')
	enviar_mensaje_button.click()
	time.sleep(300000)
def putita():
	engine.say(np)
	engine.runAndWait()
	dork=input("que quieres buscar?:  ")
	for i in search(dork):
		print(i)
di='adios bebe te espero la siguiente cuidate'



while True:
	if opcion == 1:
		monalisa()
	if opcion == 2:
		variable()
	if opcion == 3:
		puta()
	if opcion == 4:
		putita()
	if opcion == 5:
		engine.say(di)
		engine.runAndWait()
		print("adios<3")
		quit()
	if opcion == 6:
		prueba()

	break


else :
	print("nose choco")
	engine.say(gg)
	engine.runAndWait()