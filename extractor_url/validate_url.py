class ValidateURL:
    def __init__(self, url):
        self.__url = self.__sanitization_url(url)
        self.__validate__url()

    def __sanitization_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def __validate__url(self):
        if not self.__url:
            raise ValueError('A url está vazia!')

    def get_url_base(self):
        index_mark_question = self.__url.find('?')
        url_base = self.__url[:index_mark_question]

        return url_base

    def get_url_parameters(self):
        index_mark_question = self.__url.find('?')
        url_parameters = self.__url[index_mark_question + 1:]

        return url_parameters

    def get_value_parameter(self, parameter):
        parameters = self.get_url_parameters()
        index_parameter = parameters.find(parameter)
        index_value = index_parameter + len(parameter) + 1
        index_separetor = parameters.find('&', index_value)

        return self.__validate_index_sepator(index_separetor, parameters, index_value)

    def __validate_index_sepator(self, index_sepator, parameters, index_value):
        if index_sepator == -1:
            return parameters[index_value:]
        return parameters[index_value:index_sepator]