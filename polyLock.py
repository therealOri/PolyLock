# Imports
import os
import sys
import beaupy
import base64
import random
import shutil
import requests
import subprocess
from Chaeslib import Chaes
from beaupy.spinners import *
from pystyle import Colors, Colorate
import binascii
import lzma


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
    return valid, response




def pastebin_login(api_dev_key):
    print('Please login to your account using your username and password.  |  Why do you need to login?: https://pastebin.com/doc_api#9\n\n')
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



def local_store(stuff, file_path):
    code2 = f'''import binascii

stuff = {stuff}

full_stuff = "".join(stuff)
full_stuff_bytes = full_stuff.encode()
more_stuff = binascii.unhexlify(full_stuff_bytes).decode()
exec(more_stuff)
'''
    with open(file_path, 'w') as wf:
        wf.write(code2)



def clean_up(file_name):
    clear()
    cleaning_spinner = Spinner(ARC, "Cleaning Up...")
    cleaning_spinner.start()
    os.remove(f'{file_name}.py')
    os.remove(f'{file_name}.c')
    shutil.rmtree('build')

    if sys.platform == 'win32':
        ext = '.pyd'
    else:
        ext = '.so'

    for filename in os.listdir('.'): # current directory/folder
        if not filename.endswith(ext):
            pass
        else:
            new_name = f'{file_name}{ext}'
            os.rename(filename, new_name)
            break
    cleaning_spinner.stop()





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

        chunk_size = 128
        with open(file_path, 'rb') as rf:
            file_data = rf.read()

        enc_file_data = chaes.encrypt(file_data, eKey)
        enc_chunks = [enc_file_data[i:i+chunk_size] for i in range(0, len(enc_file_data), chunk_size)]
        enc_stuff=[]
        for i, chunk in enumerate(enc_chunks):
            enc_stuff.append(f"{chunk}")


        file_name='part.py'
        if os.path.isfile(file_name):
            count = 1
            while True:
                file_name = f'part_{count}.py'
                if os.path.isfile(file_name):
                    count += 1
                    continue
                else:
                    break


        with open(file_name, 'w') as fw:
            code_part = f'''locked_data = "{enc_stuff}"'''
            fw.write(code_part)

        with open('setup.py', 'w') as fws:
            setup_code=f'''from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("{file_name}")
)
'''
            fws.write(setup_code)

        base_file_name = os.path.splitext(file_name)[0]
        subprocess.check_call([sys.executable, 'setup.py', 'build_ext', '--inplace'])


        code = f'''import base64
from Chaeslib import Chaes
import beaupy
import sys
import ast
import {base_file_name}


data = {base_file_name}.locked_data
data_lst = ast.literal_eval(data)
built_stuff = "".join(data_lst)

chaes = Chaes()
chaes.clear()
dKey = beaupy.prompt("Encryption Key")
if not dKey:
    chaes.clear()
    sys.exit()

try:
    enc_data = chaes.hex_to_base64(built_stuff)
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

        clean_up(base_file_name)
        clear()
        if beaupy.confirm("Do you want to obfuscate code?"):
            try:
                subprocess.check_call([sys.executable, 'specter.py'])
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
                    if check[0] == False:
                        print(f"An error has occured...\nError: {check[1].text}  | Code: {check[1].status_code}")
                        api_user_key = pastebin_login(api_dev_key)
                else:
                    api_user_key = pastebin_login(api_dev_key)
            else:
                api_user_key=''
                #post to pastebin as guest



            chunk_size = 128
            with open(file_path, 'rb') as rb:
                obf_code = rb.read()
                encoded_obf_code = binascii.hexlify(obf_code)

            chunks = [encoded_obf_code[i:i+chunk_size] for i in range(0, len(encoded_obf_code), chunk_size)]
            stuff=[]
            for i, chunk in enumerate(chunks):
                stuff.append(f"{chunk.decode()}")

            stuff = f'{stuff}'
            N = 2
            part_size = len(stuff) // N
            parts = []

            for i in range(N):
                start = i * part_size
                end = (i+1) * part_size if i < N-1 else len(stuff)
                parts.append(stuff[start:end])

            # Upload each part and get paste IDs
            letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
            digits = "012345678901234567890123456789"
            paste_names = [''.join(random.choices(letters + digits, k=10)) for i in range(5)]
            paste_ids = []

            paste_spinner = Spinner(ARC, "Storing code in pastebin...")
            paste_spinner.start()
            for part, name in zip(parts, paste_names):
                api_data = {'api_dev_key':api_dev_key,
                        'api_option':'paste',
                        'api_user_key':api_user_key,
                        'api_paste_code':part,
                        'api_paste_name': name
                }
                response = requests.post('https://pastebin.com/api/api_post.php', data=api_data)
                paste_ids.append(response.text.split('/')[-1])



            code2 = f'''import binascii
import requests
import ast
from beaupy.spinners import *

part_url_1 = 'https://pastebin.com/raw/{paste_ids[0]}'
part_url_2 = 'https://pastebin.com/raw/{paste_ids[1]}'


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
            quit(f"Error fetching {{url}} | Status: {{response.status_code}}")


    full_stuff_lst = ast.literal_eval(full_stuff)
    full_stuff = "".join(full_stuff_lst)
    full_stuff_bytes = full_stuff.encode()
    more_stuff = binascii.unhexlify(full_stuff_bytes).decode()

    spinner.stop()
    exec(more_stuff)

except Exception as e:
    spinner.stop()
    print(f"Error with request: {{e}}")
'''

            if response.status_code == 200:
                with open(file_path, 'w') as wf:
                    wf.write(code2)
                paste_spinner.stop()
            else:
                paste_spinner.stop()
                clear()
                input(f'Unable to make a request to pastebin with error: [{response.text}  |  {response.status_code}], defaulting to writing to file instead.\n\nPress "enter" to continue...')
                clear()
                local_store(stuff, file_path)

        else:
            chunk_size = 128
            with open(file_path, 'rb') as rb:
                obf_code = rb.read()
                encoded_obf_code = binascii.hexlify(obf_code)

            chunks = [encoded_obf_code[i:i+chunk_size] for i in range(0, len(encoded_obf_code), chunk_size)]
            stuff=[]
            for i, chunk in enumerate(chunks):
                stuff.append(f"{chunk.decode()}")
            local_store(stuff, file_path)


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
