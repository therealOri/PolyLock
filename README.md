# About
PolyLock is a new and advanced python3 code obfuscator and encryptor, helping you keep your code secure/safe and still runable/executable.


- Encryption is handled with [Chaeslib](https://pypi.org/project/Chaeslib/)

- Obfscation is handled by my fork of [Specter](https://github.com/therealOri/Specter/)

- Code compilation is handled by [Nuitka](https://github.com/Nuitka/Nuitka/).


You can provide any .py file you like, PolyLock will then encrypt the file's data and then obfuscate it. You will then be asked if you want to compile the .py to an executable and if you say yes, you will be left with either an executable binary or a windows .exe file. Making sure your code is secure and obfuscated. You can also allow the ussage of github to store parts of the obfuscated code, keeping the final result small.

<br>
<br>

If you like what I have made, please leave a star! :star: and share this project with your friends and communities!
__ __
> Note: Loading/execution times may vary depending on how large the file is that's going to be obfuscated. And Specter sometimes likes to spit out an error and nor run properly so you may need to re obfuscate/try again if this happens.


<br>
<br>

# Flowchart
![PolyLock_New_flowchart](https://github.com/therealOri/PolyLock/assets/45724082/15d3772f-0fa0-4feb-a6e9-d267623b7658)

> Dev note;
>
> This is my first time making a flow chart/diagram, It may not be pretty or the best but hopefully it's at the very minimum understandable.
__ __

<br>
<br>

# Updates
The full list of changes can be found in the [Changelog.md](https://github.com/therealOri/PolyLock/blob/main/CHANGELOG.md).

<br>

(Latest - p2)
> 04/24/24

Updated polybin to have more layers. Also updated the example files and main file accordingly to work with this update.
__ __

<br>

(Latest - p1)
> 02/24/24

In this update We fully move away from pastebin (and their small file size limit restrictions), and instead move the storage of some code to github. With these changes you will now be able to have it make a repository for you or provide a link/url to a repository instead so it can save files to it and later on use. To do this, you will need to make a [fine-grained github access token](https://github.com/therealOri/PolyLock?tab=readme-ov-file#github-fine-grained-tokens), as that is what will make all of this possible. You will also need to have `curl` and `wget` installed. In regards to everything else in the code, it's pretty much the same in terms of flow and what not.

Changes;
- Moved from pastebin to github/git.
- Added another layer of fun to the final file/result using 'polybin'. I'm sure a laugh or two to will be had.
- Removed the use of setup.py and the "part" files. So now everything is in one file instead of multiple files.
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

<br>

Also, `Specter` can be used by itself if you want to use it instead of polylock, but let it be known that it is for obfuscation and does not aim to be both encryption and obfuscation, etc. It also doesn't really like to handle large files (anything over 70kb-80kb in file size).
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

