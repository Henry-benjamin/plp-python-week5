import random

secrete_number = random.randint(1, 20)
guess = 0
attempts =0

while guess != secrete_number:
   guess = int(input("Enter your guess: "))
   attempts +=1
   if guess > secrete_number:
       print( "Too high!" )
   elif guess < secrete_number:
       print("Too low!")
else:
  print("congratulatetions! You got it! 🎉🏆")
  print(f"You got it in {attempts} tries!")