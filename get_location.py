import IP2Location
import re
import socket


def get_physical_location(address):
    address = re.sub(':.*', '', address)  # 用正则表达式去除端口部分
    try:
        ip_address = socket.gethostbyname(address)
    except socket.gaierror:
        ip_address = address

    try:
        database = IP2Location.IP2Location("./IP2LOCATION-LITE-DB3.BIN")
        rec = database.get_all(ip_address)
        #print(rec.country_short)
        country_short = rec.country_short
        city = rec.city
        #return f"{country}_{city}"
        return f"{country_short}"
    except database.not_found_exception as e:
        print(f"Error: {e}")
        return "Unknown"
    


if __name__ == "__main__":
    address = "8.8.8.8"
    print(get_physical_location(address))