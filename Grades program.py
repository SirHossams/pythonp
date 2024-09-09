print('How are you? Please insert your score to determine your grade and tell you.')
x=int(input())
if x<60:
	print("Oh no! you have failed! your grade is F.")
elif x>=60 and x<65:
	print("Congratulations! you have passed. Your grade is D.")
elif x>=65 and x<75:
	print("Good work! your grade is C.")
elif x>=75 and x<85:
	print("Brilliant! Your grade is B.")
elif x>=85 and x<95:
	print("Excellent! Your grade is A.")
elif x>=95 and x<=100:
	print("Perfect! You are fantastic! Your grade is A+")
else:
	print("Do you try to kid with me?! This is not a score")
exit()