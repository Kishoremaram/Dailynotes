# remove the digits in string
def removedigit(str1):
    num={"0","1","2","3","4","5","6","7","8","9"}
    str2=""
    for i in str1:
        if i not in num:
            str2=str2+i
    print("string:",str2)
    return str2
