from time import sleep
from apis import (apiTipificador, apiBackOffice)
import sys
import os
apiConsultarCasosTipificador    = apiTipificador.apiConsultarCasosTipificador
apiAgregarCentroCaso            = apiTipificador.apiAgregarCentroCaso
apiBackofficeFilter             = apiBackOffice.apiBackofficeFilter

try:
    data = apiConsultarCasosTipificador()
    print(len(data))
    pedidos = []
    for caso in data:
        if caso['order_vtex'] != None:
            pedidos.append(caso['order_vtex'])
        elif 'pedido' in caso['pedido']:
            pedidos.append(caso['pedido']['pedido'])
    pedidos = apiBackofficeFilter(pedidos)

    contador = 0
    for caso in data:
        print(f"{contador}/{len(data)}")
        if caso['order_vtex'] in pedidos:
            centro = pedidos[caso['order_vtex']]
            apiAgregarCentroCaso(caso['id'],centro)
        elif 'pedido' in caso['pedido']:
            if caso['pedido']['pedido'] in pedidos:
                centro = pedidos[caso['pedido']['pedido']]
                apiAgregarCentroCaso(caso['id'],centro)
        contador += 1
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    print(e)
    print('No hay casos')
    sleep(10)