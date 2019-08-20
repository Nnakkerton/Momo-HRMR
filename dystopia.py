def dystopia():

	i = 0
	i01.moveHand("left", 180, 180, 180, 180, 180, 45)
	i01.moveHand("right", 180, 180, 180, 180, 180, 168)
	while i < 5: 

		i01.moveArm("left", 90, 90, 140, 97)
		i01.moveArm("right", 90, 90, 140, 97)

		sleep(1.0)

		i01.moveArm("left", 75, 90, 115, 97)
		i01.moveArm("right", 75, 90, 115, 97)

		sleep(1.0)
		i += 1

	i01.moveArm("left", 8, 90, 172, 97) #left arm straight up
	i01.moveArm("right", 20, 90, 90, 97) #right arm down
	#pyoratuoli lahtee rullaa
	#print commands.getoutput('/bin/echo "0,-120" | /usr/bin/nc localhost 21000') moves the wheelchair left
	sleep(5.0)
	i01.moveArm("right", 8, 90, 172, 97) #right arm up
	sleep(6.0)

	i01.moveArm("left", 8, 90, 90, 97) #arms down
	i01.moveArm("right", 20, 90, 90, 97) #arms down

	i01.moveHand("right",180,180,180,180,180,168) #wrists up
  	i01.moveHand("left",180,180,180,180,180,50) #wrists up
  	sleep(6.0)

	i01.moveArm("left", 8, 90, 172, 97) #left arm straight up
	i01.moveArm("right", 8, 90, 172, 97) #right arm up
	sleep(2)

	i01.moveArm("left", 22, 90, 120, 97)
	i01.moveArm("right", 34, 90, 120, 97)
	sleep(2)
	#arms swinging part
	n = 0
	while n < 2:
		i = 120
		j = 97
		#LEFT: twist up
		while i < 140:
			i += 1
			i01.moveArm("left", 22, 90, i, j)
			i01.moveArm("right", 34, 90, i, j)
			while j < 127:
				i01.moveArm("left", 22, 90, i, j)
				i01.moveArm("right", 34, 90, i, j)
				if i < 140:
					i += 1
				j += 1
				sleep(0.02)

		sleep(2)
		#LEFT: twist down
		while j > 97:
			j -= 15
			i01.moveArm("left", 22, 90, i, j)
			i01.moveArm("right", 34, 90, i, j)
			sleep(1)
			while i > 120:
				i01.moveArm("left", 22, 90, i, j)
				i01.moveArm("right", 34, 90, i, j)
				if j > 97:
					j -= 1
				i -= 1
				sleep(0.02)
		sleep(2)
		i01.moveArm("left", 22, 90, 120, 97)
		i01.moveArm("right", 34, 90, 120, 97)
		n += 1

	i01.moveArm("right", 20, 90, 90, 97) #right arm down
	i01.moveArm("left", 22, 90, 90, 97) #left arm down

	i01.moveArm("right", 20, 90, 90, 97) #right arm down
	print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 14000')
	i01.moveHand("right",180, 180, 180, 180, 180, 144)

	sleep(3)
	#i01.moveArm("left", 22, 90, 90, 97) #left arm down
	i01.moveArm("right", 20, 90, 174, 125) #right arm up
	i01.head.neck.moveTo(145) #moves head up
	sleep(6)

	print commands.getoutput('/bin/echo "50,400,500,500,500" | /usr/bin/nc localhost 14000')
	print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')

	sleep(0.5)


	i01.moveArm("right", 20, 60, 174, 97) #twist the arm a bit
	sleep(2)
	print commands.getoutput('/bin/echo "50,600,700,700,700" | /usr/bin/nc localhost 14000') #fingers contract
	sleep(1)
	i01.moveArm("right", 20, 90, 90, 97) #right arm down to initial position
	sleep(3)
	print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 14000')

	i01.head.neck.moveTo(5) #moves head down
	sleep(2)

	i01.moveArm("right", 50, 120, 160, 120) #right arm up and point at people
	sleep(1)
	i01.moveArm("right", 50, 120, 160, 120) #right arm up and point at people
	i01.head.neck.moveTo(50)
	sleep(4)
	print commands.getoutput('/bin/echo "800,50,800,800,800" | /usr/bin/nc localhost 14000')
	#print commands.getoutput('/Users/helsinkispare/turnright.sh')
	sleep(4)
	#i01.moveArm("right", 50, 60, 160, 120) #right arm up and point at people
	#sleep(2)
	print commands.getoutput('/bin/echo "50,50,50,900,50" | /usr/bin/nc localhost 14000')
	sleep(0.6)
	print commands.getoutput('/bin/echo "800,50,800,50,800" | /usr/bin/nc localhost 14000')
	sleep(0.5)
	i01.moveArm("right", 51, 120, 160, 120)
	print commands.getoutput('/bin/echo "50,800,400,400,50" | /usr/bin/nc localhost 14000')
	sleep(0.6)
	print commands.getoutput('/bin/echo "50,800,800,50,800" | /usr/bin/nc localhost 14000')
	sleep(0.4)
	print commands.getoutput('/bin/echo "800,400,50,50,600" | /usr/bin/nc localhost 14000')
	sleep(0.7)
	print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 14000') #sormet suoraksi
	sleep(1)

	for index in range(4):
		i01.head.jaw.moveTo(180) #loop for mouth movements
		sleep(1)
		i01.head.jaw.moveTo(0)
		sleep(1)
	i01.moveArm("right", 20, 90, 90, 97) #right arm down to initial position
	i01.moveHand("right",180, 180, 180, 180, 180, 155)
	sleep(2)
	print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/turnright.sh')
