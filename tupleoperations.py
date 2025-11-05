
tuple1 = tuple(map(int, input("Enter elements of tuple1 separated by space: ").split()))
tuple2 = tuple(map(int, input("Enter elements of tuple2 separated by space: ").split()))
while 1:
    print("Menu:")
    print("1. Length of tuples")
    print("2. Concatenation")
    print("3. Minimum element")
    print("4. Maximum element")
    print("5. Sum of elements")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Length of tuple1:", len(tuple1))
        print("Length of tuple2:", len(tuple2))
    elif choice == 2:
        print("Concatenation of both tuples:", tuple1 + tuple2)
    elif choice == 3:
        print("Minimum element of tuple 1:", min(tuple1))
        print("Minimum  of tuple 2:",min(tuple2))        
    elif choice == 4:
        print("Maximum element of tuple 1:", max(tuple1))
        print("Maximum element of tuple2:",max(tuple2))        
    elif choice == 5:
        print("Sum  of tuple 1 :", sum(tuple1))
        print("sum of tuple 2 :",sum(tuple2))       
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
