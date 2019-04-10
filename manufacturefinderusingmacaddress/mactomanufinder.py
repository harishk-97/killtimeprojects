print("please enter the full or hex mac address to find its manufacturer:")
a=input().split('-')
b=''
for i in range(3):
    if i==0:
        b+=a[i]
    else:
        b+='-'
        b+=a[i]
flag=0
for num,line in enumerate(open('macmanufacturer.txt')):
    if b in line:
        print(line)
        flag=1
    if(flag>1 and flag<=5):
        print(line,end='\n')
        flag+=1
    elif(flag==6):
        break
    elif(flag==1):
        flag+=1
if(flag==0):
    print("macmanufacturer.txt file maybe missing\nTry to add it in the folder where this code is present.\nFor help,contact me at masterkid1711@gmail.com")
