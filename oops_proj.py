class chatbook:
    def __init__(self):
        self.username= ''
        self.password=''
        self.loggedin=False
        # self.menu()


    def menu(self):
        user_input=input("""Welcome to Chatbook!! How would you like to proceed?
                         1. Press 1 to signup
                         2. Press 2 to signin
                         3. Press 3 to write a post
                         4. Press 4 to message a friend
                         5. Press any other key to exit""")
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email=input("Enter Your Email Here -->")
        pwd=input(" Setup Your Password Here -->")
        self.username=email
        self.password=pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please Signup first by pressing 1 in the main menu")
        else:
            uname=input("Enter Your Email/Username here -->")
            pswd=input("Enter Your Password Here -->")
            if self.username==uname and self.password==pswd:
                print("You have signed in successfully !!")
                self.loggedin=True
            else:
                print("Please input correct credentials..")
        print('\n')
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt=input("Enter Your Message here-->")
            print(f"Following content has been posted --> {txt}")
        else:
            print("You Need to signin first to post something...")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            txt=input("Enter your Message Here-->")
            frnd=input("Whom to send the message?--->")
            print(f"Your mesage has been sent to {frnd}")
        else:
            print("You Need to signin first")
        print('\n')
        self.menu()

obj=chatbook()

    
    
        