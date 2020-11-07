import json, yaml


def text_report(date, type, num_devices, avg_price, min_price, max_price, median_ram, oses, file_name):
    """ Displaying Device information in text format """
    d_str = str("Average Price: $%.2f" % avg_price)
    a_str = str("Timestamp: %s" % date.strftime("%Y-%m-%d %H:%M"))
    b_str = str("Device: %s" % type)
    c_str = str("Number: %d" % num_devices)
    e_str = str("Minimum Price: $%.2f" % min_price)
    f_str = str("Maximum Price: $%.2f" % max_price)
    g_str = str("Median RAM: %.1f GB" % median_ram)
    h_str = str("Operating Systems: %s" % ", ".join(oses))
    print(f"{d_str}\n{a_str}\n{b_str}\n{c_str}\n{e_str}\n{f_str}\n{g_str}\n{h_str}\n")
    #file report
    f = open(f"{file_name}.txt", "a")
    f.write(f"{d_str}\n{a_str}\n{b_str}\n{c_str}\n{e_str}\n{f_str}\n{g_str}\n{h_str}\n")
    f.close()


def csv_report(date, type, num_devices, avg_price, min_price, max_price, median_ram, oses, file_name):
    """ Displaying Device information in csv format """
    current_date = date.strftime("%Y-%m-%d %H:%M")
    csv = f"{'%.2f' % avg_price},{current_date},{type}{num_devices},{'%.2f' % min_price},{'%.2f' % max_price},{'%.1f' % median_ram},{oses}"
    print(csv)
    #file report
    f = open(f"{file_name}.csv", "a")
    f.write(csv)
    f.close()


def yaml_report(date, type, num_devices, avg_price, min_price, max_price, median_ram, oses, file_name):
    """ Displaying Device information in yaml format """
    current_date = date.strftime("%Y-%m-%d %H:%M")
    data = {
        "average_price": "%.2f" % avg_price ,
        "date_time": current_date,
        "device_type": type,
        "number": num_devices,
        "min_price":"%.2f" % min_price ,
        "max_price": "%.2f" % max_price ,
        "median_ram": "%.1f" % median_ram,
        "operating_systems": oses
    } 
    yaml_data = yaml.dump(data, default_flow_style=False)
    print(yaml_data)
    #file report
    f = open(f"{file_name}.yaml", "a")
    f.write(yaml_data)
    f.close()


def json_report(date, type, num_devices, avg_price, min_price, max_price, median_ram, oses, file_name):
    """ Displaying Device information in json format """
    current_date = date.strftime("%Y-%m-%d %H:%M")
    json_data = {
        "average_price": "%.2f" % avg_price ,
        "date_time": current_date,
        "device_type": type,
        "number": num_devices,
        "min_price":"%.2f" % min_price ,
        "max_price": "%.2f" % max_price ,
        "median_ram": "%.1f" % median_ram,
        "operating_systems": oses
    } 
    fj = json.dumps(json_data, indent=4)
    print(fj)
    #file report
    f = open(f"{file_name}.json", "a")
    f.write(fj)
    f.close()


