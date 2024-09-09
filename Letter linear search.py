s=input('Insert the word: ')
#we try by the linear search
char=input('Insert the letter you want to search: ')
print('Insert the boundaries of search: ')
start=int(input('Insert the start position: '))
end=int(input('Insert the end position: '))
cond=False;stor=0
for i in range(start,end+1):
	if s[i]==char:
		cond=True
		stor=i
		break
if cond is True:
	print('it exists in the position number '+str(stor+1))
else:
	print('It does not exists')
exit()