conv=[]
def farTocel():
    temp=int(input("Enter Temp in Farenheit"))
    ans=((temp-32)*5/9)
    ans=round(ans,2)
    print(ans)
    conv.append((temp,ans))

def celTofar():
    temp=int(input("Enter Temp in Celsius"))
    ans=(temp*9/5)+32
    ans=round(ans,2)
    print(ans)
    conv.append((temp,ans))

def celTokev():
    temp=int(input("Enter Temp in Celsius"))
    ans=temp+273.15
    ans=round(ans,2)
    print(ans)
    conv.append((temp,ans))

def kevTocel():
    temp=int(input("Enter Temp in Kelvin"))
    ans=temp-273.15
    ans=round(ans,2)
    print(ans)
    conv.append((temp,ans))

def farTokev():
    temp=int(input("Enter Temp in Farenheit"))
    ans=((temp-32)*5/9)+273.15
    ans=round(ans,2)
    print(ans)
    conv.append((temp,ans))


def kevTofar():
    temp=int(input("Enter Temp in Kelvin"))
    ans=(((temp-273.15)*9/5)+32)
    ans=round(ans,2)
    print(ans)
    conv.append((temp,ans))

c = "y"
tup = (
    (1, "farenheit", "celcius"),
    (2, "celsius", "farenheit"),
    (3, "celcius", "kelvin"),
    (4, "kelvin", "celsius"),
    (5, "farenheit", "kelvin"),
    (6, "kelvin", "farenheit"),
    (7, "show tuple"),
)


while True:
    print(tup)
    ch = int(input("Enter choice: "))
    if ch == 1:
        farTocel()
    elif ch == 2:
        celTofar()
    elif ch == 3:
        celTokev()
    elif ch == 4:
        kevTocel()
    elif ch == 5:
        farTokev()
    elif ch == 6:
        kevTofar()
    elif ch == 7:
        print(conv)
    else:
        print("wrong option")

    c = input("Continue? (y/n)")
    if c == "n":
        break