def encode_list(string_list):
    encoded = []
    for i in string_list:
        encoded.append(i.encode('utf-8'))
    return encoded


def decode_list(bytes_list):
    decoded = []
    for i in bytes_list:
        decoded.append(i.decode('utf-8'))
    return decoded


def main():
    string_list = ["Hello World","Привет","Мир"]
    print(f'Изначальный список: {string_list}')
    encoded_list = encode_list(string_list)
    print(f'Список байт кодов: {encoded_list}')
    decoded_list = decode_list(encoded_list)
    print(f'Декодированный список: {decoded_list}')


if __name__ == "__main__":
    main()