#* XOR шифрование/расшифрование. На входе файл с текстом и ключ шифрования (строка), 
# на выходе преобразованное (зашифрованное/расшифрованное) сообщение в файле.


key = 'verylongkey'

    
def cipher_encrypt(_text, _key):
    encripted_str = ""
    j = 0
    key_length = len(key)
    for symbol in _text:
        encripted_str += chr(ord(symbol) ^ ord(_key[j]))
        j += 1
        j = j % key_length
    return  encripted_str 

with open('task3input.txt', 'r') as input:
    text  = input.read()

encrypted_text = cipher_encrypt(text,key)
decrypted_text = cipher_encrypt(encrypted_text,key)

with open('task3output.txt', 'w', encoding='utf-8') as output:
    output.write(f'Зашифрованный текст: {encrypted_text}\nРасшифрованный текст: {decrypted_text}')