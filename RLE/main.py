# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def get_list(some_str) -> list:
    symbol_list = [some_str[0]]
    for i in range (1, len(some_str)):
        if some_str[i] != some_str[i - 1]:
            symbol_list.append(some_str[i])
    return symbol_list

def symbol_count(some_str) -> list:
    count_list = []
    symbol = some_str[0]
    count = 0
    for i in range (len(some_str)):
        if some_str[i] == symbol:
            count += 1
        else:
            count_list.append(count)
            symbol == some_str[i]
            count = 1
    return count_list

def rle_code(list_symbol, list_count):
    rle_str = ''
    list_count_str = list(map(str, list_count))
    for i in range(len(list_count_str)):
        rle_str += list_count_str[i] + list_symbol[i]
    return rle_str

def rle_decode(some_str):
    num_list = []
    symbol_list = []
    index_to_start = 0
    for i in range(len(some_str)):
        if some_str.isalpha():
            symbol_list.append(some_str[i])
            num_list.append(some_str[index_to_start:i])
            index_to_start = i + 1
        
    list_number = list(map(int, num_list))
    decode_str = ''
    for i in range(len(symbol_list)):
        for _ in range(list_number[i]):
            decode_str += symbol_list[i]
    return decode_str

with open ('codefile.txt', 'r') as file:
    my_str = str(file.read())
print(my_str)

my_symbol_list = get_list(my_str)
print(my_symbol_list)

my_count_list = symbol_count(my_str)
print(my_count_list)

rle_str = rle_code(my_symbol_list, my_count_list)
print(rle_str)

decode_rle = rle_decode(rle_str)
print(decode_rle)

with open('decode.txt', 'w') as file:
    file.write(decode_rle)

