#WAP to accept username and password from the user where the username and passwords are already stored in a dictionary format.

print("SECURE EMPLOYEE ACCOUNT SYSTEM")

accounts = {}
n = int(input("Enter number of accounts to create:"))

for i in range(n):
    username = input("Enter username:")

    while True:
        password = input("Enter password:")
        upper = lower = digit = special = False

        for ch in password:
                if ch.isupper():
                    upper = True
                elif ch.islower():
                    lower = True
                elif ch.isdigit():
                    digit = True
                elif ch == " ":
                    space = True
                else:
                    special = True

        if len(password) >= 8 and upper and lower and digit and special and " " not in password:
            break

        print("Password rejected!")
        if len(password) < 8:
            print("At least 8 characters required.")
            if not upper:
                print("At least one uppercase required.")
            if not lower:
                print("At least one lowercase required.")
            if not digit:
                print("At least one digit required.")
            if not special:
                print("At least one special character required.")
            if " " in password:
                print("Space not allowed.")

    while True:
        confirm = input("confirm password:")

        if confirm == password:
            accounts[username] = password
            print("account successfully created!")
            break
        else:
            print("Password do not match. please enter confirm password")


print("\nEMPLOYEE LOGIN")

for attempt in range(5):
     username = input("\nEnter username: ")
     password = input("Enter password: ")

     if username in accounts and accounts[username] == password:
          print("\nLogin successful!")
          print(f"\nWelcome {username}")
          break
     else:
         print("\nInvalid username or password.")
         remaining = 4-attempt
         if remaining > 0:
             print(f"Attempts remaining: {remaining}")

else:
       print("Access Denied!")
       print("Maximum login attempts exceeded.")







