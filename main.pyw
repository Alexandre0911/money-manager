from github import Github
import PySimpleGUI as psg
import datetime



github = Github("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")
repo = "Alexandre0911/money-manager"
get_repo = github.get_repo(repo).updated_at


null = ''
spaces = ' '
update = ' {}/{}/{}'.format(get_repo.month, get_repo.day, get_repo.year)
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
        [psg.Text('Made By : Alexandre0911@github.com'), psg.Text('{}Last Update Released  : {}'.format(spaces*42, update))],
        [psg.Text('Amount Of Money At The Start Of The Month', size=(33)), psg.InputText(size=(42)), psg.Text('€ / $')],
        [psg.Text('Basic Necessities Money Percentage', size=(33)), psg.InputText(size=(42)), psg.Text('%')],
        [psg.Text('Free Time Money Percentage ', size=(33)), psg.InputText(size=(42)), psg.Text('%')],
        [psg.Text('Financial Liberty Money Percentage ', size=(33)), psg.InputText(size=(42)), psg.Text('%')],
        [psg.Text('Long-Term Expenses Money Percentage', size=(33)), psg.InputText(size=(42)), psg.Text('%')],
        [psg.Text('Financial Instruction Money Percentage', size=(33)), psg.InputText(size=(42)), psg.Text('%')],
        [psg.Text('Donations Money Percentage', size=(33)), psg.InputText(size=(42)), psg.Text('%')],
        [psg.Text('Investments Money Percentage', size=(33)), psg.InputText(size=(42)), psg.Text('%')],
        [psg.Text('Select Currency  >>>'), psg.Button('Dollars'), psg.Text('-'), psg.Button('Euros')],
        [psg.Button('Do The Math!'), psg.Text(' '*113), psg.Button('Cancel')]
    ]

    window = psg.Window('Money Manager v1.1', layout)



    while True:
        event, values = window.read(timeout=0)

        if event == psg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Dollars':

            money_sign = ' $'
            psg.PopupOK(' Currency was set to Dollars.', keep_on_top=True)

        elif event == 'Euros':

            money_sign = ' €'
            psg.PopupOK(' Currency was set to Euros.', keep_on_top=True)

        elif event == 'Do The Math!':

            if '' in values:
                psg.PopupOK(' Some box(es) need to be filled!')

                if money_sign == '':
                    psg.PopupOK(' You need to choose a currency!')

                elif money_sign != '':

                    print(values)
                    total_percentage = float(values[1]) + float(values[2]) + float(values[3]) + float(values[4]) + float(values[5]) + float(values[6]) + float(values[7])

                    if total_percentage == 100.0:

                            my_number = float(values[0])
                            psg.PopupOK(math(my_number, money_sign, float(values[1]), float(values[2]), float(values[3]), float(values[4]), float(values[5]), float(values[6]), float(values[7])), keep_on_top=True)

                    else:

                        psg.PopupOK('The percentages need to add up to 100.0 and they are adding up to {}!'.format(total_percentage))

                    
    window.close()



def math(x, y, bn, ft, fl, lte, fe, d, i):
    basic_necessities = x * (bn/100)
    free_time = x * (ft/100)
    financial_liberty = x * (fl/100)
    long_term_expenses = x * (lte/100)
    financial_instruction = x * (fe/100)
    donations = x * (d/100)
    investments = x * (i/100)



    try:
        file = open('C:\\Users\\Public\\Desktop\\Money Management ({}).txt'.format(month_names[month]), mode='w+', encoding='utf-8')
        file.write('''Money For Basic Necessities ({}%) >>> {:.2f}{}
Money For Free Time ({}%) >>> {:.2f}{}
Money For Financial Liberty ({}%) >>> {:.2f}{}
Money For Long-Term Expenses ({}%) >>> {:.2f}{}
Money For Financial Education ({}%) >>> {:.2f}{}
Money For Donations ({}%) >>> {:.2f}{}
Money For Investments ({}%) >>> {:.2f}{}'''.format(bn, basic_necessities, y, ft, free_time, y, fl, financial_liberty, y, lte, long_term_expenses, y, fe, financial_instruction, y, d, donations, y, i, investments, y))
    finally:
        file.close()



    a = 'Money For Basic Necessities >>> {:.2f}{}'.format(basic_necessities, y)
    b = 'Money For Free Time >>> {:.2f}{}'.format(free_time, y)
    c = 'Money For Financial Liberty >>> {:.2f}{}'.format(financial_liberty, y)
    d = 'Money For Long-Term Expenses >>> {:.2f}{}'.format(long_term_expenses, y)
    e = 'Money For Financial Education >>> {:.2f}{}'.format(financial_instruction, y)
    f = 'Money For Donations >>> {:.2f}{}'.format(donations, y)
    g = 'Money For Investments >>> {:.2f}{}'.format(investments, y)

    saved = 'Document Saved to Desktop as Money Management ({}).txt'.format(month_names[month])

    return '{}\n{}\n{}\n{}\n{}\n{}\n{}\n\n{}'.format(a, b, c, d, e, f, g, saved)



if __name__ == '__main__':
    main()