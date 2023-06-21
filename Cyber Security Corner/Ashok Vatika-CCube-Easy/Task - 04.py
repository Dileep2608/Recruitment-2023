encrypted_txt = "|OP`Z<E]|Y\$"
key = "Jai Shree Ram!"

# Your code goes here

def decrypt(encrypted_txt,key):
    encrypted_code = []
    key_code = []
    ans = ""
    for i in range(len(encrypted_txt)):
        encrypted_code.append(ord(encrypted_txt[i]))
    for i in range(len(key)):
        key_code.append(ord(key[i]))

    for i in range(min(len(encrypted_code), len(key_code))):
        ans += chr(encrypted_code[i]^key_code[i])
    return ans

answer = decrypt(encrypted_txt,key)
with open("location_coordinates.txt", "w") as file:
    file.write(answer)
