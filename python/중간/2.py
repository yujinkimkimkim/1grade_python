text = list(input('문자를 입력해주세요 >> '))
print(text)
new_text = []

for i in range(len(text)):
    if ( ord(text[i])>=65 and ord(text[i])<=90 ):
        new_text.append(chr(91-ord(text[i])+64)) # 그 범위에서 제일 큰 값보다 1 큰 값 - (입력받은 값 - 범위에서 제일 작은 값에서 1 뺀 값)

    elif ( ord(text[i])>=97 and ord(text[i])<=122 ):
        new_text.append(chr(123-ord(text[i])+96))

    elif ( ord(text[i])>=48 and ord(text[i])<=57 ):
        new_text.append(chr(58-ord(text[i])+47))

    else:
        print('입력은 알파벳과 숫자로만 입력하세요!!')

print(new_text)
