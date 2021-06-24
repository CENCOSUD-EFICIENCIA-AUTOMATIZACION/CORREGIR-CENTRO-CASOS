import requests
import json

def apiConsultarCasosTipificador():
    url = "https://cl-jproducto-back.ecomm.cencosud.com/backend/v1/requerimiento/query"
    payload = {
        "query": """
            SELECT * 
            FROM requerimientos
            WHERE (centro IS NULL OR centro = 'undefined') AND
            motivo <> 'Consulta'
        """
    }
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response    = requests.request("POST", url, headers=headers, data=payload)
    data        = json.loads(response.text)
    return data['payload']

def apiAgregarCentroCaso(id,centro):
    url = "https://cl-jproducto-back.ecomm.cencosud.com/backend/v1/requerimiento/query"
    payload = {
        "query": f"""
                UPDATE requerimientos
                SET centro = '{centro}'
                WHERE id = '{id}';
        """
    }
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response    = requests.request("POST", url, headers=headers, data=payload)
    data        = json.loads(response.text)
    return data['payload']