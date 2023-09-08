print("Welcome to the quiz! ")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
print("Okey! Lets Play :) ")
rules= ('''So here are the rules
        Every correct answer will get 1 point
       ''')
print(rules)
score = 0
ques= input("Who is known as father of computer? ")

if ques.lower() == 'charles babbage':
    print("Correct")
    score += 1
else:
    print("Incorrect")

ques= input("What is the brain of computer system called? ")

if ques.lower() == 'cpu':
    print("Correct")
    score += 1
else:
    print("Incorrect")

ques= input("What does CPU stands for? ")

if ques.lower() == 'central processing unit':
    print("Correct")
    score += 1
else:
    print("Incorrect")

ques= input("What does RAM stands for? ")

if ques.lower() == 'random access memory':
    print("Correct")
    score += 1
else:
    print("Incorrect")

ques= input('''What is the smallest unit of memory?
            1-  Byte 
            2- Bit
            3- Nibble
            4- KB 
            ''')

if ques.lower() == 'bit':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("The game has ended and your score is " , + score)