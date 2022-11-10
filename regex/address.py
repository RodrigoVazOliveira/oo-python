import re

address = "Rua das mães, Casa, Jardim Patricia, Uberlândia, MG, 38364-947"
pattern = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
search = pattern.search(address)
if search:
    print(search.group())