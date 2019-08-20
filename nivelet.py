def nivelet():
    i01.moveArm("left", 8, 90, 90, 97) #take initial position
    i01.moveArm("right", 20, 98, 90, 94) #take initial position
    i01.head.neck.moveTo(90) #move head down
    i01.moveHand("left", 180, 180, 180, 180, 180, 57) #wrist initial position
    sleep(5)
    i01.moveArm("left", 90, 90, 90, 97) #left bicep up
    sleep(5)
    i01.moveArm("left", 89, 90, 90, 97) #keep left bicep in place
    i01.moveHand("left", 180, 180, 180, 180, 180, 37)
    sleep(5)
    i01.moveArm("left", 90, 90, 90, 97) #keep left bicep in place
    i01.moveArm("right", 20, 98, 150, 94) #move right shoulder up
    sleep(6)
    i01.moveArm("left", 20, 90, 90, 97) #keep left bicep in place
    i01.moveArm("right", 20, 98, 149, 94) #move right shoulder up
    i01.head.neck.moveTo(0) #move head down
    sleep(4)
    i01.moveArm("left", 8, 90, 90, 97) #take initial position
    i01.moveArm("right", 20, 98, 90, 94) #take initial position
    i01.head.neck.moveTo(90) #move head down
    i01.moveHand("left", 180, 180, 180, 180, 180, 57) #wrist initial position
