import re

url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
pattern_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = pattern_url.match(url)

if not match:
    raise ValueError('A url não é válida!')

print('A url é válida!')

