print('hello world')
print('what is your name?')
myName=input()
print('It is good to meet you, '+ myName)
print('The length of your name is"')
print(len(myName))
print('What is your age?')
myAge =input()
print('You will be '+str(int(myAge)+1) +' in next year')


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(6):
	for j in range (8):
		print (grid[j][i],end='')
	print(grid[j+1][i])
