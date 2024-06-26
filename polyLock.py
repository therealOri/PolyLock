# Imports
import os
import re
import sys
import beaupy
import base64
import random # for generating names, not for anything involving encryption.
import shutil
import requests
import subprocess
from Chaeslib import Chaes
from beaupy.spinners import *
from pystyle import Colors, Colorate
import binascii
import lzma
import json
import time





def clear():
    os.system("clear||cls")


tools = ['curl', 'wget', 'git']
for tool in tools:
    try:
        subprocess.check_output([tool, '--version'])
    except OSError:
        clear()
        input(f'{tool} not found, please install {tool} and then try again.\n\nPlease press "enter" to exit...')
        clear()
        quit()




if not os.path.exists('polybin.so'):
    try:
        print("Unable to import polybin. (Either not found or not able to be imported.\nTrying to install polybin...)\n")
        subprocess.check_call(['wget', 'https://raw.githubusercontent.com/therealOri/PolyLock/master/polybin.so'])
        from polybin import *
    except:
        clear()
        input('Unable to install/download "polybin", you will need to download it manually, place it in the same place as "polyLock", and then try again.\nYou can find it here: https://github.com/therealOri/PolyLock\n\n\nPlease press "enter" to exit...')
        clear()
        quit()
else:
    from polybin import *







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
    if sys.platform == 'win32':
        platform_command = ['cmd.exe', '/c', 'nuitka', '--version']
        system_args = ['cmd.exe', '/c', 'nuitka', '--follow-imports', file_path]
    else:
        platform_command = ['nuitka3', '--version']
        system_args = ['nuitka3', '--follow-imports', file_path]

    try:
        result_code = subprocess.run(platform_command) #check to see if nuitka is installed.
    except:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'nuitka'])
        except Exception as e:
            clear()
            input(f'An error has occured while trying to install the nuitka compiler. You can try to install it manually from pypi by using "pip install nuitka" then try to run this code again.\n\nError: {e}\n\nPress "enter" to exit...')
            clear()
            exit()

    clear()
    args = system_args
    subprocess.check_call(args)




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

    awrgas = dbvcfautrfuaiyu(code2)
    code2_2 = f"""from polybin import *
sgfiydu = "{awrgas}"
ugsjdkfoug = iuiyiavfaapi(sgfiydu)

exec(ugsjdkfoug)
"""
    with open(file_path, 'w') as fw:
        fw.write(code2_2)





def validate_github_user(git_name):
    url = f"https://api.github.com/users/{git_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return 200
    elif response.status_code == 404:
        return 404





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



        code = f'''import base64
from Chaeslib import Chaes
import beaupy
import sys
import ast


splt_enc_stff = {enc_stuff}

chaes = Chaes()
chaes.clear()
dKey = beaupy.prompt("Encryption Key")
if not dKey:
    chaes.clear()
    sys.exit()

try:
    enc_stuff = "".join(splt_enc_stff)
    enc_data = chaes.hex_to_base64(enc_stuff)
    json_input = base64.b64decode(enc_data)
    key_and_salt = dKey.split(":")
    salt_1 = key_and_salt[1]
    key_0 = key_and_salt[0]

    salt = base64.b64decode(salt_1)
    key = base64.b64decode(key_0)
except Exception:
    chaes.clear()
    print("Invalid key, unable to continue...")
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

        with open(file_path, 'w') as fw:
            fw.write(code)

        clear()
        print("Note: (WIP - May break or throw errors. Make sure to have a backup of your original saved before obfuscating in case you need to restart/try again.)\n")
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
        if beaupy.confirm("Do you want to use github for storage?"):
            chunk_size = 128
            with open(file_path, 'rb') as rb:
                obf_code = rb.read()
                encoded_obf_code = binascii.hexlify(obf_code)

            chunks = [encoded_obf_code[i:i+chunk_size] for i in range(0, len(encoded_obf_code), chunk_size)]
            stuff=[]
            for i, chunk in enumerate(chunks):
                stuff.append(f"{chunk.decode()}")


            letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
            digits = "012345678901234567890123456789"
            file_name = ''.join(random.choices(letters + digits, k=10)) #k = length
            new_repo_name = ''.join(random.choices(letters + digits, k=10))

            with open(f"{file_name}.txt", 'w') as tmpw:
                tmpw.write(f"{stuff}")


            while True:
                github_username = beaupy.prompt("Your github username - (Example: therealOri)")
                if not github_username:
                    clear()
                    input('Username can NOT be an empty string or None.\n\nPress "enter" to try again...')
                    clear()
                    continue

                valid = validate_github_user(github_username)
                if valid == 404:
                    clear()
                    input('Invalid Username provided.\n\nPress "enter" to try again...')
                    clear()
                    continue
                else:
                    break


            while True:
                access_token = beaupy.prompt("GitHub Fine-Grained Access Token", secure=True)
                if not github_username:
                    clear()
                    input('access_token can NOT be an empty string or None.\n\nPress "enter" to try again...')
                    clear()
                    continue
                else:
                    break
            f=None
            if beaupy.confirm("Do you want to have a repository made for you? - (If you don't have a repository made already)"):
                f=True
                print("Creating Repository...")
                time.sleep(2.5)
                data = {"name":f"{new_repo_name}"}
                json_data = json.dumps(data)
                subprocess.check_call(['curl', '-s', '-H', f'Authorization: token {access_token}', '-d', json_data, 'https://api.github.com/user/repos'])
                remote_url = f"https://{access_token}@github.com/{github_username}/{new_repo_name}.git"
                subprocess.check_call(["git", "init"])
                subprocess.check_call(["git", "add", f"{file_name}.txt"])
                subprocess.check_call(["git", "commit", "-m", "Add file"])
                subprocess.check_call(["git", "remote", "add", "origin", remote_url])
                subprocess.check_call(["git", "push", "origin", "master"])
                shutil.rmtree(".git/")
                os.remove(f'{file_name}.txt')
                input(f'[+] Done! [+]\nCheck it out here: https://github.com/{github_username}/{new_repo_name}\n\nPress "enter" to continue...')
                clear()
            else:
                f=False
                while True:
                    repo_url = beaupy.prompt("Repository URL - (Example: https://github.com/therealOri/PolyFiles)")
                    match = re.search(r"github\.com/[^/]+/([^/]+)/?", repo_url)
                    if match:
                        existing_repo_name = match.group(1)
                        clear()
                        break
                    else:
                        clear()
                        input('Invalid URL provided.\n\nPress "enter" to try again...')
                        clear()
                        continue

                print(f"Updating {repo_url}...")
                time.sleep(2.5)
                remote_url = f"https://{access_token}@github.com/{github_username}/{existing_repo_name}.git"
                subprocess.check_call(['git', 'clone', repo_url])
                shutil.move(f'{file_name}.txt', f'{existing_repo_name}/')
                os.chdir(f'{existing_repo_name}')
                subprocess.check_call(["git", "add", f"{file_name}.txt"])
                subprocess.check_call(["git", "commit", "-m", "Add file"])
                subprocess.check_call(["git", "remote", "set-url", "origin", remote_url])
                subprocess.check_call(["git", "push", "origin", "master"])
                os.chdir('../')
                shutil.rmtree(f"{existing_repo_name}/")
                input(f'[+] Done! [+]\nQuick Access: https://github.com/{github_username}/{existing_repo_name}\n\nPress "enter" to continue...')
                clear()


            if f == True:
                repo_name = new_repo_name
            else:
                repo_name = existing_repo_name
            code2 = f'''import binascii
import ast
from beaupy.spinners import *
import requests
import os


def clear():
    os.system("clear||cls")


clear()
spinner = Spinner(ARC, "Building code...")
spinner.start()
try:
    url = "https://raw.githubusercontent.com/{github_username}/{repo_name}/master/{file_name}.txt"
    response = requests.get(url)
    if response.status_code == 404:
        spinner.stop()
        clear()
        print("Repository trying to be reached is set to private!")
        raise Exception("Unable to read private repository.")
        quit()
    else:
        full_stuff = requests.get("https://raw.githubusercontent.com/{github_username}/{repo_name}/master/{file_name}.txt")

    if full_stuff.status_code == 200:
        full_stuff_lst = ast.literal_eval(full_stuff.text)
        full_stuff = "".join(full_stuff_lst)
        full_stuff_bytes = full_stuff.encode()
        more_stuff = binascii.unhexlify(full_stuff_bytes).decode()

        spinner.stop()
        clear()
        exec(more_stuff)
    else:
        spinner.stop()
        clear()
        quit("Unable to get and or read file data from repository...")

except Exception as e:
    spinner.stop()
    clear()
    print(f"Error with request: {{e}}")
    print("You will need to re obfuscate the code/try again...")
'''

            awrgas = dbvcfautrfuaiyu(code2)
            code2_2 = f"""from polybin import *
sgfiydu = "{awrgas}"
ugsjdkfoug = iuiyiavfaapi(sgfiydu)

exec(ugsjdkfoug)
"""
            with open(file_path, 'w') as fw:
                fw.write(code2_2)

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


        clear()
        if beaupy.confirm("Do you want to compile the code to an executable?"):
            compile_code(file_path)
            file_name = os.path.basename(file_path)
            name_without_ext = os.path.splitext(file_name)[0]
            shutil.rmtree(f"{name_without_ext}.build")
            os.remove(file_path)
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
