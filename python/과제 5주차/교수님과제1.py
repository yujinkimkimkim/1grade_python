values=["1.33","","5.03"]
for i in values:
    try:
        print(float(i))
        print("정확한 데이터입니다.")
        print("변환을 완료했습니다.")
    except:
        print("0")
        print("데이터 값이 잘못되었습니다.")
        print("변환을 완료했습니다.")