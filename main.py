import reports, data, sys

input_type = sys.argv[1].lower()
report_type = sys.argv[2].lower()

def main(input_type, report_type):
    if input_type == 'phone':
        print('phone')
        phone_data = data.get_phone_info_list()
        phone_list = []
        for i in phone_data:
            i.split(',')
            phone_list.append(i)
        ##pass in phone_list into the text_report function 
        if report_type == 'text':
            print('text')
            reports.text_report(phone_list, input_type)
        elif report_type == 'csv':
            print('csv')
            reports.csv_report(phone_list, input_type)
        elif report_type == 'json':
            print('json')
            reports.json_report(phone_list, input_type)
        else:
            print('Report type must be either text, csv or json')
    elif input_type == 'tablet':
        print('tablet')
        tablet_data = data.get_tablet_info_list()
        tablet_list = []
        for i in tablet_data:
            i.split(',')
            tablet_list.append(i)
        print(tablet_list)
        #pass in tablet_list into the text_report function 
        if report_type == 'text':
            print('text')
            reports.text_report(tablet_list, input_type)
        elif report_type == 'csv':
            print('csv')
            reports.csv_report(tablet_list, input_type)
        elif report_type == 'json':
            print('json')
            reports.json_report(tablet_list, input_type)
        else:
            print('Report type must be either text, csv or json')
    elif input_type == 'laptop':
        print('laptop')
        laptop_data = data.get_laptop_info_list()
        laptop_list = []
        for i in laptop_data:
            i.split(',')
            laptop_list.append(i)
        if report_type == 'text':
            print('text')
            reports.text_report(laptop_list, input_type)
        elif report_type == 'csv':
            print('csv')
            reports.csv_report(laptop_list, input_type)
        elif report_type == 'json':
            print('json')
            reports.json_report(laptop_list, input_type)
        else:
            print('Report type must be either text, csv or json')
    else:
        print('Input type must be either phone, table or laptop ')



if __name__=='__main__':
    main(input_type, report_type)
