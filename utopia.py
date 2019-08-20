def utopia():
	i01.moveHand("right", 180, 180, 180, 180, 180, 155)
	i01.moveArm("right", 20, 98, 90, 94)
	i01.moveArm("left", 22, 90, 90, 97)
	i01.moveHand("left",180,180,180,180,180,56)
	print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')
	sleep(6)
	i01.moveArm("left", 38, 130, 163, 126)
	i01.moveHand("left", 180, 180, 180, 180, 180, 62)
	sleep(6)
	print commands.getoutput('/bin/echo "900,50,50,900,900" | /usr/bin/nc localhost 20000')
	sleep(0.5)
	print commands.getoutput('/bin/echo "900,400,400,900,900" | /usr/bin/nc localhost 20000')
	sleep(0.5)
	print commands.getoutput('/bin/echo "900,50,50,900,900" | /usr/bin/nc localhost 20000')
	sleep(0.5)
	print commands.getoutput('/bin/echo "900,400,400,900,900" | /usr/bin/nc localhost 20000')
	i01.moveArm("left", 38, 130, 164, 126) #keep left shoulder in place

	sleep(2)
	i01.moveHand("right", 180, 180, 180, 180, 180, 165)
	sleep(3)
	i01.moveArm("right", 20, 98, 90, 130) #moves right arm to the side
	i01.moveArm("left", 38, 130, 163, 128) #keep left shoulder in place
	print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/turnleft.sh')
	sleep(2)
	print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/forward.sh')
	sleep(0.2)
	print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/forward.sh')
	sleep(0.2)
	 #long break due to walking around
	#turn left 180degrees and go forward
	#keep both hands in position
	i01.moveArm("right", 80, 47, 110, 98)
	i01.moveHand("right", 180, 180, 180, 180, 180, 168)
	i01.moveArm("left", 85, 38, 146, 125)
	i01.moveHand("left", 180, 180, 180, 180, 180, 55)
	sleep(5)
	i01.moveArm("right", 20, 98, 90, 94)
	sleep(2)
	i01.moveArm("left", 22, 90, 90, 97)
	print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')
	sleep(4)
	i01.head.rothead.moveTo(135)
	print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 14000') #right hand open
	i01.moveArm("left", 8, 130, 90, 120) #left arm to the side
	sleep(2)
	i01.moveArm("right", 94, 84, 174, 132) #right arm up

	i01.moveHand("left", 180, 180, 180, 180, 180, 60)
	print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 20000') #left hand to a fist
	sleep(5)
	#walk forward
	i01.head.rothead.moveTo(90)
	i01.head.neck.moveTo(63) #head neck initial positions
	i01.moveArm("left", 78, 65, 170, 103)
	print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000') #open left hand
	sleep(2)
	i01.moveArm("left", 78, 90, 170, 103)
	i01.moveArm("right", 94, 119, 174, 132)
	sleep(5)
	i01.moveArm("left", 76, 90, 120, 100) #move arms to initial duck position
	i01.moveArm("right", 85, 90, 111, 101) #move arms to initial duck position
	sleep(3)
	i01.moveArm("left", 76, 90, 120, 100) #stay
	i01.moveArm("right", 59, 90, 111, 101) #down
	print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/forward.sh')
	print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/forward.sh')
	sleep(1)
	i01.moveArm("left", 50, 90, 120, 100) #down
	i01.moveArm("right", 85, 90, 111, 101) #up
	sleep(1)
	print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/forward.sh')
	print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/forward.sh')
	i01.moveArm("left", 76, 90, 120, 100) #up
	i01.moveArm("right", 59, 90, 111, 101) #down
	sleep(1)
	i01.moveArm("left", 50, 90, 120, 100) #down
	i01.moveArm("right", 85, 90, 111, 101) #up
	sleep(1)
	i01.moveArm("left", 76, 90, 120, 100) #up
	i01.moveArm("right", 85, 90, 111, 101) #end duck
	sleep(0.5)
	i01.head.neck.moveTo(133)
	i01.head.rothead.moveTo(14)
	sleep(2)
	i01.head.jaw.moveTo(0)
	sleep(1)
	i01.head.jaw.moveTo(180)
	sleep(1)
	i01.head.jaw.moveTo(0)
	sleep(1)
	i01.head.jaw.moveTo(180)
	sleep(1)
	i01.head.jaw.moveTo(0)
	sleep(1)
	i01.head.jaw.moveTo(180)
	sleep(1)
	i01.moveArm("right", 86, 69, 134, 113) #right hand goes up front, fingers ready to move
	sleep(2)
	i01.moveArm("left", 76, 37, 132, 100) #place left hand under right hand
	sleep(2)
	print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 14000') #right hand open
	print commands.getoutput('/bin/echo "50,50,50,50,900" | /usr/bin/nc localhost 14000') #right hand open
	print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/back.sh')
	sleep(0.2)
	print commands.getoutput('/bin/echo "50,50,50,900,900" | /usr/bin/nc localhost 14000') #right hand open
	sleep(0.2)
	print commands.getoutput('/bin/echo "50,50,900,900,900" | /usr/bin/nc localhost 14000') #right hand open
	sleep(0.2)
	print commands.getoutput('/bin/echo "50,900,900,900,900" | /usr/bin/nc localhost 14000') #right hand open
	sleep(0.2)
	print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 14000') #right hand open
	sleep(0.5)
	print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/back.sh')
	print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 14000') #right hand open
	sleep(1)
	print commands.getoutput('/bin/echo "50,50,50,50,900" | /usr/bin/nc localhost 14000') #right hand open
	sleep(0.1)
	print commands.getoutput('/bin/echo "50,50,50,900,900" | /usr/bin/nc localhost 14000') #right hand open
	sleep(0.1)
	print commands.getoutput('/bin/echo "50,50,900,900,900" | /usr/bin/nc localhost 14000') #right hand open
	sleep(0.1)
	print commands.getoutput('/bin/echo "50,900,900,900,900" | /usr/bin/nc localhost 14000') #right hand open
	sleep(0.1)
	print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 14000') #right hand open
	sleep(0.5)
	i01.moveArm("left", 76, 37, 132, 126) #move left to the side
	sleep(1.5)
	i01.moveArm("right", 70, 69, 96, 126)
	sleep(1.5)
	i01.moveArm("left", 76, 72, 102, 126)
	sleep(1.5)
	i01.moveArm("right", 70, 15, 140, 94)
	sleep(1.5)
	i01.moveArm("left", 76, 72, 102, 126)
	sleep(1.5)
	i01.head.rothead.moveTo(90)
	i01.head.neck.moveTo(63)
	i01.moveArm("right", 20, 90, 90, 94)
	sleep(1)
	i01.moveArm("left", 8, 86, 90, 97)
