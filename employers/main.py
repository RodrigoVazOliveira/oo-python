from junior import Junior
from full import Full

if __name__ == '__main__':
    jonas = Junior("Jonas")
    jonas.search_asks_without_response()
    print(jonas)

    john = Full("John")
    john.search_asks_without_response()
    john.search_course_of_month(1)
    john.show_tasks()

    print(john)