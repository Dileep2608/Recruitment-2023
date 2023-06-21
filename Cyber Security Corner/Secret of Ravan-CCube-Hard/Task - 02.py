import pyzipper
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', ';', ':', '"', "'", '<', '>', '?', ',', '.', '/', '`', '~']
known_password_dict = {'n':1, '_':2, '^':3, '`':5, 'W':6, '5':8}
flag = 0
source = "The_secret.zip"
destination = "./The_secret_extracted_folder"
# As you can see, characters at 4th and 7th position are missing. You need to find those characters using brute-force.
password_list= list(known_password_dict.keys())
#Write your code here
for i in characters:
    for j in characters:
        password_list.insert(3,i)
        password_list.insert(6,j)
        password = ''.join(password_list)
        try:
            with pyzipper.AESZipFile(source) as zip_ref:
                zip_ref.extractall(destination, pwd=password.strip().encode())
        except RuntimeError:
            print("Wrong password:", password.strip())
            password_list.pop(3)
            password_list.pop(5)
            continue
        else:
            print("**** PASSWORD FOUND **** :", password.strip())
            flag = 1
            break
    if flag == 1:
        break
