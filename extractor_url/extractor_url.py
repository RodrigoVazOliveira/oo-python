url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = url.strip() # or url = url.replace(" ", "")  or url.lstrip() or url.rstrip()

if url == "" or url is None:
    raise ValueError('A url está vazia!')

index_mark_question = url.find('?')
url_base = url[:index_mark_question]
url_parameters = url[index_mark_question+1:]

coin_origin = 'moedaOrigem'
index_coin_origin_parameter = url_parameters.find(coin_origin)
index_value_coin_origin = index_coin_origin_parameter + len(coin_origin) + 1
coin_origin_value = url_parameters[index_value_coin_origin:index_value_coin_origin+5]

coin_destine = 'moedaDestino'
index_coin_destination_parameter = url_parameters.find(coin_destine)
index_value_coin_destination = index_coin_destination_parameter + len(coin_destine) + 1
coin_destination_value = url_parameters[index_value_coin_destination:index_value_coin_destination+5]

print("url base: {}, parametros: {}".format(url_base, url_parameters))
print("valorOrigin: {}, valorDestino: {}".format(coin_origin_value, coin_destination_value))


