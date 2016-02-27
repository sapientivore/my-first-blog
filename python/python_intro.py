name = 'Nyx'
girls = ['Rachel', 'Monica', 'Phoebe']

print('Hello, Django girls!')
if 3 > 2:
	print('It works!')

def hi(name):
	print('Hi there ' + name + '!')
	print('How are you?')

for name in girls:
	hi(name)
	print('Next girl')
