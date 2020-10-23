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
    print(f"Timestamp: {dt_string}")

    #Device
    print(f'Device: {input_type.capitalize()}')
    #Number
    print(f'Number: {len(list_t)}')
    #Average price
    total = 0 
    for h in list_t:
        h_split = h.split(',')
        total += float(h_split[6])
    average = total / len(list_t)
    print(f'Average Price: ${average:.2f}')
        
    #Min price
    prices = []
    for i in list_t:
        i_split = i.split(',')
        price = i_split[6]
        prices.append(price)
    print(f'Minimum Price: ${min(prices)}')


    #Max price
    print(f'Maximum Price: ${max(prices)}')

    #median ram
    ram = 0 
    for j in list_t:
        j_split = j.split(',')
        ram += int(j_split[3])
    average_ram = ram / len(list_t)
    if average_ram <= 20:
        new_ram = 8
        print(f'Median RAM: {new_ram}')
    elif average_ram >20.0 and average_ram <48.0:
        new_ram = 32
        print(f'Median RAM: {new_ram} GB')
    elif average_ram > 20 and average_ram > 48:
        new_ram = 64
        print(f'Median RAM: {new_ram}')
    #os 
    master = ''
    for k in list_t:
        k_split = k.split(',')
        both = k_split[4:6]
        a = both.pop(0)
        b = both.pop(0)
        all_string = f' {a} {b},'
        master += all_string
    last_comma = master.rstrip(',')
    print(f'Operating System:{last_comma}')

def csv_report(list_t, input_type):
    '''list_t = literal list  of items (phone, laptop, tablet) *** input_type = item to generate report for (phone, tablet, laptop) '''
    print('*****in reports****')
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y-%m-%d %H:%M")

    #average
    total = 0 
    for i in list_t:
        i_split = i.split(',')
        total += float(i_split[6])
    average = total / len(list_t)

    #Min / Max 



    #RAM
    ram = 0 
    for j in list_t:
        j_split = j.split(',')
        ram += int(j_split[3])
    average_ram = ram / len(list_t)
    if average_ram <= 20:
        new_ram = 8.0
    elif average_ram >20.0 and average_ram <48.0:
        new_ram = 32.0
    elif average_ram > 20 and average_ram > 48:
        new_ram = 64.0
    #os 
    str_csv = ''
    for k in list_t:
        k_split = k.split(',')
        both = k_split[4:6]
        a = both.pop(0)
        b = both.pop(0)
        all_string = f'{a} {b}/'
        str_csv += all_string
    master_csv = str_csv.rstrip('/')

    #csv 
    print(f'{dt_string},{input_type.capitalize()},{len(list_t)},Average{average:.2f},min, max,{new_ram},{master_csv}')

def json_report(list_t, input_type):
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y-%m-%d %H:%M")

    #Average price
    total = 0 
    for h in list_t:
        h_split = h.split(',')
        total += float(h_split[6])
    average = total / len(list_t)
    print(f'Average Price: $')

    #RAM
    ram = 0 
    for j in list_t:
        j_split = j.split(',')
        ram += int(j_split[3])
    average_ram = ram / len(list_t)
    if average_ram <= 20:
        new_ram = 8.0
    elif average_ram >20.0 and average_ram <48.0:
        new_ram = 32.0
    elif average_ram > 20 and average_ram > 48:
        new_ram = 64.0

    #os 
    str_json = ''
    for k in list_t:
        k_split = k.split(',')
        both = k_split[4:6]
        a = both.pop(0)
        b = both.pop(0)
        all_string = f'{a} {b},'
        str_json += all_string
    master_json = str_json.rstrip(',')

    print('{' '\n'
        f'      \"date_time\": "{dt_string}",''\n'
        f'      \"device_type\": "{input_type.capitalize()}",''\n'
        f'      \"number\": {len(list_t)},''\n'
        f'      \"average_price\": {average:.2f},''\n'
        f'      \"min_price\": phone,''\n'
        f'      \"max_price\": phone,''\n'
        f'      \"median_ram\": {new_ram},''\n'
        f'      \"operating_system\": "{master_json}"''\n'
        '}')


