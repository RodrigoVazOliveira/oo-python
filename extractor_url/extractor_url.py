import re


class ExtractorURL:
    def __init__(self, url):
        self.__url = self.sanitization_url(url)
        self.__validate__url()

    def sanitization_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def __validate__url(self):
        if not self.__url:
            raise ValueError('A url está vazia!')

        pattern_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = pattern_url.match(self.__url)
        if not match:
            raise ValueError('A url não é válida!')

    def get_url_base(self):
        index_mark_question = self.__url.find('?')
        url_base = self.__url[:index_mark_question]

        return url_base

    def get_url_parameters(self):
        index_mark_question = self.__url.find('?')
        url_parameters = self.__url[index_mark_question + 1:]

        return url_parameters

    def validate_index_sepator(self, index_sepator, parameters, index_value):
        if index_sepator == -1:
            return parameters[index_value:]
        return parameters[index_value:index_sepator]

    def get_value_parameter(self, parameter):
        parameters = self.get_url_parameters()
        index_parameter = parameters.find(parameter)
        index_value = index_parameter + len(parameter) + 1
        index_separetor = parameters.find('&', index_value)

        return self.validate_index_sepator(index_separetor, parameters, index_value)

    def __len__(self):
        return len(self.__url)

    def __str__(self):
        return self.__url
