tup=()
while True:
    test_str=input("enter your email address: ")
    username=test_str.split("@")[0]
    print(username)
    domainname=test_str.split("@")[1]
    print(domainname)
    choice=input("do you want to continue? y or n: ").lower()
    if choice=='y':
        continue
    else:
        break