color=['magenta' , 'green' , 'yello']
for c in color:
    print c
temp=eval(raw_input("enter temperature"))
while true:
  if temp>31 and temp<35:
     print'sunny day'
     break
  elif temp>35 and temp<40:
       print'warm day'
       break
  elif temp>40 and temp<50:
        print 'high temp'
        break
  else:
     print'invalid'
     break

    
    
    
