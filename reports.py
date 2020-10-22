from datetime import datetime
#dont import data go data to main then to reports (data => main <=> reports)
import main

def text_report(list_t, input_type):
    '''list_t = literal list  of items (phone, laptop, tablet) *** input_type = item to generate report for (phone, tablet, laptop) '''
    print('*****in reports****')

    #Timestamp
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y-%m-%d %H:%M")
    print(f"Timestamp {dt_string}")

    #Device
    print(f'Device: {input_type.capitalize()}')
    #Number
    print(f'Number: {len(list_t)}')
    #Average price
    total = 0 
    for i in list_t:
        i_split = i.split(',')
        total += float(i_split[6])
    average = total / len(list_t)
    print(f'Average price: ${average:.2f}')
        
    #Min price

    #Max price

    #median ram
    ram = 0 
    for i in list_t:
        i_split = i.split(',')
        ram += int(i_split[3])
    average_ram = ram / len(list_t)
    if average_ram <= 20:
        new_ram = 8
        print(f'Median RAM: {new_ram}')
    elif average_ram >20.0 and average_ram <48.0:
        new_ram = 32
        print(f'Median RAM: {new_ram} GB')
    elif average_ram > 20 and average_ram > 48:
        new_ram = 62
        print(f'Median RAM: {new_ram}')
    #os 
    master = ''
    for i in list_t:
        i_split = i.split(',')
        both = i_split[4:6]
        a = both.pop(0)
        b = both.pop(0)
        all_string = f' {a} {b},'
        master += all_string
    last_comma = master.rstrip(',')
    print(f'Operating System:{last_comma}')

def csv_report():
    pass


def json_report():
    now_date = date()
    print(now_date)
    print('{' '\n'
        f'      \"date_time\": {now_date}''\n'
        f'      \"device_type\": phone''\n'
        f'      \"number\": phone''\n'
        f'      \"average_price\": phone''\n'
        f'      \"min_price\": phone''\n'
        f'      \"max_price\": phone''\n'
        f'      \"median_price\": phone''\n'
        f'      \"operating_system\": phone''\n'
        '}')


