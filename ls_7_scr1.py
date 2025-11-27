ask = input("Wright in format\"int1+int2=\":")
int1 = ""
s = ""
int2 = ""
print(ask)
k = 0
i = 0
while (k < 50) or (i < 50):
    if (ask[k] == "+") or (ask[k] == "-") or (ask[k] == "*") or (ask[k] == "/"):
        int1 = ask[0:k]
        s = ask[k]
        i = k
        if ask[k] == "=":
            print("check")
            int2 = ask[i+1:]
            print(int1, s, int2)
            break
        else:
            k+=1
    else:
        k+=1
print(int1, s, int2)
a = float(int1)
b = float(int2)
if s == "+":
    print(a+b)
elif s == "-":
    print(a-b)
elif s == "*":
    print(a*b)
else:
    print(a/b)