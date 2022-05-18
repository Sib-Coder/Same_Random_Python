import base64


def encode(secret_string):
    bytes_string = secret_string.encode('ascii')
    code_string = base64.b64encode(bytes_string)
    secret_string_out = code_string.decode('ascii')
    print(f"Encode string is: {secret_string_out} ")


def decode(secret_string):
    bytes_string_out = secret_string.encode('ascii')
    code_string_out = base64.b64decode(bytes_string_out)
    secret_string_out = code_string_out.decode('ascii')
    print(f"Decode string is: {secret_string_out}")


def main():
    user_string = input("Your string is: ")
    action = input("write what you want to do - encode or decode:  ")
    if (action == 'encode'):
        encode(user_string)
    elif (action == 'decode'):
        decode(user_string)
    else:
        print("wrong action !!!")

if __name__ == '__main__':
    main()
