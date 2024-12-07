from datetime import datetime


def main() -> None:
    """
    Печатные газеты использовали свой формат дат для каждого выпуска. Для каждой
    газеты из списка напишите формат указанной даты для перевода в объект datetime:
    The Moscow Times - Wednesday, October 2, 2002
    The Guardian - Friday, 11.10.13
    Daily News - Thursday, 18 August 1977
    Пример работы программы
    Программа должна выводить на экран объекты типа datetime, соответствующие датам
    в условии задачи
    """
    tmt: datetime = datetime.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y')
    tg: datetime = datetime.strptime('Friday, 11.10.13', '%A, %d.%m.%y')
    tdn: datetime = datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y')
    print(f'The Moscow Times - {tmt} ({type(tmt)})\nThe Guardian - {tg} ({type(tg)})\nDaily News - {tdn} ({type(tdn)})')  # noqa T201


if __name__ == '__main__':
    main()
