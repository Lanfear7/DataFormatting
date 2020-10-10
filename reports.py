from datetime import datetime

def date():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y-%m-%d %H:%M")
    print("date and time =", dt_string)

def text_report():
    pass


def csv_report():
    pass


def json_report():
    pass