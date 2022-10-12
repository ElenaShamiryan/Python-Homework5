with open('file.txt', 'w') as data:
    data.write('qqwwweeeerrrrrttttttyyyyyyy')

with open('file.txt', 'r') as data:
    string = data.readline()

def compress(text):
    count = 1
    result = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count = count + 1
        else:
            result = result + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        result = result + str(count) + text[-1]
    return result

def decompress(text):
    lst = ''
    result = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            lst = lst + text[i]
        else:
            result = result + text[i] * int(lst)
            lst = ''
    return result


with open('file.txt', 'r') as file:
    start_string = file.read()

with open('file_1.txt', 'w') as file:
    encoded_string = compress(start_string)
    file.write(encoded_string)

with open('file_1.txt', 'r') as file:
    start_string = file.read()

with open('file_2.txt', 'w') as file:
    start_string = decompress(encoded_string)
    file.write(start_string)

print(compress(string))
print(decompress(compress(string)))