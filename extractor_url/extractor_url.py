from validate_url import ValidateURL

url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

validate_url = ValidateURL(url)

url_base = validate_url.get_url_base()
url_parameters = validate_url.get_url_parameters()
coin_origin_value = validate_url.get_value_parameter('moedaOrigem')
coin_destination_value = validate_url.get_value_parameter('moedaDestino')
quantity = validate_url.get_value_parameter('quantidade')

print("url base: {}, parametros: {}".format(url_base, url_parameters))
print("valorOrigin: {}, valorDestino: {}, quantidade: {}".format(coin_origin_value, coin_destination_value, quantity))


