import http.client
import json

def apiBackofficePicking(pedidos):
    conn    = http.client.HTTPSConnection("api.smdigital.cl", 8443)
    payload = {
        "size": len(pedidos),
        "page": 1,
        "filters": {
            "idOrder": pedidos    
        },
        "sort": [{"updatedAt": {"order": "desc"}}]
    }
    payload = json.dumps(payload)
    headers = {
        'X-RateLimit-Limit-day':    '36000',
        'x-api-key':                'VjD9jdcIaOO95nGwAgaHNRQyEU0z6aG5',
        'Content-Type':             'application/json'
    }
    conn.request("POST", "/v0/picking/picking/search", payload, headers)
    res     = conn.getresponse()
    data    = res.read()
    print(data)
    data    = json.loads(data.decode("utf-8"))
    return data['payload']

def apiBackofficeFilter(pedidos):
    import requests
    url     = "https://api.smdigital.cl:8443/v0/picking/orders/findOrdersByFilter"
    payload = {
        "size": 1000,
        "page": 1,
        "filters": {
            "id": pedidos
        },
        "sort": [{
            "creationDate": {
                "order": "desc"
            }
        }]
    }
    payload = json.dumps(payload)
    headers = {
        'X-RateLimit-Limit-day': '36000',
        'x-api-key': 'VjD9jdcIaOO95nGwAgaHNRQyEU0z6aG5',
        'Content-Type': 'application/json'
    }

    response    = requests.request("POST", url, headers=headers, data=payload)
    data        = response.text
    data        = json.loads(data)
    pedidos     = {}
    for pedido in data['payload']:
        pedidos[pedido['id']] = pedido['detail']['idStore']
    return pedidos