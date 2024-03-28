print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lowered_names = combined_names.lower()
t = lowered_names.count('t')
r = lowered_names.count('r')
u = lowered_names.count('u')
e = lowered_names.count('e')
first_digit = t + r + u + e
l = lowered_names.count('l')
o = lowered_names.count('o')
v = lowered_names.count('v')
e = lowered_names.count('e')
second_digit = l + o + v + e
score = int(first_digit+second_digit)
if score < 10 or score > 90:
  print(f'Your score is {score}, you go together like coke and mentos.')
elif score > 40 and score < 50:
  print(f'Your score is {score}, you are alright together.')
else:
  print(f'Your score is {score}.')