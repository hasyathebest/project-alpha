alpha=input ("enter anything and this machine will tell you if it is a alphabet or not")
if alpha==str:
    h=3
elif alpha==float:
    h=4
elif alpha==int:
    h=5

if h==3:
    print("that is a string number not a decimal muber or even a normal number")
elif h==4:
    print("that is a decimal number")
elif h==5:
    print("that is a normal number")