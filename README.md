# About
PolyLock is a new and advanced python3 code obfuscator and encryptor, helping you keep your code secure/safe and still runable/executable.


- Encryption is handled with [Chaeslib](https://pypi.org/project/Chaeslib/)

- Obfscation is handled by my fork of [Specter](https://github.com/therealOri/Specter/)

- Code compilation is handled by [Nuitka](https://github.com/Nuitka/Nuitka/).


You can provide any .py file you like, PolyLock will then encrypt the file's data and then obfuscate it. You will then be asked if you want to compile the .py to an executable and if you say yes, you will be left with either an executable binary or a windows .exe file. Making sure your code is secure and obfuscated. You can also allow the ussage of pastebin to store parts of the obfuscated code, keeping the final result small.

If you like what I have made, please leave a star! :star: and share this project with your friends and communities!
__ __

<br>
<br>

# Flowchart
![polylock_diagram](https://github.com/therealOri/PolyLock/assets/45724082/4e484bdb-22b9-438b-81a5-0e0b1b6bdfdf)
> Dev note;
>
> This is my first time making a flow chart/diagram, It may not be pretty or the best but hopefully it's at the very minimum understandable.
__ __

<br>
<br>

# Updates
The full list of changes can be found in the [Changelog.md](https://github.com/therealOri/PolyLock/blob/main/CHANGELOG.md).

<br>

❄️ (Latest) ❄️
> 09/12/23
- Added a windows compatibility patch for the `compile_code()` function.
- Removed option for whether or not to add an icon to the compiled executable.

__ __

<br>
<br>

# Installation
```
git clone https://github.com/therealOri/PolyLock.git
```
```
cd PolyLock
```
```
virtualenv plkENV
```
```
source plkENV/bin/activate
```
```
pip install -r requirements.txt
```
```
python polyLock.py
```
> If you don't have `virtualenv`, you can install it via "pip". `pip install virtualenv`.
__ __

<br>
<br>

# Extra Info
The `setup.py` file is used by PolyLock to cythonize the `part.py` file that will be created that stores the encrypted data of the file you have given polylock. "`part.py`" will either be a .so file or .pyd file..depending on if you use Linux/Mac or Windows. You WILL need that .so/.pyd file along side of your original/now modified file, otherwise nothing will happen or you will get an error.

Specter can be used by itself if you want to use it instead of polylock, but let it be known that it is for obfuscation and does not aim to be both encryption and obfuscation, etc. It also doesn't really like to handle large files (anything over 70kb-80kb in file size).
__ __

<br>
<br>

# ⚠️ Warning & disclaimer
I have not tested ANY of the code on a windows system so I have no idea what works and what doesn't..(yet). If you are using windows then please feel free to test it out and get back to me with any issues that occur by making an [issue](https://github.com/therealOri/PolyLock/issues/new/choose) report. Please and thanks!

Also! I shall not be held liable or be punishable on or off ANY platforms for what users do with this code and or what code they obfuscate, etc. This code was made for the intended purpose of keeping code personal, safe, and secure. Not really any different than normal file/data encryption.
__ __

<br />
<br />
<br />


# Support  |  Buy me a coffee <3
Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)

