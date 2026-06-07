import random
import string

passwords={}

#load password text file
try:
    with open("1_password.txt",'r') as file:
        for line in file:
            website,pwd=line.strip().split(":")
            passwords[website]=pwd

except:
    pass

def generate_password():
    char=string.ascii_letters+string.digits+"!@#$%^&*_+"
    passwords="".join(random.choice(char) for _ in range(8) )
    return passwords
while True:
    print("\n----- Personal Password Management-----")
    print("1. Save Password ")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    choice=input("Enter Your Choice:")
    
    #save password
    if choice=="1":
        name=(input("Enter Your Name: "))
        pwd=(input("Enter Your Password: "))

        passwords[name]=pwd
        with open("1_password.txt","a") as file:
            file.write(f"{name}:{pwd}\n ")
            print("Saved...!!!")
    #view password
    elif choice=="2":
        if not passwords:
            print("No Data Found....!!!")
        else:
            for name,pwd in passwords.items():
                print(name ,":", pwd)
    #Generate password
    elif choice=="3":
        print("Generated Passwords:",generate_password())
    elif choice=="4":
        print("Thank you....!!!")
        break
    else:
        print("Invaild-input")




