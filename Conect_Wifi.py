def conecta(NomeDaRede,SenhaDaRede):
    print("Conectando com a rede WIFI - " + NomeDaRede)
    import network
    import time
    
    station = network.WLAN(network.STA_IF)
    time.sleep(0.5)
    station.active(True)
    station.connect(NomeDaRede,SenhaDaRede)
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station



