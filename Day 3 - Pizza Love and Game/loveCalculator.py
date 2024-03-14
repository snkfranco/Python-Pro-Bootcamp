print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combinedNames = name1 + name2
lower_combinedNames = combinedNames.lower()
t = lower_combinedNames.count('t')
r = lower_combinedNames.count('r')
u = lower_combinedNames.count('u')
e = lower_combinedNames.count('e')
times1 = t + r + u + e
l = lower_combinedNames.count('l')
o = lower_combinedNames.count('o')
v = lower_combinedNames.count('v')
e = lower_combinedNames.count('e')
times2 = l + o + v + e

strTimes = str(times1) + str(times2)
finalScore = int(strTimes)

if finalScore < 10 or finalScore > 90:
  print(f'Your score is {finalScore}, you go together like coke and mentos.')
elif finalScore > 40 and finalScore < 50:
  print(f'Your score is {finalScore}, you are alright together.')
else:
  print(f'Your score is {finalScore}.')