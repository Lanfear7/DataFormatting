import sys
import data
import reports
import datetime
import statistics

PRICE_INDEX = 6
RAM_INDEX = 3
OS_INDEX = 4
OS_VERSION_INDEX = 5


def main():
    """Displaying device information in the format that has passed to the command line argument"""

    input_type_list = ("phone", "tablet", "laptop")
    report_type_list = ("text", "csv", "json", "yaml")

    if len(sys.argv) != 4:
        print("Invalid number of command line arguments")
        exit(0)

    input_type = sys.argv[1]
    report_type = sys.argv[2]
    file_name = sys.argv[3]

    if input_type not in input_type_list:
        print("Input type must be either phone, tablet or laptop.")
        exit(0)

    if report_type not in report_type_list:
        print("Report type must be either text, csv or yaml.")
        exit(0)

    if file_name == '':
        print('Report Filename must be a non-empty string ')
        exit(0)
        
    results = []

    if input_type == 'phone':
        results.extend(data.get_phone_info_list())
    elif input_type == 'tablet':
        results.extend(data.get_tablet_info_list())
    elif input_type == 'laptop':
        results.extend(data.get_laptop_info_list())

    prices = []
    ram = []
    oses = []

    # Extract the relevant data from the results. The format is the
    # same for all the data types.
    for result in results:
        fields = result.split(",")
        prices.append(float(fields[PRICE_INDEX]))
        ram.append(int(fields[RAM_INDEX]))
        oses.append(fields[OS_INDEX] + " " + fields[OS_VERSION_INDEX])

    os_single = []
    for i in oses: 
        if i not in os_single: 
            os_single.append(i) 
    reverse = sorted(os_single, reverse=True)



    current_datetime = datetime.datetime.now()
    device_name = input_type.title()
    num_devices = len(results)
    avg_price = round(statistics.mean(prices), 2)
    min_price = min(prices)
    max_price = max(prices)
    median_ram = statistics.median(ram)

    if "text" == report_type:
        reports.text_report(current_datetime, device_name, num_devices,
                            avg_price, min_price, max_price,
                            median_ram, reverse, file_name)
    elif "json" == report_type:
        reports.json_report(current_datetime, device_name, num_devices,
                            avg_price, min_price, max_price,
                            median_ram, reverse, file_name)
    elif "csv" == report_type:
        reports.csv_report(current_datetime, device_name, num_devices,
                           avg_price, min_price, max_price,
                           median_ram, reverse, file_name)
    elif "yaml" == report_type:
        reports.yaml_report(current_datetime, device_name, num_devices,
                           avg_price, min_price, max_price,
                           median_ram, reverse, file_name)


if __name__ == "__main__":
    main()

