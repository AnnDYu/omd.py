def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Утка взяла зонт и под дождем дошла до бара. '
        'Бармен предложил утке покрасить потрескавшуюся стену в баре в обмен на пинту пива. Покрасить?'
    )
    option = ''
    options_bar = {'да': True, 'нет': False}
    while option not in options_bar:
        print('Выберите: {}/{}'.format(*options_bar))
        option = input()

    if options_bar[option]:
        print('Утка покрасила стену и насладилась бокалом пенного вознаграждения от бармена! :)')
    else:
        print('Утка отказалась и во время распития напитков ей насыпались в кружку '
              'кусочки облупившейся краски c испорченной стены.'
              ' Утка очень расстроилась :( '
              )


def step2_no_umbrella():
    print('В середине пути пошел дождь. Утке пришлось вернуться домой и отложить поход в бар :(')


if __name__ == '__main__':
    step1()
