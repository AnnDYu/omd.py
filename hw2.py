def csv_to_list(csv_file: str) -> list:
    with open(csv_file, 'r', encoding='utf8') as file:
        lines = file.readlines()
        head = lines[0].split(";")
        lines.pop(0)
        data = []
        for line in range(len(lines)):
            info = lines[line].split(";")
            data_dict = dict(zip(head, info))
            data.append(data_dict)
            line = line + 1
    return data


def question(data: list):
    print(f'Возможности: 1) Показать иерархию команд. 2) Вывести сводный отчёт по департаментам. '
          f'3) Сохранить сводный отчёт в csv-файл.'
          )
    options = {'1': hierarchy, '2': display_report, '3': save_to_csv}
    option = ''
    while option not in options:
        print('Введите номер команды'.format(*options))
        option = input()
    return options[option](data)


def hierarchy(data: list) -> dict:
    depart = []
    for row in data:
        depart.append(row['Департамент'])
    depart = set(depart)
    dep_kom = {x: [] for x in depart}
    for row in data:
        if row['Отдел'] not in dep_kom[row['Департамент']]:
            dep_kom[row['Департамент']].append(row['Отдел'])
    print(dep_kom)


def display_report(data: list) -> list:
    depart = []
    for row in data:
        depart.append(row['Департамент'])
    depart = set(depart)

    worker: dict = {i: 0 for i in depart}
    min: dict = {i: 9999999999 for i in depart}
    max: dict = {i: -1 for i in depart}
    sum: dict = {i: 0 for i in depart}
    avg: dict = {i: 0 for i in depart}

    for j in data:
        worker[j['Департамент']] = worker[j['Департамент']] + 1
        sum[j['Департамент']] = sum[j['Департамент']] + float(j['Оклад\n'])
        if min[j['Департамент']] > float(j['Оклад\n']):
            min[j['Департамент']] = float(j['Оклад\n'])
        if max[j['Департамент']] < float(j['Оклад\n']):
            max[j['Департамент']] = float(j['Оклад\n'])

    avg = {i: int(sum[i] / worker[i]) for i in depart}

    final: list[list[Union[str, Any]]] = [[i, worker[i], max[i], min[i], avg[i]] for i in depart]
    print(final)
    return final


def save_to_csv(data: list):
    final = display_report(data)
    head = ['Департамент', 'Кол-во работников', 'Макс зп', 'Мин зп', 'Средняя зп']
    final = [head] + final
    import numpy as np
    np.savetxt('results.csv', [p for p in final], delimiter=',', fmt='%s')


if __name__ == '__main__':
    csv_file = input()  # Corp_Summary.csv
    data = csv_to_list(csv_file)
    question(data)