# PolyLock Updates & Changes

<br>
<br>
<br>


> 09/12/23
- Added a windows compatibility patch for the `compile_code()` function.
- Removed option for whether or not to add an icon to the compiled executable.
__ __

<br>
<br>

> 08/24/23
- Re-worked the handling of the encrypted data so it will be stored locally, instead of having to trust the security of another platform. This will also allow you to use larger files like 100kb+ for example, and not be impacted by slow compile times or slow obfuscation times. (hopefully)
- Changed the obfuscation method from Hyperion to Specter.
- Encrypted file data will now be written to a `part.py` file to which it will be cythonized. (basically a shareable library file). 
__ __

<br>
<br>

> 08/06/23
- In the event of polylock not being able to make a request to pastebin, it will default to writing to local file instead.
- Added a spinner to take up empty space when validating pastebin user keys. (To give you something to look at...like a loading bar, etc.)
- Added a banner/logo when the script is ran/started.
- Fixed a bug where the checking of the file you want to encrypt and obfuscate to see if it exists and ends with ".py" wasn't working. It now works.
__ __

<br>
<br>

> 08/01/23
- Added more logic for handling user keys and adding more if checks. Basically just handling what would happen if request.status_code's happen to be anything other than 200 and polylock is unable to make a successful request.
- Implemented api_user_key validation to check and see if the key given is valid and if it isn't, allow the user to make a key/new key. And if the user can't make a new key or log in to pastebin, polylock will just post/paste as guest.
__ __

<br>
<br>

> 07/30/23
- New way of handling the storage of the encrypted and obfuscated code data. You can now use pastebin to store the data and read from when executing. This will make the final result Waaaaaaaaayyyyyyyy smaller and faster to compile. Or you can stick with not using pastebin and keep everything in one file, but with the new method of using a list to store the data, as to prevent strings from being to big and to hopefully reduce the ammount of recursion...however the downside is the bigger the list, the more memory it will need to use. (That's why I added the use of pastebin)
> You can also choose to use your own account or just post to pastebin as a guest. There are upload limits on accounts per 24hrs so try not to upload and save to pastebin to frequently per day. "`Guests` can create up to `10` new pastes per `24 hours`, `Free` members can create up to `20` new pastes per `24 hours`, and `PRO` members can create up to `250` new pastes per `24 hours`."
__ __
