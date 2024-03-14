def panduankuohao(input_array):  # 寻找最内层的括号内容
    openning = 0
    closing = 0
    for i in range(len(input_array)):
        if input_array[i] == "(":
            openning = i
        elif input_array[i] == ")":
            closing = i
            break
    return openning, closing


def panduanneibu(input_array):  # 判断最内层的括号中是否well formed
    if input_array[0] == "¬":
        if len(input_array) == 2 and input_array[1].isalpha:
            return True
        else:
            return False
    elif input_array[0].isalpha():
        if len(input_array) == 3 and (input_array[1] in ['∧', '∨', '→', '↔']) and input_array[2].isalpha():
            return True
        else:
            return False
    else:
        return False

def panduankuohaonumber(input_array):   #判断括号数目是否正确
    jishu = 0
    for i in input_array:
        if i == "(":
            jishu += 1
        elif i == ")":
            jishu -= 1
    if jishu==0:
        return True
    else:
        return False

def tidai(i,j,input_array): #将已经判断了的部分变成一个字母
        input_array=input_array[0:i]+["a"]+input_array[j+1:]
        return input_array

def number(input_array):  #通过左括号个数判断需要循环几次
    n1=0
    n2=0
    for i in input_array:
        if i=="(":
            n1+=1
        elif i==")":
            n2+=1
    return n1,n2

input_string=input("请输入逻辑命题：")
input_array=[char for char in input_string]
n1,n2=number(input_array)
input_array1=input_array
flag=True
while n1>0:
    i,j=panduankuohao(input_array)
    if n1*n2!=0:
        x=input_array[i+1:j]
        flag=panduanneibu(x)
        if flag:
            input_array=tidai(i, j, input_array)
        else:
            break
    else:
        flag=False
        break
    n1-=1
flag2=True
if len(input_array)!=1:
    flag2=False
if flag and panduankuohaonumber(input_array1) and flag2:
    print("是良好命题")
else:
    print("不是良好命题")





