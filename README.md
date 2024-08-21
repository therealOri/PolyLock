# About
PolyLock is a new and advanced python3 code obfuscator and encryptor, helping you keep your code secure/safe and still runable/executable.


- Encryption is handled with [Chaeslib](https://pypi.org/project/Chaeslib/)

- Obfscation is handled by my fork of [PyDelta](https://github.com/therealOri/PyDelta-PythonObfuscator)

- Code compilation is handled by [Nuitka](https://github.com/Nuitka/Nuitka/).


You can provide any .py file you like, PolyLock will then encrypt the file's data and then obfuscate it. You will then be asked if you want to compile the .py to an executable and if you say yes, you will be left with either an executable binary or a windows .exe file. Making sure your code is secure and obfuscated. You can also allow the ussage of github to store parts of the obfuscated code, keeping the final result small.

<br>
<br>

If you like what I have made, please leave a star! :star: and share this project with your friends and communities!
__ __
> Note: Loading/execution times may vary depending on how large the file is that's going to be obfuscated.


<br>
<br>

# Flowchart
![polylock_delta](https://github.com/user-attachments/assets/18eecb3d-44ed-44f5-9b5c-1bcc5be675ce)

> Dev note;
>
> This is my first time making a flow chart/diagram, It may not be pretty or the best but hopefully it's at the very minimum understandable.
__ __

<br>
<br>

# Updates
The full list of changes can be found in the [Changelog.md](https://github.com/therealOri/PolyLock/blob/main/CHANGELOG.md).

<br>

> 08/05/24

- Removed the check looking for `wget` tool from the command line & instead now using python wget.
- Created a windows specific lib `.pyd` instead of using a `.so` file. Importing on windows should be fixed and now compatible with windows systems.
- Changed random to use pycryptodome's randomness.
- Updated the tui to show the banner more consistently.
- Now using pydelta for obfuscation.

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

> Note: If you are using windows, you may need to delete or move the `polybin.so` file. If you are not using windows, you may need to delete or move the `polybin.pyd` file.
__ __

<br>
<br>

# Github fine-grained tokens
For this new version of polylock, because we are using github, you will need to make yourself a token. Below I will show you the steps you need to take to make the token and what scopes/permissions it should have.
> Note: __DO NOT SHARE YOUR ACCESS TOKENS WITH ANYONE.__

To get started you shall do the following;
- Go to your `user settings` and scroll down to `"Developer Settings"`, click it.
- Expand "Personal Access Tokens".
- Click "Fine-grained tokens".
- Click "generate new token".
- Give the token a name, an expiration date, and description.
- __Set "Repository Access" to "All Repositories".__
- Set the following `repository permissions` to "Read & Write" - (`Administrator, Contents`) [metadata is on by default]
  > `Account permissions` should NOT be touched. `Leave alone`.
- Click "Generate token" button and then copy the token and `save the token` somewhere secure/safe.
  > (You will need this to interact with the github api, make repositories, and update repositories.
__ __

<br>
<br>

# ToDo
Here you can find my plans on what I would like to do and or future ideas.
  - Add more layers. (Can never be TOO much like an onion.)
__ __

<br>
<br>

# ⚠️ Warning & disclaimer
If you have any issues that occur while using PolyLock, then by all means please make an [issue](https://github.com/therealOri/PolyLock/issues/new/choose) report!

Also! I shall not be held liable or be punishable on or off ANY platforms for what users do with this code and or what code they obfuscate, "lock", etc. This code was made for the intended purpose of keeping code personal, safe, and secure. Not really any different than normal file/data encryption.
__ __

<br />
<br />
<br />


# Support  |  Buy me a coffee <3
Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)

