import os
while True:
	userName = raw_input('Please input your name:')
	if userName == 'easy':
		password = raw_input('Welcome, please input your password:')
		while password != 'year93926':
			password = raw_input('Wrong,please input your password again!:')
		while True:
			fname = raw_input('Welcome, now you can tell me the file name you want open it :')
			while os.path.exists(fname) == False:
				fname = raw_input('Wrong file name input again:')
			f = file(fname)
			while True:
				line = f.readline()
				if len(line) == 0:
					break
				print line
			print '\nfile over!!'
	else:
		continue