list1 = list(map(int, input("Enter numbers separated by space: ").split()))
list2 = list(map(int, input("Enter numbers separated by space: ").split()))
while(1):
        print(" *** menu***")
        print(" 1.length")
        print(" 2. concatenation")
        print(" 3. repetition")
        print(" 4.in")
        print(" 5.not in")
        print(" 6.maximum")
        print(" 7.minimum")
        print(" 8.sum of elements")
        print(" 9.all ")
        print(" 10. any operator")
        print(" 11.exit")
        ch=int(input("enter your choice:"))
        if (ch==1):
               print("length of the lists",len(list1),len(list2))
        elif(ch==2):
               print("concatenation",list1+list2)   
        elif(ch==3):
            n=int(input("enter the no of times you want the list to repeat:"))
            print("repetition of list 1 and list 2:",list1*n,list2*n)
        elif(ch==4):
            element=int(input("enter element to find in a list :"))
            if element in list1:
                print("element is present in the list")
            else:
                print("element is not present in the list ")
        elif(ch==5):
            element=int(input("enter element to find in a list :"))
            if element not in list1:
                print("element is  not present in the list ")
            else:
                print("element is present in the list")
        elif(ch==6):
            print("max",max(list1),max(list2))
        elif(ch==7):
            print("min",min(list1),min(list2))
        elif(ch==8):
            print("sum",sum(list1),sum(list2))
        elif ch == 9:
            print("All elements non-zero in list1?", all(list1))
            print("All elements non-zero in list2?", all(list2))

        elif ch == 10:
            print("Any non-zero element in list1?", any(list1))
            print("Any non-zero element in list2?", any(list2))

        elif ch == 11:
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again!")             
        print(list1)
        print(list2)


    
    

    


