# Imports
import os
import sys
import beaupy
import base64
import subprocess
from Chaeslib import Chaes



# Helper Functions
def clear():
    os.system("clear||cls")


#idk if this will conflict with the already existing "exit()" python uses by default.
#sys.exit() is to allow the compiled executable to work on windows as the normal "exit()" doesn't want to work.'
def exit(msg=None):
    if not msg or msg == None:
        sys.exit()
    else:
        sys.exit(msg)


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
            icon_arg=''
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





# The Goods
def main():
    file_path = beaupy.prompt("Path to the file you want to obfuscate/lock.")
    if not file_path:
        clear()
        exit()

    file_path = file_path.replace('\\', '').strip()
    if not file_path.endswith('.py') and os.path.isfile(file_path):
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
chase.clear()
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
                input(f'An error has occured while trying to obfuscate code. Ssomething may have gone wrong while obfuscating or running the command "python hyperion.py" using subprocess.\n\nError: {e2}\n\nPress "enter" to exit...')
                clear()
                exit()

        clear()
        chunk_size = 64
        with open(file_path, 'rb') as rb:
            obf_code = rb.read()
            encoded_obf_code = base64.b64encode(obf_code)

        #NOTE
        #The following code here is kind of a patch to not only make compiling a little faster but to help hyperion when obfuscating and allowing Nuitka to compile and run the code with little to no issues. Instead of having python break because strings are to long, idk.
        chunks = [encoded_obf_code[i:i+chunk_size] for i in range(0, len(encoded_obf_code), chunk_size)]
        code2 = '''
import base64
stuff = []
'''
        for i, chunk in enumerate(chunks):
            code2 += f'stuff.append("{chunk.decode()}")\n'

        code2 += '''
full_stuff = "".join(stuff)
full_stuff_bytes = full_stuff.encode()
more_stuff = base64.b64decode(full_stuff_bytes).decode()
exec(more_stuff)
'''
        code2 = code2.lstrip()
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
    main()
