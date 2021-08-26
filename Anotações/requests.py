import pip._vendor.requests as requests
pedido = requests.get("https://www.google.com")
print(pedido.status_code)

pedido.headers #mostra informações da pagina
pedido.headers["Date"] #mostra informações especificas da pagina
pedido.text #todo codigo html da pagina frontal