def f(num):
    new_num = ''
    while num > 0:
        new_num = str(num % 4) + new_num
        num //= 4
    return new_num

for i in range(1, 1000000):
    string = "0" + f(i)

    while('01' in string) or ('02' in string) or ('03' in string):
        if '01' in string:
            string = string.replace('01', '30', 1)
        elif '02' in string:
            string = string.replace('02', '101', 1)
        elif '03' in string:
            string = string.replace('03', '202', 1)

    if string.count('1') == 15 and string.count('2') == 10 and string.count('3') == 60:
        print(f(i).count('1'))
        break
print('ok')