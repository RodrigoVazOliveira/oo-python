from extractor_url import ExtractorURL

url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

extractor_url = ExtractorURL(url)
extractor_url_two = ExtractorURL(url)

url_base = extractor_url.get_url_base()
url_parameters = extractor_url.get_url_parameters()
coin_origin_value = extractor_url.get_value_parameter('moedaOrigem')
coin_destination_value = extractor_url.get_value_parameter('moedaDestino')
quantity = extractor_url.get_value_parameter('quantidade')

print("url base: {}, parametros: {}".format(url_base, url_parameters))
print("valorOrigin: {}, valorDestino: {}, quantidade: {}".format(coin_origin_value, coin_destination_value, quantity))


print(f'A quantidade de caracteres da URL é de {len(extractor_url)}')
print(extractor_url == extractor_url_two)
