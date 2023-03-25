#list of objec
#random
#range
#input
#for
#while

#entering the lenght of the paaasword  @#45redG
#enter how many password w= you wnat to generate  2
#@#45redG
#@#45redG

import random
uppercase = "QWERTYUIOPASDFGHJKL"
lowercase = "mnbvxcxzlkjhgfdsaqwertyuiop"
numbers =    "123567890"
symbols =  "!@#$%^&*()_+:>,.'[]"

all_seq = uppercase + lowercase + numbers + symbols

print(all_seq)

def password_gen():
    while 1:
        password_lenght = int(input("Enter password lenght: "))
        password_numbers = int(input("enter numbers of password: "))
        for x in range(password_numbers):
           mypassword = ""
           for x in range(password_lenght):
               password_random =  random.choice(all_seq)
               mypassword   =  mypassword + password_random
           print("hello password geenerated is: ", mypassword)
   
               
              
               
               
              
       
           
        
    


password_gen()

