n=1 #this is the initial variable
while n != 4  :
        print "1.Read \
               2. Write \
               3. Update \
               4. Exit"
        n=int(raw_input("enter choice"))
        
        if n == 1:
            print "read"
        elif n==2:
            print "write"
        elif n==3:
            print "update"
        elif n == 4 :
            pass
        else:
            print "invalid option"
else :
        print("Exited")
