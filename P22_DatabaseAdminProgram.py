print("Welcome to the Database Admin Program\n")

# database with username and password
log_on_information = {
    'mooman74':'alskes145',
    'meramo1986':'kehns010101',
    'nickyD':'world1star',
    'george2':'booo3oha',
    'admin00':'admin1234'
}

user = input("Enter your username: ")

if user in log_on_information.keys():
    password =  input("Enter your password: ")  # takes password only if username exists
    if password == log_on_information[user]:    # checks for correct password
        print(f"\nHello {user}! You are logged in!\n")
        
        if user == "admin00":   # for admin00 displays whole database
            print("Here is the current user database:")
            for i in log_on_information.keys():
                print(f"Username: {i}\tPassword: {log_on_information[i]}")
        else:
            ch = input("Would you like to change your password: ").lower()
            if ch == 'yes':
                new = input("What would you like your new password to be: ")
                if len(new)<8:
                    print(f"{new} not the minimum eight characters.\n")
                else:
                    log_on_information[user] = new
                print(f"\n{user} your password is {log_on_information[user]}")
    else:
        print("Password incorrect!")
else:
    print("Username not in database, goodbye.")
                    