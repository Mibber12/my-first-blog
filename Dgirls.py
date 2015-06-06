print ('Helllo, Django girls!')
if 3 > 2:
	print ('Hey Mireille')

def hi():
	print('Hi there!')
	print('How are you?')

hi()

def hi(name):
	print('Hi ' + name + '!')
hi("Jules")	

girls = ['Amy', 'Charlotte', 'Django', 'Detta', 'You']
for name in girls:
	hi(name)
	print('Next girl')
