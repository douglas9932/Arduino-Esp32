from Conect_Wifi import conecta
import machine
import dht
import time
from umqtt.simple import MQTTClient
import urequests

NomeDaRede = ""
SenhaDaRede= ""

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

contadorIf = contadorElse = 0

print("Conectando ao WIFI!")
station = conecta(NomeDaRede,SenhaDaRede)

if not station.isconnected():
    print("Erro de conexão com a rede WIFI! Tente novamente.")
    print()
else:
    print("Conexão com a rede WIFI {} realizada com sucesso!".format(NomeDaRede))
    print()
    #station.disconnect()
    
time.sleep(0.2)

while True:
    d.measure()
    
    print("A temperatura atual é: {}°C.".format(d.temperature()))
    print("A umidade relativa do ar atual é: {}%.".format(d.humidity()))
    
    time.sleep(1)
    if d.temperature() > 31 or d.humidity() > 75:
        d.temperature()
        d.humidity()
        time.sleep(1)
        
        atualizarSite = ("https://api.thingspeak.com/update?api_key=&field1={}&field2={}".format(d.temperature(),d.humidity()))              
     
        print("Acessando o ThingSpeak...")
        response = urequests.get(atualizarSite)
        print("Dados enviados com sucesso!")
        print(response.text)
        
        contadorIf += 1
        r.value(1)
        print("Relé ligado.")
        print()
        print("A temperatura atual é: {}°C.".format(d.temperature()))
        print("A umidade relativa do ar atual é: {}%.".format(d.humidity()))
        print()
        print("Número de impressões no console: {}.".format(contadorIf))
        print()
        time.sleep(2)
        contadorElse = 0
    else:
        contadorElse += 1
        r.value(0)
        print("Relé desligado.")
        print()
        print("Número de impressões no console: {}.".format(contadorElse))
        print()
        time.sleep(2)
        contadorIf = 0

