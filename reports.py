from datetime import datetime
import data


def date():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y-%m-%d %H:%M")
    print("Timestamp", dt_string)


def text_report(input_type):
    date()
    total = 0
    print('Device: ' + input_type.capitalize())
    if input_type == 'phone':
        phone_data = data.get_phone_info_list()
        phone_arr = []
        for i in phone_data:
            each = i
            each_arr = each.split(',')
            phone_arr.append(each_arr)
        print('Number: ' + str(len(phone_arr)))
        for j in phone_arr:

            price = j[6]
            total = total + float(price)
            average = total / len(phone_arr)

        text = f"{average:.2f}"
        formatted = float(text)
        print(f'Average Price: {formatted}')

        print(f'Minimum price:')
        print(f'Maximum price:')
        print(f'Median RAM: ')
        print(f'Operating system:')



def csv_report():
    pass


def json_report():
    pass

