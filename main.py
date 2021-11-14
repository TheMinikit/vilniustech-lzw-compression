
ascii_table_file = open("ascii_table.txt", encoding="utf-8")
symbol_table = {}

symbol_table[' '] = 32

for line in ascii_table_file:
    symbol_table[line.rstrip().split('\t')[1]] = line.rstrip().split('\t')[0]

string_to_compress = "WYS*WYGWYS*WYSWYSG"
compressed_string = ""
counter = 256
operation_str = string_to_compress[0]
skip = 0

for i in range(len(string_to_compress) - 1):
    print("i: " + string_to_compress[i])
    if skip > 0:
        print("skipped: " + string_to_compress[i])
        skip = skip - 1
        operation_str = string_to_compress[i + 1]
        continue
    elif operation_str in symbol_table.keys():
        c = 1
        while operation_str in symbol_table.keys():
            operation_str = operation_str + string_to_compress[i + c]
            c = c + 1

        print(operation_str)
        symbol_table[operation_str] = counter
        skip = len(operation_str) - 2
        print("skip: " + str(skip))
        counter = counter + 1
        compressed_string = compressed_string + str(symbol_table[operation_str[:-1]]) + " "
        operation_str = string_to_compress[i + 1]

compressed_string = compressed_string + str(symbol_table[operation_str])

print()
print()
print()

for key in symbol_table.keys():
    print(str(key) + " " + str(symbol_table[key]))

print()
print()
print()

print(compressed_string)
