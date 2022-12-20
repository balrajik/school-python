def encrypt(text,key):
    encrypt_hex = ''
    key_iteration = 0
    for i in range(len(text)):
        tmp = ord(text[i]) ^ ord(key[key_iteration])
        encrypt_hex += hex(tmp)[2:].zfill(2)
        key_iteration +=1
        if key_iteration >= len(key):
            key_iteration = 0
    with open('n3/Output.txt','w') as file:
        file.write(encrypt_hex)


def decrypt(encrypted_text,key):
    hex_to_uni = ''
    for i in range(0,len(encrypted_text),2):
        hex_to_uni += bytes.fromhex(encrypted_text[i:i+2]).decode('utf-8')

    decrypt_text = ""
    key_iteration = 0
    for i in range(len(hex_to_uni)):
        tmp = ord(hex_to_uni[i]) ^ ord(key[key_iteration])
        decrypt_text += chr(tmp)
        key_iteration +=1
        if key_iteration >= len(key):
            key_iteration = 0
    with open('n3/Output.txt','w') as file:
        file.write(decrypt_text)


def main():
    while True:
        with open('n3/Input.txt','r') as file:
                text = file.read()
        choose = input("1 - зашифровать\n2 - расшифровать\n3 - выход\nВвод: ") 
        if choose == '1':
            key = input("Введите ключ шифрования: ")
            encrypt(text,key)
        elif choose == '2':
            key = input("Введите ключ шифрования: ")
            decrypt(text,key)
        elif choose == '3':
            break
        else:
            print("Неверный ввод")
            


if __name__ == '__main__':
    main()
