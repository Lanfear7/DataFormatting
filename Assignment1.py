def main(input_type, report):
    '''this will hold the logic of the program'''
    if input_type == 'phone' or 'tablet' or 'laptop' :
        print('good device')
    else:
        print('Input type must be either phone, table or laptop ')
    if report == 'text' or 'csv' or 'json':
        print('good input')
    else:
        print('Report type must be either text, csv or json')




if __name__ == '__main__':
    main('phone', 'text')