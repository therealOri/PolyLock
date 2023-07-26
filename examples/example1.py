import os
import pwd



def clear():
	os.system("clear||cls")





def main(msg="Hello World!"):
	message = ""
	punctuation = ['!', ' ', '"', '#' '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
	for char in msg:
		if char in punctuation:
			message += char
		else:
			for name in pwd.getpwall():
				if char.upper() in name.pw_name.replace(" ","").upper():
					message += char
					break
	return message









if __name__ == '__main__':
	clear()
	message = main(msg="I love trains, they are so cool.")
	print(message)
