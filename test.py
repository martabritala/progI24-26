# print("Sveiki!")

# mainigais = "Sveiki!"

# cits = 5 
# print(cits)
# cits = cits + 6

# print(mainigais, cits)

# # ievade = int(input("Ievadiet skaitli! : "))
# # print(ievade)
# # lielaks = ievade + 1
# # print("Skaitlis, kas par 1 lielāks :", lielaks, ievade + 1)

# print(6==1)

# number = int(input("Give me a number!: "))

# if(number>=20):
#     print("Big")
# elif(number<5):
#     print("Small")
# elif(number>10 and number<20):
#     print("Medium")
# else:
#     print("Normal")

def calculate(num1, num2):
    reiz = num1*num2
    if(reiz<=20):
        return reiz
    return num1+num2

for i in range(-2,10,3): # range (sākums, beigas(neieskaitot), solis)
    print(calculate(3,i))

print("-----=-----------")

for i in [4,8,12,2,0]:
    print(calculate(3,i))



answ = "y"
while(answ == "y"):
    sk1 = int(input("Pirmais: "))
    sk2 = int(input("Otrais: "))
    print(calculate(sk1,sk2))
    answ = input("Vai vēlaties turpināt? (ievadiet 'y'): ")

