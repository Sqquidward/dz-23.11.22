string = "1" + ('9' * 98)

while('19' in string) or ('299' in string) or ('3999' in string):
    if '19' in string:
        string = string.replace('19', '2', 1)
    elif '299' in string:
        string = string.replace('299', '3', 1)
    elif '3999' in string:
        string = string.replace('3999', '1', 1)
print(string)