from apis import (apiTipificador, apiBackOffice)
apiConsultarCasosTipificador    = apiTipificador.apiConsultarCasosTipificador
apiAgregarCentroCaso            = apiTipificador.apiAgregarCentroCaso
apiBackofficeFilter             = apiBackOffice.apiBackofficeFilter

data = apiConsultarCasosTipificador()
print(len(data))
data = data[0:300]

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