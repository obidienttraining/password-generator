import random
#random
#range
#input
#for
#while

password_generator = "QWERTYUIOPLKJHGFDSAZXCVBNM1234567890&%#@:?>()mnbvcdsaawretryuop"
123456789
def passwordgenerator():
    while 1:
        #allow user to enter password lenght
        password_len = int(input("Enter password Lenght:"))
        password_count = int(input("How many you to generate:"))
        # print(type(password_count))
        for x in range(0,password_count ):
            mypass = ""
           
            for x in range(0, password_len):
                passwordmain  = random.choice(password_generator)
                mypass    =     passwordmain + mypass
            print("hello this is my password",  mypass )


                
         
            

            
        



passwordgenerator()

# x = 0

# # print(x + 1 )

# while x < 6: #expression
#     print(x)
#     x +=1