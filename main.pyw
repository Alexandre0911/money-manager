from typing import Text
import PySimpleGUI as psg
import datetime



money_sign = ''
month = datetime.datetime.today().month

month_names = {
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'September',
    10 : 'October',
    11 : 'November',
    12 : 'December'
}



def main():
    global money_sign

    background = '#D8D8D8'

    psg.SetOptions(background_color = background,
        element_background_color = background,
        text_element_background_color = background,
        window_location = (640, 480),
        margins=(5,5),
        text_color = 'Black',
        input_text_color = 'Black',
        button_color = ('Black', 'gainsboro'))

    layout = [
        [psg.Text('This Money Manager Was Made By : Alexandre0911@github.com')],
        [psg.Text('Amount Of Money At The Start Of The Month'), psg.InputText()],
        [psg.Text('Select Currency  >>>'), psg.Button('Dollars'), psg.Text('-'), psg.Button('Euros')],
        [psg.Button('Do The Math!'), psg.Button('Cancel')]
    ]

    window = psg.Window('Money Manager v1.0', layout)



    while True:
        event, values = window.read()

        if event == psg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Dollars':
            money_sign = ' $'
            psg.PopupOK('Currency was set to Dollars', keep_on_top=True)
        elif event == 'Euros':
            money_sign = ' €'
            psg.PopupOK('Currency was set to Euros', keep_on_top=True)
        elif event == 'Do The Math!':
            if money_sign == '':
                psg.PopupOK('You need to choose a currency!')
            elif money_sign != '':
                my_number = float(values[0])
                psg.PopupOK(math(my_number, money_sign), keep_on_top=True)

    window.close()



def math(x, y):
    basic_necessities = x * 0.5
    free_time = x * 0.1
    financial_liberty = x * 0.1
    long_term_expenses = x * 0.1
    financial_education = x * 0.1
    donations = x * 0.1



    try:
        file = open('C:\\Users\\Public\\Desktop\\Money Management ({}).txt'.format(month_names[month]), mode='w+', encoding='utf-8')
        file.write('''Money For Basic Necessities >>> {:.2f}{}
Money For Free Time >>> {:.2f}{}
Money For Financial Liberty >>> {:.2f}{}
Money For Long-Term Expenses >>> {:.2f}{}
Money For Financial Education >>> {:.2f}{}
Money For Donations >>> {:.2f}{}'''.format(basic_necessities, y, free_time, y, financial_liberty, y, long_term_expenses, y, financial_education, y, donations, y))
    finally:
        file.close()



    a = 'Money For Basic Necessities >>> {:.2f}{}'.format(basic_necessities, y)
    b = 'Money For Free Time >>> {:.2f}{}'.format(free_time, y)
    c = 'Money For Financial Liberty >>> {:.2f}{}'.format(financial_liberty, y)
    d = 'Money For Long-Term Expenses >>> {:.2f}{}'.format(long_term_expenses, y)
    e = 'Money For Financial Education >>> {:.2f}{}'.format(financial_education, y)
    f = 'Money For Donations >>> {:.2f}{}'.format(donations, y)

    saved = 'Document Saved to Desktop as Money Management ({}).txt'.format(month_names[month])

    return '{}\n{}\n{}\n{}\n{}\n{}\n\n{}'.format(a, b, c, d, e, f, saved)



if __name__ == '__main__':
    main()