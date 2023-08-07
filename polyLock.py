# Imports
import os
import sys
import beaupy
import base64
import requests
import subprocess
from Chaeslib import Chaes
from beaupy.spinners import *
from pystyle import Colors, Colorate



# Helper Functions
def clear():
    os.system("clear||cls")


def banner():
    banner = """
     ██████╗  ██████╗ ██╗  ██╗   ██╗██╗      ██████╗  ██████╗██╗  ██╗
     ██╔══██╗██╔═══██╗██║  ╚██╗ ██╔╝██║     ██╔═══██╗██╔════╝██║ ██╔╝
     ██████╔╝██║   ██║██║   ╚████╔╝ ██║     ██║   ██║██║     █████╔╝
     ██╔═══╝ ██║   ██║██║    ╚██╔╝  ██║     ██║   ██║██║     ██╔═██╗
     ██║     ╚██████╔╝███████╗██║   ███████╗╚██████╔╝╚██████╗██║  ██╗
     ╚═╝      ╚═════╝ ╚══════╝╚═╝   ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝


     Made by Ori#6338 | @therealOri_ | https://github.com/therealOri



    """
    colored_banner = Colorate.Horizontal(Colors.purple_to_blue, banner, 1)
    return print(colored_banner)




def compile_code(file_path):
    result_code = subprocess.run(['nuitka3', '--version'])
    if result_code.returncode != 0:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'nuitka'])
        except Exception as e:
            clear()
            input(f'An error has occured while trying to install the nuitka compiler. You can try to install it manually from pypi by using "pip install nuitka" then try to run this code again.\n\nError: {e}\n\nPress "enter" to exit...')
            clear()
            exit()

    clear()
    if beaupy.confirm("Want to add an icon?"):
        icon_file = beaupy.prompt("Path to the picture you want to use as an icon.")
        if not icon_file:
            icon_arg = ''
        icon_file = icon_file.replace('\\', '').strip()
        if sys.platform == 'win32':
            icon_arg = '--windows-icon-from-ico=%s' % icon_file
        elif sys.platform == 'linux':
            icon_arg = '--linux-icon=%s' % icon_file
        elif sys.platform == 'darwin':
            icon_arg = '--macos-app-icon=%s' % icon_file
        else:
            icon_arg = ''

        args = ['nuitka3', '--follow-imports', icon_arg, file_path]
    else:
        args = ['nuitka3', '--follow-imports', file_path]

    subprocess.check_call(args)




def check_pastebin_key(dev_key, user_key):
    spinner = Spinner(ARC, "Validating user_key...")
    spinner.start()
    url = 'https://pastebin.com/api/api_post.php'
    data = {
        'api_dev_key': dev_key,
        'api_user_key': user_key,
        'api_option': 'paste',
        'api_paste_code': 'user_key_validation_test',
        'api_paste_name': 'user_key_validation_test'
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        valid = True
        paste_key = response.text
        paste_code_id = paste_key.split('/')[-1]
    else:
        valid = False


    if valid == True:
        data = {
            'api_dev_key': dev_key,
            'api_user_key': user_key,
            'api_option': 'delete',
            'api_paste_key': paste_code_id
        }
        requests.post(url, data=data)

    spinner.stop()
    return valid




def pastebin_login(api_dev_key):
    print('Please login to your account using your username and password.\nWhy do you need to login?: https://pastebin.com/doc_api#9\n\n')
    pbin_username = beaupy.prompt("Pastebin Username.", secure=True)
    pbin_password = beaupy.prompt("Pastebin Password.", secure=True)

    api_data_pkg = {'api_dev_key':api_dev_key,
            'api_user_name':pbin_username,
            'api_user_password':pbin_password
    }
    response = requests.post('https://pastebin.com/api/api_login.php', data=api_data_pkg)
    api_user_key = response.text
    if response.status_code == 200:
        clear()
        input(f'Pastebin User Key - (Save me & Do not share): "{api_user_key}"\n\nPress "enter" to contine...')
        clear()
        return api_user_key
    else:
        clear()
        input(f'Unable to login...\nError code: "{api_user_key.status_code}"\nPosting paste as guest instead.\n\nPress "enter" to contine...')
        clear()
        api_user_key=''
        return api_user_key





def check_file(file_path):
    if not os.path.exists(file_path):
        return False

    if not file_path.endswith('.py'):
        return False

    return True





# The Goods
def main():
    file_path = beaupy.prompt("Path to the file you want to obfuscate/lock.")
    if not file_path:
        clear()
        exit()

    file_path = file_path.replace('\\', '').strip()
    check = check_file(file_path)
    if check == False:
        clear()
        exit(msg="Invalid file type or file doesn't exist...")
    else:
        chaes = Chaes()
        key_data = input("Data for key gen - (100+ random characters): ").encode()

        clear()
        eKey = chaes.keygen(key_data)

        if not eKey:
            exit()

        save_me = base64.b64encode(eKey)
        bSalt = base64.b64encode(chaes.salt)
        master_key = f"{save_me.decode()}:{bSalt.decode()}"

        input(f'Save this key so you can decrypt later: {master_key}\n\nPress "enter" to contine...')
        clear()

        with open(file_path, 'rb') as rf:
            file_data = rf.read()

        enc_file_data = chaes.encrypt(file_data, eKey)

        code = f'''import base64
from Chaeslib import Chaes
import beaupy
import sys

locked_data = "{enc_file_data}"


chaes = Chaes()
chaes.clear()
dKey = beaupy.prompt("Encryption Key")
if not dKey:
    chaes.clear()
    sys.exit()

try:
    enc_data = chaes.hex_to_base64(locked_data)
    json_input = base64.b64decode(enc_data)
    key_and_salt = dKey.split(":")
    salt_1 = key_and_salt[1]
    key_0 = key_and_salt[0]

    salt = base64.b64decode(salt_1)
    key = base64.b64decode(key_0)
except Exception:
    chaes.clear()
    print("Unable to unlock file.")
    sys.exit()

try:
    unlocked_data = chaes.decrypt(key, json_input, salt).decode()
except Exception:
    chaes.clear()
    print("Unable to decrypt data.")
    sys.exit()

chaes.clear()
exec(unlocked_data)
'''

        with open(file_path, 'w') as wf:
            wf.write(code)

        if beaupy.confirm("Do you want to obfuscate code?"):
            try:
                subprocess.check_call([sys.executable, 'hyperion.py'])
            except Exception as e2:
                clear()
                input(f'An error has occured while trying to obfuscate code. Something may have gone wrong while obfuscating or running the command "python hyperion.py" using subprocess.\n\nError: {e2}\n\nPress "enter" to exit...')
                clear()
                exit()

        clear()
        #gotta love adding logic :')
        if beaupy.confirm("Do you want to use pastebin for storage?"):
            api_dev_key = beaupy.prompt('Pastebin DEV key.')

            if beaupy.confirm("Want to post to YOUR pastebin account?"):
                if beaupy.confirm("(!Warning!) - If you generate a new key, your old key will no longer be valid.\nDo you already have your pastebin USER key?\n\n"):
                    api_user_key = beaupy.prompt("Pastebin USER key.")

                    check = check_pastebin_key(api_dev_key, api_user_key)
                    if check == False:
                        print("Invalid api_user_key...")
                        api_user_key = pastebin_login(api_dev_key)
                else:
                    api_user_key = pastebin_login(api_dev_key)
            else:
                api_user_key=''
                #post to pastebin as guest

            chunk_size = 256 #bigger the file, bigger the chunk size...until it breaks because strings are to long or something..idk
            with open(file_path, 'rb') as rb:
                obf_code = rb.read()
                encoded_obf_code = base64.b64encode(obf_code)

            chunks = [encoded_obf_code[i:i+chunk_size] for i in range(0, len(encoded_obf_code), chunk_size)]
            stuff=[]
            for i, chunk in enumerate(chunks):
                stuff.append(f"{chunk.decode()}")

            api_data = {'api_dev_key':api_dev_key,
                    'api_option':'paste',
                    'api_user_key':api_user_key,
                    'api_paste_code':f'{stuff}'
            }

            response = requests.post('https://pastebin.com/api/api_post.php', data=api_data)
            api_paste_code = response.text
            paste_code_id = api_paste_code.split('/')[-1]

            code2 = f'''import base64
import requests

api_url = 'https://pastebin.com/raw/{paste_code_id}'
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
        print(f"Invalid response code: {{status_code}}")

except Exception as e:
    print(f"Error with request: {{e}}")
'''

            if response.status_code == 200:
                with open(file_path, 'w') as wf:
                    wf.write(code2)
            else:
                clear()
                input('Unable to make a request to pastebin, defaulting to writing to file instead.\n\nPress "enter" to continue...')
                clear()
                code2 = f'''import base64
stuff = {stuff}
full_stuff = "".join(stuff)
full_stuff_bytes = full_stuff.encode()
more_stuff = base64.b64decode(full_stuff_bytes).decode()
exec(more_stuff)
'''
                with open(file_path, 'w') as wf:
                    wf.write(code2)


        else:
            #64
            chunk_size = 256
            with open(file_path, 'rb') as rb:
                obf_code = rb.read()
                encoded_obf_code = base64.b64encode(obf_code)

            chunks = [encoded_obf_code[i:i+chunk_size] for i in range(0, len(encoded_obf_code), chunk_size)]
            stuff=[]
            for i, chunk in enumerate(chunks):
                stuff.append(f"{chunk.decode()}")

            code2 = f'''import base64
stuff = {stuff}
full_stuff = "".join(stuff)
full_stuff_bytes = full_stuff.encode()
more_stuff = base64.b64decode(full_stuff_bytes).decode()
exec(more_stuff)
'''
            with open(file_path, 'w') as wf:
                wf.write(code2)


        if beaupy.confirm("Do you want to compile the code to an executable?"):
            compile_code(file_path)
            clear()
            input('Code has been successfully locked, obfuscated, and compiled to an executable/binary.\n\nPress "enter" to continue/exit...')
            clear()
        else:
            clear()
            input('Code has been successfully locked/obfuscated.\n\nPress "enter" to continue/exit...')
            clear()









if __name__ == '__main__':
    clear()
    banner()
    main()
