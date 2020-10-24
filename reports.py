from datetime import datetime
#dont import data go data to main then to reports (data => main <=> reports)
import main

def text_report(list_t, input_type):
    '''list_t = literal list  of items (phone, laptop, tablet) *** input_type = item to generate report for (phone, tablet, laptop) formatting for Text'''

    #Timestamp
    now = datetime.now()
    # dd/mm/YY H:M
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
        
    #Min / Max
    master_list = []
    for i in list_t:
        new_list = i.split(',')
        master_list.append(new_list[6])
    float_list = []
    for i in master_list:
        current_value = i
        new_float = float(current_value)
        float_list.append(new_float)
        maximum = max(float_list)
    max_formatted = format(maximum, '.2f')
    print(f'Minimum Price: ${min(float_list)}')
    print(f'Maximum Price: ${max_formatted}')

    #median ram
    ram = 0 
    for j in list_t:
        j_split = j.split(',')
        ram += int(j_split[3])
    average_ram = ram / len(list_t)
    if average_ram <= 20:
        new_ram = 8.0
        print(f'Median RAM: {new_ram} GB')
    elif average_ram >20.0 and average_ram <48.0:
        new_ram = 32.0
        print(f'Median RAM: {new_ram} GB')
    elif average_ram > 20 and average_ram > 48:
        new_ram = 64.0
        print(f'Median RAM: {new_ram} GB')
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
    '''list_t = literal list  of items (phone, laptop, tablet) *** input_type = item to generate report for (phone, tablet, laptop) formatting for CSV'''
    now = datetime.now()
    # dd/mm/YY H:M
    dt_string = now.strftime("%Y-%m-%d %H:%M")

    #average
    total = 0 
    for i in list_t:
        i_split = i.split(',')
        total += float(i_split[6])
    average = total / len(list_t)

    #Min / Max 
    master_list = []
    for i in list_t:
        new_list = i.split(',')
        master_list.append(new_list[6])
    float_list = []
    for i in master_list:
        current_value = i
        new_float = float(current_value)
        float_list.append(new_float)




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
    print(f'{dt_string},{input_type.capitalize()},{len(list_t)},{average:.2f},{min(float_list)},{max(float_list)},{new_ram},{master_csv}')

def json_report(list_t, input_type):
    '''list_t = literal list  of items (phone, laptop, tablet) *** input_type = item to generate report for (phone, tablet, laptop)  formatting for JSON '''
    now = datetime.now()
    # dd/mm/YY H:M
    dt_string = now.strftime("%Y-%m-%d %H:%M")

    #Average price
    total = 0 
    for h in list_t:
        h_split = h.split(',')
        total += float(h_split[6])
    average = total / len(list_t)

    master_list = []
    for i in list_t:
        new_list = i.split(',')
        master_list.append(new_list[6])
    float_list = []
    for i in master_list:
        current_value = i
        new_float = float(current_value)
        float_list.append(new_float)

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
        all_string = f'\n          "{a} {b}",'
        str_json += all_string
    master_json = str_json.rstrip(',')
    print('{' '\n'
        f'      \"date_time\": "{dt_string}",''\n'
        f'      \"device_type\": "{input_type.capitalize()}",''\n'
        f'      \"number\": {len(list_t)},''\n'
        f'      \"average_price\": {average:.2f},''\n'
        f'      \"min_price\": {min(float_list)},''\n'
        f'      \"max_price\": {max(float_list)},''\n'
        f'      \"median_ram\": {new_ram},''\n'
        f'      \"operating_system\": [{master_json}      \n     ] \n '
        '}')


