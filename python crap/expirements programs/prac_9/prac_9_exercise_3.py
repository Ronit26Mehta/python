dic1={'a':100,'b':200,'c':300}
dic2={'a':300,'b':200,'d':400}
for key in dic2:
    if key in dic1:
      dic2[key]=dic2[key]+dic1[key]
    else:
        pass
print(dic2)
