import re
def send_email(message, recipient, sender = 'university.help@gmail.com'):
    pattern_com = (r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9/-]+\.com\b')
    pattern_net = (r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9/-]+\.net\b')
    pattern_ru = (r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9/-]+\.ru\b')

    is_valid = recipient.find('@')
    is_valid_com = re.fullmatch(pattern_com, recipient)
    is_valid_net = re.fullmatch(pattern_net, recipient)
    is_valid_ru = re.fullmatch(pattern_ru, recipient)
    is_valid_s = sender.find('@')
    is_valid_com_s = re.fullmatch(pattern_com, sender)
    is_valid_net_s = re.fullmatch(pattern_net, sender)
    is_valid_ru_s = re.fullmatch(pattern_ru, sender)

    if is_valid < 0:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        return
    if is_valid_com is None and is_valid_net is None and is_valid_ru is None:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        return
    if is_valid_s < 0:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        return
    if is_valid_com_s is None and is_valid_net_s is None and is_valid_ru_s is None:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        return
    if sender == recipient:
        print('Невозможно отправить письмо самому себе')
        return
    if 'university.help@gmail.com' not in sender:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
        return
    if sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')





