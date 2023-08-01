# About
PolyLock is a python3 code obfuscator and encryptor, helping you keep your code secure/safe and still runable/executable.


- Encryption is handled with [chaeslib](https://pypi.org/project/Chaeslib/)

- Obfscation is handled by my fork of [hyperion](https://github.com/therealOri/Hyperion/)

- Code compilation is handled by [nuitka](https://github.com/Nuitka/Nuitka/).


You can provide any .py file you like, PolyLock will then encrypt the file's data and then obfuscate it. You will then be asked if you want to compile the .py to an executable and if you say yes, you will be left with either a linux executable binary, a windows .exe, or whatever you get on Mac OS. Making sure your code is secure and obfuscated. You can also allow the ussage of pastebin to store the encrypted and obfuscated code, keeping the final result small. (less than 25 lines)

If you like what I have made, please feel free to leave a star! :star:
__ __

<br>
<br>

# Flowchart
![PolyLock_diagram_flowchart](https://github.com/therealOri/PolyLock/assets/45724082/25e3dd48-3056-41fb-a88b-016e0f3a5829)
> Dev note;
>
> This is my first time making a flow chart/diagram, It may not be pretty or the best but hopefully it's at the very minimum understandable.
__ __

<br>
<br>

# Updates
> 07/30/23

Updated:
- New way of handling the storage of the encrypted and obfuscated code data. You can now use pastebin to store the data and read from when executing. This will make the final result Waaaaaaaaayyyyyyyy smaller and faster to compile. Or you can stick with not using pastebin and keep everything in one file, but with the new method of using a list to store the data, as to prevent strings from being to big and to hopefully reduce the ammount of recursion...however the downside is the bigger the list, the more memory it will need to use. (That's why I added the use of pastebin)
> You can also choose to use your own account or just post to pastebin as a guest. There are upload limits on accounts per 24hrs so try not to upload and save to pastebin to frequently per day. "`Guests` can create up to `10` new pastes per `24 hours`, `Free` members can create up to `20` new pastes per `24 hours`, and `PRO` members can create up to `250` new pastes per `24 hours`."
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

# ⚠️ Warning & disclaimer
I have not tested ANY of the code on a windows system so I have no idea what works and what doesn't..(yet). If you are using windows then please feel free to test it out and get back to me with any issues that occur by making an [issue](https://github.com/therealOri/PolyLock/issues/new/choose) report. Please and thanks!

I shall not be held liable or be punishable on or off platforms for what users do with this code and or what code they obfuscate, etc. This code was made for the intended purpose of keeping code personal, safe, and secure. Not really any different than normal file/data encryption.
__ __

<br />
<br />
<br />


# Support  |  Buy me a coffee <3
Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)

