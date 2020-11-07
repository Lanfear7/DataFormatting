# Data Module

def get_phone_info_list():
    """ Returns a list of phone data """

    # Format <id>,<manufacturer>,<model>,<memory in GB>,<operating system>,<os version>,<price>
    f = open("phones.csv", "r")
    fd = f.readlines()
    f.close()

    return fd


def get_tablet_info_list():
    """ Returns a list of tablet data """

    # Format <id>,<manufacturer>,<model>,<memory in GB>,<operating system>,<os version>,<price>
    f = open("tablets.csv", "r")
    fd = f.readlines()
    f.close()

    return fd


def get_laptop_info_list():
    """ Returns a list of laptop data """

    # Format <id>,<manufacturer>,<model>,<memory in GB>,<operating system>,<os version>,<price>
    f = open("laptops.csv", "r")
    fd = f.readlines()
    f.close()

    return fd
