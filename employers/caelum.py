from employer import Employer


class Caelum(Employer):
    def show_tasks(self):
        print('Fez muita coisa...')

    def search_course_of_month(self, month=None):
        print(f'Mostrando cursos - {month}' if month else 'Mostrando cursos desse mês')
