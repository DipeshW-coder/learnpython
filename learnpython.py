# print function 

print("Dipesh is best at earning money he is the richest in the room and he is the best at everything he does")

# VARIABLES   "yeh joh variables hai isko dabba samajh woh dabbe me saman rkha hai toh agar dabbe ko hilaya toh saman khud hi hilta hai yehi hota hai variables me bhi"
# Variables are used to store data values

name = "Harsha"
print(name) 


 # yaha par apne ko "" dalne ki jarurat nahi hai kyuki yaha par name variable hai jo ki string hai aur upar wale print me meko kuch print karwana hai isliye "" dalna hai


name_1 = "kushal"
print("meet " + name_1 + " he is son of " + name)

# yaha par + ka use kiya hai kyuki yaha par name_1 variable hai jo ki string hai aur upar wale print me meko kuch print karwana hai isliye + ka use kiya hai
# joh likhna hai joh variable nahi hai usko "" isme dalna hai aur joh variable hai usko direct likhna hai + dalke

name_2 = "Dipesh" #string
age = 17 #integer
height = 5.7 #float
is_very_clever = True #boolean

# convert all the variables into string
# to convert the variables into string we use str() function

print("this is "+name_2+ " he is " +str(age)+ " years old and his height is " +str(height)+ " and he is very smart " + str(is_very_clever))
# abhi upr joh hai agar maine str() function nahi lagaya toh woh error dega kyuki age aur height integer hai toh woh string me nahi aa payega toh isliye str() function lagana padta hai
# str lagane ke baad hi chalega proceed hoga 
# yeh sab kuch print karne ke liye hai

# taking user input 

name_4 = input("enter your name: ")
print("God bless you " + name_4)

# yaha par ham input le rhe hai joh input krega kuch matlab maine wahah dipesh dala toh input kiya maine neeche dipesh dikhayega fir 
#input function me str() dalne ki jarurat nahi hai kyuki woh khud hi string me le lega toh isliye str() nahi lagana hai
# BASIC ARITHMATIC CONCEPTS

a = 23
b = 46

print(a+b) # addition 
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # division 
print(a//b) # floor division (remove decimal)
print(a%b) # modulus 
print(a**b) # exponentiation



# string me convert krna hota hai agar koi bhii number ko toh ham str() use krte hai 
# agar koi string to number me use krna hota hai toh ham int() use krte hai 
# ABHI neeche joh umar wala section hai usme theyre asking age so mai number dalunga agar int() use nhi kiya toh fir error dega 


#IF-ELSE STATEMENT
umar = int(input("enter your age: "))
if umar >+ 18:
    print("you are old enough to earn money on your own! Get your ass up and go to earn!")

else:
    print("khelne kudne ka time hai enjoy birooooo")    


# FOR LOOP

for i in range(23):
    print("Dipesh is great")

# WHILE LOOP
# while loop jo hai woh true ke basis pe chalta hai jabtak woh value true hai tabtak woh print karta hai

j = 1
while j <= 5 :
    print(j)
    j += 1

print ("ab next hai while loop")

#How It Works:
#The loop starts with i = 1.
#It checks if i <= 5. If True, it executes the block inside the loop.
#print(i) prints the current value of i.
#i += 1 increases i by 1.
# The loop repeats until i becomes 6, at which point the condition i <= 5 becomes False, and the loop stops.

k = 1
while k <= 10:
    print(k)
    k += 1
    if k == 3:
        break

count = 0
while count < 3:
    print("Count:", count)
    count += 1

# LISTS

fruits = ["banana", "mango", "apple"]
print(fruits[0]) # yeh fruits ke iske 1st wale ko print krega 
print(fruits[1]) # yeh fruits ke iske 2nd wale ko print krega 

fruits.append("cherry") #this will add cherry to the list
fruits.remove("banana") #this will remove banana from the list
print(fruits)


# TUPLES 
numbers = (1, 2, 3, 4, 5)
print(numbers[3]) # yeh numbers ke isme 4th wale ko print krega  dhyaan se yeh 4th TAK nahi 4TH KO print krega

# DICTIONARIES 

student = {
    
    "name": "Dipesh",
    "age": 17,
    "is_clever": True
}
print(student["name"]) # yeh student ke name ko print krega
print(student["age"]) # yeh student ke age ko print krega
print(student["is_clever"]) # yeh student ke is_clever ko print

# .get
print(student.get("age")) # yeh student ke name ko print krega yaha par .get ko ko isliye use kiya hai kyuki agar age nahi hota toh error aata but abhi .get hai toh error nahi ayega agar age nhi bhi ho toh woh none print karega


