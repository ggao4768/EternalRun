from gamelib import*

game=Game(640,480,"Eternal Run")
start=Animation("images\\mega360.png",48,game,1920/6,1920/8,3)

title=Animation("images\\megabeginning.png",12,game,480,320,3)
title.resizeTo(game.width,game.height)

instructions=Image("images\\INSTRUCTIONS.png",game)
instructions.resizeTo(game.width,game.height)
game.setBackground(instructions)

boom = Sound("sound\\starwars.wav",2)
    
while not game.over:
    game.processInput()

    instructions.draw()
    boom.play()

    if keys.Pressed[K_ESCAPE]:
        game.over=True
    game.update(60)
         
start=Animation("images\\mega360.png",48,game,1920/6,1920/8,3)

title=Animation("images\\megabeginning.png",12,game,480,320,3)
title.resizeTo(game.width,game.height)

game.over=False
while not game.over:
    game.processInput()
    
    title.draw()
    start.draw()

    game.drawText("ETERNAL RUN",game.width/4 ,game.height/6,Font(green,70,yellow))
    game.drawText("Press [SPACE] To Start",0,0,Font(red,30,green))
    game.drawText("Copright @ 2017, Time Flyers Inc.",game.width/2,game.height - 30,Font(yellow,30,blue))    
    game.update(60)

    if keys.Pressed[K_SPACE]:
        game.over=True

meter=game.score

bk=Image("images\\day.png",game)
bk.resizeTo(game.width,game.height)
game.setBackground(bk)
    
bar=Animation("images\\bar.png",3,game,700,110,3)
bar.resizeTo(game.width,bar.height)
bar.moveTo(320,game.height-50)

land=Animation("images\\landobstacle.png",12,game,800,600,3)
land.resizeBy(-70)
xCoordinate=game.width
land.moveTo(xCoordinate+150,bar.y-80)
land.setSpeed(5,90)

air=Animation("images\\air.png",8,game,800,600,3)
air.resizeBy(-80)
y=randint(150,250)
air.moveTo(xCoordinate,y)
air.setSpeed(5,90)

run=Animation("images\\megarun.png",5,game,500,500,1)
run.resizeBy(-88)
run.moveTo(bar.x-300,bar.y-80)
run.stop()

lastdance=Sound("sound\\bigbang-lastdance.wav",1)

jumping = False 
landed = False 
factor = 1

game.over=False
while not game.over:
    
    game.processInput()
    
    game.scrollBackground("left",3)
    bk.draw()
    bar.draw()
    land.move()
    air.move()
    lastdance.play()
    
    game.score +=1

    if keys.Pressed[K_LEFT]: 
        run.nextFrame()
        run.x -= 8
    elif keys.Pressed[K_RIGHT]:
        run.prevFrame()
        run.x += 8
    else:
        run.draw()

    if run.y <345:
        landed = False
    else:
        landed = True
    if jumping:
        run.y -= 24 * factor
        factor *= .95
        landed = False

        if factor < .18:
            jumping = False

            factor = 1
            
    if keys.Pressed[K_UP] and landed and not jumping:
        jumping = True

    if not landed:
        run.y += 7

    if land.isOffScreen("left"):
        xCoordinate=game.width
        land.moveTo(xCoordinate+100,bar.y-80)

    if air.isOffScreen("left"):
        y=randint(150,250)
        air.moveTo(xCoordinate,y)
        air.setSpeed(5,90)

    if run.collidedWith(land) or run.collidedWith(air):
        game.over=True

    if game.over:
        game.drawText("Meters: "+ str(game.score),0,0)               
        game.update(30)
        game.drawText("Game Over",game.width/4+20 ,game.height/6+50,Font(black,70,red))
        game.drawText("Press [SPACE] to End",game.width/2+50,game.height-30)
        game.update(60)
        game.wait(K_SPACE)
        game.quit() 

    if game.score>1000:
        game.over=True
            
    game.drawText("Meters: "+ str(game.score),0,0)               
    game.update(30)
game.drawText("Next Level",game.width/4+20 ,game.height/6+50,Font(black,70,red))
game.drawText("Press [SPACE] to Start",game.width/2+50,game.height-30)
game.update(60)
game.wait(K_SPACE)
game.over=False

bk1=Image("images\\forest1.png",game)
bk1.resizeTo(game.width,game.height)

bird=Animation("images\\bk2.bird.png",7,game,141,113)
bird.resizeBy(-15)
y=randint(150,250)
bird.moveTo(xCoordinate,y)
bird.setSpeed(5,90)

game.score=1001

while not game.over:
    
    game.processInput()

    game.scrollBackground("left",4)
    bk1.draw()
    bar.draw()
    land.move()
    bird.move()

    land.speed=6
    bird.speed=6
    
    game.score+=2

    if keys.Pressed[K_LEFT]: 
        run.nextFrame()
        run.x -= 8
    elif keys.Pressed[K_RIGHT]:
        run.prevFrame()
        run.x += 8
    else:
        run.draw()

    if run.y <345:
        landed = False
    else:
        landed = True
    if jumping:
        run.y -= 24 * factor
        factor *= .95
        landed = False


        if factor < .18:
            jumping = False

            factor = 1
            
    if keys.Pressed[K_UP] and landed and not jumping:
            jumping = True

    if not landed:
        run.y += 9

    if land.isOffScreen("left"):
        xCoordinate=game.width
        land.moveTo(xCoordinate+100,bar.y-80)

    if bird.isOffScreen("left"):
        y=randint(150,250)
        bird.moveTo(xCoordinate,y)
        bird.setSpeed(5,90)

    if run.collidedWith(land) or run.collidedWith(bird):
        game.over=True
        
    if game.over:
        game.drawText("Meters: "+ str(game.score),0,0)               
        game.update(30)
        game.drawText("Game Over",game.width/4+20 ,game.height/6+50,Font(black,70,red))
        game.drawText("Press [SPACE] to End",game.width/2+50,game.height-30)
        game.update(60)
        game.wait(K_SPACE)
        game.quit()
        
    if game.score>2500:
        game.over=True
    game.drawText("Meters: "+ str(game.score),0,0)               
    game.update(30)
game.drawText("Next Level",game.width/4+20 ,game.height/6+50,Font(black,70,red))
game.drawText("Press [SPACE] to Start",game.width/2+50,game.height-30)
game.update(60)
game.wait(K_SPACE)
game.over=False

bk2=Image("images\\background2.png",game)
bk2.resizeTo(game.width,game.height)

kangaroo=Animation("images\\bk3 kangaroo.png",8,game,421,299)
kangaroo.resizeBy(-70)
xCoordinate=game.width
kangaroo.moveTo(xCoordinate+150,bar.y-110)
kangaroo.setSpeed(5,90)

game.score=2501

while not game.over:    
    game.processInput()
    
    game.scrollBackground("left",4)
    bk2.draw()
    kangaroo.move()
    air.move()
    lastdance.play()
    
    game.score +=3

    air.speed=7
    kangaroo.speed=7
    

    if keys.Pressed[K_LEFT]: 
        run.nextFrame()
        run.x -= 8
    elif keys.Pressed[K_RIGHT]:
        run.prevFrame()
        run.x += 8
    else:
        run.draw()

    if run.y <345:
        landed = False
    else:
        landed = True
    if jumping:
        run.y -= 24 * factor
        factor *= .95
        landed = False


        if factor < .18:
            jumping = False

            factor = 1

            
    if keys.Pressed[K_UP] and landed and not jumping:
            jumping = True

    if not landed:
        run.y += 7

    if kangaroo.isOffScreen("left"):
        xCoordinate=game.width
        kangaroo.moveTo(xCoordinate+100,bar.y-110)

    if air.isOffScreen("left"):
        y=randint(150,250)
        air.moveTo(xCoordinate,y)
        air.setSpeed(5,90)

    if run.collidedWith(kangaroo) or run.collidedWith(air):
        game.over=True
        
    if game.over:
        game.drawText("Meters: "+ str(game.score),0,0)               
        game.update(30)
        game.drawText("Game Over",game.width/4+20 ,game.height/6+50,Font(black,70,red))
        game.drawText("Press [SPACE] to End",game.width/2+50,game.height-30)
        game.update(60)
        game.wait(K_SPACE)
        game.quit()

    if game.score>4500:
        game.over=True

        
    game.drawText("Meters: "+ str(game.score),0,0)               
    game.update(30)
game.drawText("Next Level",game.width/4+20 ,game.height/6+50,Font(black,70,red))
game.drawText("Press [SPACE] to Start",game.width/2+50,game.height-30)
game.update(60)
game.wait(K_SPACE)
game.over=False 

bk3=Image("images\\background3.png",game)
bk3.resizeTo(game.width,game.height)

bird=Animation("images\\bk2.bird.png",7,game,141,113)
bird.resizeBy(-15)
y=randint(150,250)
bird.moveTo(xCoordinate,y)
bird.setSpeed(5,90)

kangaroo=Animation("images\\bk3 kangaroo.png",8,game,421,299)
kangaroo.resizeBy(-70)
xCoordinate=game.width
kangaroo.moveTo(xCoordinate+150,bar.y-60)
kangaroo.setSpeed(5,90)

run.moveTo(bar.x-300,bar.y-50)

game.score=4502

while not game.over:    
    game.processInput()
    
    game.scrollBackground("left",5)
    bk3.draw()
    kangaroo.move()
    bird.move()
    lastdance.play()
    
    game.score +=4

    bird.speed=8
    kangaroo.speed=8
    

    if keys.Pressed[K_LEFT]: 
        run.nextFrame()
        run.x -= 8
    elif keys.Pressed[K_RIGHT]:
        run.prevFrame()
        run.x += 8
    else:
        run.draw()

    if run.y <345:
        landed = False
    else:
        landed = True
    if jumping:
        run.y -= 24 * factor
        factor *= .95
        landed = False


        if factor < .18:
            jumping = False

            factor = 1
            
    if keys.Pressed[K_UP] and landed and not jumping:
            jumping = True

    if not landed:
        run.y += 7

    if kangaroo.isOffScreen("left"):
        xCoordinate=game.width
        kangaroo.moveTo(xCoordinate+100,bar.y-60)

    if bird.isOffScreen("left"):
        y=randint(150,250)
        bird.moveTo(xCoordinate,y)
        bird.setSpeed(5,90)

    if run.collidedWith(kangaroo) or run.collidedWith(bird):
        game.over=True
        
    if game.over:
        game.drawText("Meters: "+ str(game.score),0,0)               
        game.update(30)
        game.drawText("Game Over",game.width/4+20 ,game.height/6+50,Font(black,70,red))
        game.drawText("Press [SPACE] to End",game.width/2+50,game.height-30)
        game.update(60)
        game.wait(K_SPACE)
        game.quit()

    if game.score>6500:
        game.over=True
        
    game.drawText("Meters: "+ str(game.score),0,0)               
    game.update(30)
game.drawText("Next Level",game.width/4+20 ,game.height/6+50,Font(black,70,red))
game.drawText("Press [SPACE] to Start",game.width/2+50,game.height-30)
game.update(60)
game.wait(K_SPACE)
game.over=False

bk4=Image("images\\background4.png",game)
bk4.resizeTo(game.width,game.height)

sea=Animation("images\\shark1.png",19,game,250,250,3)
sea.resizeBy(-60)
y=randint(150,250)
sea.moveTo(xCoordinate,y)
sea.setSpeed(5,90)

xCoordinate=game.width
land.moveTo(xCoordinate+150,bar.y-30)
land.setSpeed(5,90)

run.moveTo(bar.x-300,bar.y-30)


game.score=6503   

while not game.over:    
    game.processInput()
    
    game.scrollBackground("left",5)
    bk4.draw()
    land.move()
    sea.move()
    lastdance.play()
    
    game.score +=4

    sea.speed=10
    land.speed=10
    

    if keys.Pressed[K_LEFT]: 
        run.nextFrame()
        run.x -= 8
    elif keys.Pressed[K_RIGHT]:
        run.prevFrame()
        run.x += 8
    else:
        run.draw()

    if run.y <400:
        landed = False
    else:
        landed = True
    if jumping:
        run.y -= 24 * factor
        factor *= .95
        landed = False


        if factor < .18:
            jumping = False

            factor = 1
            
    if keys.Pressed[K_UP] and landed and not jumping:
            jumping = True

    if not landed:
        run.y += 7

    if land.isOffScreen("left"):
        xCoordinate=game.width
        land.moveTo(xCoordinate+100,bar.y-30)

    if sea.isOffScreen("left"):
        y=randint(150,250)
        sea.moveTo(xCoordinate,y)
        sea.setSpeed(5,90)

    if run.collidedWith(land) or run.collidedWith(sea):
        game.over=True
        
    if game.over:
        game.drawText("Meters: "+ str(game.score),0,0)               
        game.update(30)
        game.drawText("Game Over",game.width/4+20 ,game.height/6+50,Font(black,70,red))
        game.drawText("Press [SPACE] to End",game.width/2+50,game.height-30)
        game.update(60)
        game.wait(K_SPACE)
        game.quit()

    if game.score>=10000:
        game.over=True
        
    game.drawText("Meters: "+ str(game.score),0,0)               
    game.update(30)
game.drawText("Next Level",game.width/4+20 ,game.height/6+50,Font(black,70,red))
game.drawText("Press [SPACE] to Start",game.width/2+50,game.height-30)
game.update(60)
game.wait(K_SPACE)

game.over=False

bk5=Image("images\\background5.png",game)
bk5.resizeTo(game.width,game.height)

monster=Sound("sound\\MONSTER.wav",3)
cactus=Image("images\\bk5 cactus.png",game)
cactus.resizeBy(-75)
xCoordinate=game.width
cactus.moveTo(xCoordinate+150,bar.y-80)
cactus.setSpeed(5,90)

game.score=10003

while not game.over:    
    game.processInput()
    
    game.scrollBackground("left",6)
    bk5.draw()
    cactus.move()
    air.move()
    lastdance.play()
    
    game.score +=5

    air.speed=12
    cactus.speed=12
    

    if keys.Pressed[K_LEFT]: 
        run.nextFrame()
        run.x -= 8
    elif keys.Pressed[K_RIGHT]:
        run.prevFrame()
        run.x += 8
    else:
        run.draw()

    if run.y <345:
        landed = False
    else:
        landed = True
    if jumping:
        run.y -= 24 * factor
        factor *= .95
        landed = False


        if factor < .18:
            jumping = False

            factor = 1
            
    if keys.Pressed[K_UP] and landed and not jumping:
            jumping = True

    if not landed:
        run.y += 7

    if cactus.isOffScreen("left"):
        xCoordinate=game.width
        cactus.moveTo(xCoordinate+100,bar.y-80)

    if air.isOffScreen("left"):
        y=randint(150,250)
        air.moveTo(xCoordinate,y)
        air.setSpeed(5,90)

    if run.collidedWith(air) or run.collidedWith(cactus):
        game.over=True
        
    if game.over:
        game.drawText("Meters: "+ str(game.score),0,0)               
        game.update(30)
        game.drawText("Game Over",game.width/4+20 ,game.height/6+50,Font(black,70,red))
        game.drawText("Press [SPACE] to End",game.width/2+50,game.height-30)
        game.update(60)
        game.wait(K_SPACE)
        game.quit()

    if game.score>15000:
        game.over=True


    game.drawText("Meters: "+ str(game.score),0,0)               
    game.update(30)
game.drawText("Final Level (Endless) ",game.width/4-80 ,game.height/6+50,Font(black,70,red))
game.drawText("Press [SPACE] to Start",game.width/2+50,game.height-30)
game.update(60)
game.wait(K_SPACE)
game.over=False

bk6=Animation("images\\background7.png",32,game,640,480,3)
bk6.resizeTo(game.width,game.height)

run.moveTo(bar.x-300,bar.y-10)

monster=Sound("sound\\MONSTER.wav",3)

dragon=Animation("images\\bk6 dragon.png",4,game,132,89,3)
y=randint(150,250)
dragon.moveTo(xCoordinate,y)
dragon.setSpeed(5,90)

fire=Animation("images\\bk6 fire.png",16,game,1000/3,1500/6,3)
fire.resizeBy(-70)
xCoordinate=game.width
fire.moveTo(xCoordinate+150,bar.y-10)
fire.setSpeed(5,90)

game.score=15005

while not game.over:    
    game.processInput()
    
    game.scrollBackground("left",7)
    bk6.draw()
    fire.move()
    dragon.move()
    monster.play()
     
    game.score +=7

    dragon.speed=15
    fire.speed=15
    

    if keys.Pressed[K_LEFT]: 
        run.nextFrame()
        run.x -= 8
    elif keys.Pressed[K_RIGHT]:
        run.prevFrame()
        run.x += 8
    else:
        run.draw()

    if run.y <420:
        landed = False
    else:
        landed = True
    if jumping:
        run.y -= 24 * factor
        factor *= .95
        landed = False

        if factor < .18:
            jumping = False

            factor = 1
            
    if keys.Pressed[K_UP] and landed and not jumping:
            jumping = True

    if not landed:
        run.y += 7

    if fire.isOffScreen("left"):
        xCoordinate=game.width
        fire.moveTo(xCoordinate+100,bar.y-10)

    if dragon.isOffScreen("left"):
        y=randint(150,250)
        dragon.moveTo(xCoordinate,y)
        dragon.setSpeed(5,90)

    if run.collidedWith(fire) or run.collidedWith(dragon):
        game.over=True

    if game.score>25000:
        game.score +=8
        dragon.speed=18
        fire.speed=18
        
    if game.score>50000:
        game.score +=9
        dragon.speed=19
        fire.speed=19
        
    if game.score>70000:
        game.score +=11
        dragon.speed=21
        fire.speed=21

    if game.score>85000:
        game.score +=13
        dragon.speed=23
        fire.speed=23
        
    if game.score>100000:
        game.score +=14
        dragon.speed=24
        fire.speed=24
        
    if game.score>120000:
        game.score +=15
        dragon.speed=25
        fire.speed=25

    if game.score>150000:
        game.score +=17
        dragon.speed=27
        fire.speed=27
        
    if game.score>170000:
        game.score +=19
        dragon.speed=30
        fire.speed=30
        
    if game.score>200000:
        game.score +=21
        dragon.speed=31
        fire.speed=31
        
    if game.score>230000:
        game.score +=23
        dragon.speed=33
        fire.speed=33
        
    if game.score>250000:
        game.score +=25
        dragon.speed=35
        fire.speed=35
        
    if game.score>280000:
        game.score +=27
        dragon.speed=37
        fire.speed=37

    if game.score>300000:
        game.score +=28
        dragon.speed=39
        fire.speed=39
        
    if game.score>330000:
        game.score +=30
        dragon.speed=40
        fire.speed=40
        
    if game.score>350000:
        game.score +=31
        dragon.speed=41
        fire.speed=41
        
    if game.score>380000:
        game.score +=33
        dragon.speed=43
        fire.speed=43

    if game.score>410000:
        game.score +=37
        dragon.speed=45
        fire.speed=45

    if game.score>450000:
        game.score +=40
        dragon.speed=50
        fire.speed=50
          
    if game.over:
        game.drawText("Meters: "+ str(game.score),0,0)               
        game.update(30)
        game.drawText("Game Over",game.width/4+20 ,game.height/6+50,Font(black,70,red))
        game.drawText("Press [SPACE] to End",game.width/2+50,game.height-30)
        game.update(60)
        game.wait(K_SPACE)
        game.quit()

    game.drawText("Meters: "+ str(game.score),0,0)               
    game.update(30)
game.update(60)
game.wait(K_SPACE)

