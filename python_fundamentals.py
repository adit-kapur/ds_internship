import math
import re 



# q1
user_input=input("Q1. Enter no. of rows and colums in the form x,y: ")
row,col=user_input.split(",")
row=int(row)
col=int(col)
a=[]
for i in range(row):
    b=[]
    for j in range(col):
        b.append(i*j)
    a.append(b)

print(a)



#q2
user_inp=input("Q2. Enter comma separated sequence of words: ")
lists=user_inp.split(",")
lists.sort(key=str.casefold)
print(",".join(lists))



#q3
user_inp=input("Q3. Enter a sequence of whitespace separated words: ")
list1=user_inp.split(" ")
list2=[]
for val in list1:
    if val not in list2:
        list2.append(val)
list2.sort()
print(" ".join(list2))
print()



#q4
items = []
print("Q4.",end=" ")
for i in range(1000, 3001):
    s = str(i)
    for j in range(len(s)):
        if int(s[j]) % 2 != 0:
            break
    else:
        items.append(s)           

print(", ".join(items)) 



#q5
string=input("Q5. Enter the sentence: ")
letters=0
num=0
for i in string:
    if i.isalnum():
        if i.isalpha():
            letters+=1
        else:
            num+=1
print(f"LETTERS {letters}")
print()
print(f"DIGITS {num}")



#q6
string=input("Q6. Enter the sentence: ")
upper=0
lower=0
for i in string:
    if i.isalpha():
        if i.isupper():
            upper+=1
        else:
            lower+=1
print(f"UPPER CASE {upper}")
print()
print(f"LOWER CASE {lower}")



#q7
print("Q7.",end=" ")
amount = 0
while True:
    user_inp = input("Enter transaction: ")
    if user_inp == "" :
        break
    else:
        lists = user_inp.split(" ")
        if lists[0].casefold() == "d":
            amount += int(lists[1])
        elif lists[0].casefold() == "w":
            amount -= int(lists[1])

print(amount)



#q8
passwords = input("Q8. Type in: ")
passwords = passwords.split(",")

accepted_pass = []
for s in passwords:
    l, u, special, d = 0, 0, 0, 0
    if (6 <= len(s) <=12):
        for i in s: 
            if (i.islower()):
                l+=1           
            if (i.isupper()):
                u+=1         
            if (i.isdigit()):
                d+=1           
            if(i=='@'or i=='$' or i=='#'):
                special += 1     
                 
    if (l>=1 and u>=1 and special>=1 and d>=1):
        accepted_pass.append(s)

print(",".join(accepted_pass))



#q9
user_inp = input("Q9. Enter details: ")
info_list = [tuple(case.split(',')) for case in user_inp.split(' ')]
print(sorted(info_list, key=lambda x: (x[0], x[1], x[2])))



#q10
x, y = 0, 0
print("Q10.",end=" ")
while True:
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)
c = round(c)
print("Distance: ", c)



#q11
user_inp = input("Q11. Enter the string: ")
i = 0
while i < len(user_inp):
    count = 1
    while i + 1 < len(user_inp) and user_inp[i].casefold() == user_inp[i + 1].casefold():
        i += 1
        count += 1
    print(user_inp[i].casefold() + str(count), end="")
    i += 1
print()


#q12
inp = input("Q12. Enter string: ")
user_inp = list(inp)
print(user_inp)
output=[]
strs = "0123456789"
num_list = list(strs)

for i in range(len(inp)):
    if user_inp[i].isalpha():
        t_sum = 0
        if i < len(inp)-2:
            if user_inp[i+1] in num_list:
                for j in range(i+1,len(user_inp)):
                    if user_inp[j] in num_list:
                        t_sum += int(user_inp[j])
                    if user_inp[j].isalpha():
                        if t_sum == 9:
                            output.append([user_inp[i],user_inp[j]])
                        else:
                            continue

for i, j in output:
    print(i,j, sep=",")



#q13  
user_inp = input("Q13. Enter binary no: ")
result = 0
 
   # Pick a starting point
for i in range(0, len(user_inp)):
    if (user_inp[i] == '1'):
            for j in range(i+1, len(user_inp)):
                if (user_inp[j] == '1'):
                    result = result + 1

print(result)



#q14
notes = eval(input("Q14. Enter list of currency denominations: "))
notes.sort(reverse=True)
amount = int(input("Enter the amount: "))
notesCount = {}
for note in notes:
    if amount >= int(note):
        notesCount[int(note)] = amount//int(note)
        amount = amount % int(note)
             
print ("Currency Count ->")
for key, val in notesCount.items():
    print(f"{key}-{val}")



#q15
def stations(n, m): 
    num = 1
    dem = 1
    s = m
 
    while m!= 1: 
        dem *= m
        m -= 1
      
    t = n- s + 1
    while t != (n-2 * s + 1): 
        num *= t 
        t-=1
    if (n- s + 1) >= s: 
        return int(num/dem) 
    else: 
        return -1
  
user_inp1 = int(input("Q15. n: "))
user_inp2 = int(input("m: "))
num = stations(user_inp1, user_inp2) 
if num != -1: 
    print(num) 
else: 
    print("Not Possible") 
  
# q16
print("Q16.",end=" ")
p1_wins = 0
p2_wins = 0
while p1_wins != 5 and p2_wins != 5:
    print("Choose Stone, Paper, or Scissor:")
    user_inp = input("Player A and Player B: ")
    choice = user_inp.split()
    p1 = choice[0]
    p1 = p1.lower()

    p2 = choice[1]
    p2 = p2.lower()

    if (p1 == "stone"):
        if (p2 == "stone"):
            print("DRAW")

        elif (p2 == "paper"):
            print("Player B wins")
            p2_wins += 1

        elif (p2 == "scissor"):
            print("Player A wins")
            p1_wins += 1

    elif (p1 == "paper"):
        if (p2 == "stone"):
            print("Player A wins")
            p1_wins += 1 

        elif (p2 == "paper"):
            print("DRAW")

        elif (p2 == "scissor"):
            print("Player B wins")
            p2_wins += 1

    elif (p1 == "scissor"):
        if (p2 == "stone"):
            print("Player B wins")
            p2_wins += 1

        elif (p2 == "paper"):
            print("Player A wins")
            p1_wins += 1 

        elif (p2 == "scissor"):
            print("DRAW")
    else:
        print("Invalid input, try again")



# q17
reg_exp = r'\b[a-z0-9._%+-]+@[a-z0-9._]+\.[a-z]{2,7}\b'
 
 
def check(email):
    if(re.fullmatch(reg_exp, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")


user_inp = input("Q17. Enter email: ")
check(user_inp)



# q18
# 18_a
user_inp = int(input("Q18_a. Enter num of rows: "))
count = 1
for i in range(1, user_inp+1):
        for j in range(1, i+1):
            if j < i:
                print(count, end='*')
            else:
                print(count, end='')
            count += 1
        print()

# 18_b      
def print_diamond(n):
    for i in range(n):
        for j in range(n-i+1):
            # for left spacing
            print(end=" ")
        for j in range(i+1):
            print("*", end=" ")
        # for new line
        print()
    for i in range(n-1,0,-1):
        for j in range(n-i+2):
            print(end=' ')
        for j in range(i):
            print("*", end=" ")
        print()


user_inp = int(input("Q18_b. Enter num of rows: "))
print_diamond(user_inp)

# 18_c
def pattern_pyr(N):
    count = 1
     
    # This is upper half of pattern
    for i in range(1, N+1):
        for j in range(1, i+1):
            if j < i:
                print(count, end='*')
            else:
                print(count, end='')
            count += 1
        print()
 
    count = count - N -(N-1)
     
    # This is lower half of pattern
    for i in range(N-1, 0, -1):
        for j in range(1, i+1):
            if j < i:
                print(count, end='*')
            else:
                print(count, end='')
            count += 1
        count = (count + 1) - 2 * i
        print()


user_inp = int(input("Q18_c. Enter num of rows: "))
pattern_pyr(user_inp)

# 18_d
def Pattern_g(line): 
    pat="" 
    for i in range(0,line):     
        for j in range(0,line):      
            if ((j == 1 and i != 0 and i != line-1) or ((i == 0 or
                i == line-1) and j > 1 and j < line-2) or (i == ((line-1)/2) 
                and j > line-5 and j < line-1) or (j == line-2 and
                i != 0 and i != line-1 and i >=((line-1)/2))):   
                pat=pat+"*"   
            else:       
                pat=pat+" "   
        pat=pat+"\n"   
    return pat 
   
user_inp = int(input("Q18_d. Enter num of rows: "))
print(Pattern_g(user_inp))

# 18_e
num_row = int(input("Q18_e. Enter no of rows: "))

for i in range(num_row):
    for j in range(num_row):
        if (i == 0 or i == (num_row-1)):
            print("1", end=" ")
        elif (j == ((num_row-1)/2) or (j == num_row/2 or j == ((num_row/2)-1))):
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()



# q19
def solution(list , num, case):
    old = list
    new = [0]*len(list)
    if case == 1:
        for i in range(num):
            new[-1] = old[0]
            new[:-1] = old[1:]
            old = new.copy()
            print("".join(new))
    elif case == 2:
        for i in range(num):
            new[0]=old[-1]
            new[1:] = old[:-1]
            old = new.copy() # This was the problematic line
            print("".join(new))


case_inp = int(input("Q19. Enter choice 1 or 2: "))
user_inp = input("Enter string: ")
num_inp = int(input("Enter no of time to be moved: "))
lists = list(user_inp)

solution(lists, num_inp, case_inp)



# q20
print("Q20.",end=" ")
healthy = {"Sugar level":15, "Blood pressure":32, "Heartbeat rate":71, "weight":65, "fat percentage":10}
patient_inp = {}
parameters = ["Sugar level","Blood pressure","Heartbeat rate","weight","fat percentage"]
for i in parameters:
    val = int(input("{}:".format(i)))
    patient_inp[i] = val
print(patient_inp)
compare = {}
for i in parameters:
    compare[i] = healthy[i] - patient_inp[i]
print(compare)
for key, value in compare.items():
    print(key, value)
    if value > 0:
        print(f"{key} is {value} more than the ideal value")
    if value < 0:
        value = -value
        print(f"{key} is {value} less than the ideal value")



# q21
def isArmstrong(x):
    num_str = str(x)
    n = len(str(x))
    sum1 = sum(int(digit)**n for digit in num_str)

    # If condition satisfies
    if (sum1 == x):
        print("Armstrong number")
    else:
        print("not an armstrong number")


user_inp = int(input("Q21. Enter num: "))
isArmstrong(user_inp)



# q22
def DecimalToBinary(num):
        if num > 1:
            DecimalToBinary(num // 2)
        print(num % 2, end='') 


user_inp = int(input("Q22. Enter num: "))
DecimalToBinary(user_inp)
print()



# q23
def Perfect_Num(num):
    Sum = 0
    for i in range(1, num//2+1):
        if(num % i == 0):
            Sum = Sum + i
    if (Sum == num):
        print("Perfect number")
    else:
        print("Not a perfect number")


user_inp = int(input("Q23. Enter num: "))
Perfect_Num(user_inp)
