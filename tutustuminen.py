def tutustuminen():
    sleep(21)
    i01.head.neck.moveTo(90)
    print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 14000')
    print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')
    i01.moveArm("right", 20, 90, 90, 97) #right arm down
    i01.moveHand("right", 180, 180, 180, 180, 180, 144) #set right hand's wrist position
    i01.moveArm("left", 22, 90, 90, 97) #left arm down
    i01.moveHand("left", 180, 180, 180, 180, 180, 63) #set left hand's wrist position

    sleep(3)
    i01.moveArm("right", 97, 141, 154, 143) #right arm up
    i01.moveArm("left", 50, 130, 169, 149) #left arm up
    sleep(5)
    print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 14000')
    print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 20000')
    sleep(1)
    print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 14000')
    print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')
    sleep(1)
    print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 14000')
    print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 20000')
    sleep(1)
    print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 14000')
    print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')
    sleep(1)
    print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 14000')
    print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 20000')
    sleep(1)
    i01.moveArm("right", 96, 141, 154, 142) #right arm up
    print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 14000')
    print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')
    sleep(1)
    print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 14000')
    print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 20000')
    sleep(1)
    print commands.getoutput('/bin/echo "900,50,50,900,900" | /usr/bin/nc localhost 20000') #left hand fore- and middlefinger up
    sleep(1)
    print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 20000') #left into fist
    sleep(1)
    print commands.getoutput('/bin/echo "900,50,50,50,900" | /usr/bin/nc localhost 14000') #right hand fore, middle and ring finger up
    sleep(1)
    print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 14000') #right into fist
    sleep(1)
    print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 14000') #right open
    sleep(1)
    print commands.getoutput('/bin/echo "900,900,900,900,900" | /usr/bin/nc localhost 14000') #right fist
    sleep(1)
    print commands.getoutput('/bin/echo "50,50,900,900,900" | /usr/bin/nc localhost 20000') #left hand thumb and forefinger up
    sleep(1.5)
    momotalk3("haha haha,haha")
    #i01.head.jaw.moveTo(180) #toistolla suun aukaiseminen
    #sleep(1)
    #i01.head.jaw.moveTo(0)
    sleep(1)
    print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 20000')
    print commands.getoutput('/bin/echo "50,50,50,50,50" | /usr/bin/nc localhost 14000')
    i01.moveArm("right", 20, 90, 90, 97) #right arm down
    i01.moveArm("left", 22, 90, 90, 97) #left arm down
    sleep(3)
    i01.moveHand("right", 180, 180, 180, 180, 180, 168) #set right hand's wrist position
    i01.moveHand("left", 180, 180, 180, 180, 180, 48) #set left hand's wrist position
    sleep(3)
    sleep(3)
    i01.moveArm("right", 100, 90, 144, 97) #right arm up
    i01.moveArm("left", 90, 90, 144, 97) #left arm up
    sleep(5)

    #now wheel chair will start going forwards
    #arms start going up and down
    i01.moveHand("right", 180, 180, 180, 180, 180, 144) #set right hand's wrist position to point outside
    sleep(1.5)
    i01.moveArm("right", 20, 90, 90, 97) #right arm down
    sleep(2)
    i01.moveHand("left", 180, 180, 180, 180, 180, 64) #set left hand's wrist position to point outside
    sleep(1.5)
    i01.moveArm("right", 100, 90, 144, 97) #right arm up
    i01.moveArm("left", 22, 90, 90, 97) #left arm down
    print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/forward.sh')
    print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/forward.sh')
    print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/forward.sh')
    sleep(1.5)
    i01.moveArm("left", 90, 90, 144, 97) #left arm up
    i01.moveArm("right", 20, 90, 90, 97) #right arm down
    sleep(1.5)
    i01.moveArm("right", 100, 90, 144, 97) #right arm up
    i01.moveArm("left", 22, 90, 90, 97) #left arm down
    sleep(1.5)
    i01.moveArm("left", 90, 90, 144, 97) #left arm up
    i01.moveArm("right", 20, 90, 90, 97) #right arm down

    #back down with wheelchair, if possible BACK BACK BACK BACK
    i01.moveArm("left", 83, 56, 165, 97) #left arm cross over face
    i01.moveHand("left", 180, 180, 180, 180, 180, 48)
    i01.moveHand("right", 180, 180, 180, 180, 180, 167) #turn right wrist here so it doesnt crash to left hand
    sleep(2)
    i01.moveArm("right", 97, 60, 150, 97) #right arm cross over face
    print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/back.sh')
    print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/back.sh')
    print commands.getoutput('/Users/helsinkispare/Documents/myrobotlab.1.0.2693/back.sh')
    sleep(4)
    i01.head.neck.moveTo(90)
    i01.moveArm("right", 97, 120, 150, 97) #right arm rotate to the side
    i01.moveHand("right", 180, 180, 180, 180, 180, 144) #move hand outside
    sleep(1)
    i01.moveArm("left", 83, 105, 150, 97) #left arm cross over face
    i01.moveHand("left", 180, 180, 180, 180, 180, 64)
    sleep(2)
    i01.moveArm("right", 20, 90, 90, 97) #right arm down
    i01.moveHand("right", 180, 180, 180, 180, 180, 144) #set right hand's wrist position
    i01.moveArm("left", 22, 90, 90, 97) #left arm down
    i01.moveHand("left", 180, 180, 180, 180, 180, 63) #set left hand's wrist position
    i01.head.neck.moveTo(0)
    print commands.getoutput('/bin/echo "950,950,950,950,950" | /usr/bin/nc localhost 14000') #right into fist
    print commands.getoutput('/bin/echo "950,950,950,950,950" | /usr/bin/nc localhost 20000') #left into fist
