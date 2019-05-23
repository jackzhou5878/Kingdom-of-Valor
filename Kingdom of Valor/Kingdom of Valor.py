from gamelib import*

#Myobjects and initial settings
game = Game(800,600,"Kingdom of Valor")
bk = Image("bk1.jpg",game)
game.setBackground(bk)
bk.resizeTo(800,600)
sabeehah = Image("sabeehah.png", game)
sabeehah.resizeBy(-92)
title = Image("title.png", game)
title.resizeBy(-20)
howtoplay = Image("howtoplay.png", game)
howtoplay.resizeBy(-40)
play = Image("play.png", game)
play.resizeBy(-40)
story = Image("story.png", game)
story.resizeBy(-40)
storyImage = Image("storyimage.png", game)
storyImage.visible = False
howtoplayImage = Image("howtoplayImage.png", game)
howtoplayImage.visible = False
back = Image("back.png", game)
back.resizeBy(-90)
back.visible = False
minions = Image("minion.png", game)
mage = Image("mage.png", game)
mage.resizeBy(-30)
mage.y = 410
mage.x = 650
mage.setSpeed(25,180)
portal = Image("portal.png", game)
portal.resizeBy(-40)
bk2 = Image("bk2.gif", game)
bk2.resizeTo(800,600)
explosion = Animation("explosion.gif", 1, game, 128, 128)
explosion.resizeTo(180,180)
explosion.visible = False
fireball = Animation("fireball.png",6,game,3072/6,512,512)
fireball.resizeBy(-80)
fireball.visible = False
magic = Image("magic.png", game)
portal.x = 700
portal.y = 450
sabeehah.y = 500
sabeehah.x = 100
howtoplay.y = 500
story.y = 350
play.y = 200
title.y = 100
back.y = 550
back.x = 50
f = Font(white,40,cyan,"Impact")
m = Font(white,20,cyan,"Impact")
fireball.setSpeed(20,270)
mage.health = 1500

#Title Sreen
while not game.over:
    game.processInput()
    bk.draw()
    title.draw()
    howtoplay.draw()
    play.draw()
    storyImage.draw()
    story.draw()
    sabeehah.draw()
    howtoplayImage.draw()
    back.draw()
    explosion.draw()

    if play.collidedWith(mouse)and mouse.LeftClick:
        game.over = True
        
    if story.collidedWith(mouse)and mouse.LeftClick:
        howtoplayImage.visible = False
        storyImage.visible = True
        story.visible = False
        back.visible = True
        

    if back.collidedWith(mouse)and mouse.LeftClick:
        storyImage.visible = False
        story.visible = True
        back.visible = False
        howtoplay.visible = True
        howtoplayImage.visible = False

    if howtoplay.collidedWith(mouse)and mouse.LeftClick:
        storyImage.visible = False
        howtoplayImage.visible = True
        howtoplay.visible = True
        back.visible = True

    game.update(30)
        
game.over = False

#Level 1
game.time = 60

while not game.over:
    game.processInput()
    keys = KeyBoard()
    minions = []
    bk.draw()
    portal.draw()
    mage.draw()
    game.displayTime(10,10,f)
    game.time -= 0.0048
    game.displayScore(600,10,f)
    game.drawText("LEVEL 1",350,10,f)
    sabeehah.move(True)
    mage.move(True)
    fireball.draw()
    fireball.move()
    

    if fireball.x >= 800:
        fireball.visible = False
    
    if game.time <0:
        game.over = True

    if keys.Pressed[K_UP]:
        sabeehah.y -= 5

    if keys.Pressed[K_DOWN]:
        sabeehah.y += 5

    if keys.Pressed[K_RIGHT]:
        sabeehah.x += 5

    if keys.Pressed[K_LEFT]:
        sabeehah.x -= 5

    if keys.Pressed[K_w]:
        sabeehah.y -= 5

    if keys.Pressed[K_s]:
        sabeehah.y += 5

    if keys.Pressed[K_d]:
        sabeehah.x += 5

    if keys.Pressed[K_a]:
        sabeehah.x -= 5

    if game.time <= 58:
        portal.visible = False
        
    if game.score >= 2000:
        portal.visible = True
        mage.visible = False

    if keys.Pressed[K_SPACE] and fireball.visible==False:
        fireball.visible = True
        fireball.x = sabeehah.x+100
        fireball.y = sabeehah.y
        fireball.move()

    if sabeehah.collidedWith(mage):
        explosion.visible = True
        explosion.draw()
        explosion.x = sabeehah.x
        explosion.y = sabeehah.y
        sabeehah.health -=5

    if fireball.collidedWith(mage):
        game.score +=25

    if sabeehah.collidedWith(portal):
        game.over = False

    if mage.isOffScreen("top"):
        mage.y+=5

    if fireball.collidedWith(mage):
        mage.health -=100
        fireball.visible = False

    if mage.health <= 0:
        portal.visible = True
        mage.visible = False
        
    game.drawText(" Health:"+str(sabeehah.health),sabeehah.x-25,sabeehah.y+70)
    game.drawText(" Health:"+str(mage.health),mage.x-25,mage.y+110)

    if sabeehah.health <= 0:
        game.over = True                    
        
    game.update(30)

game.over = False

#Level 2

while not game.over:
    game.processInput()
    bk2.draw()

    game.update(30)

game.over = False

