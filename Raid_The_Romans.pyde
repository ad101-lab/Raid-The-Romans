import random        

def setup():
     fullScreen()
     background(255)
     img = loadImage("castle.png")
     image(img, displayWidth*0.75, displayHeight*0.3, displayHeight*0.25, displayHeight*0.25)
     line(displayWidth*0.7, 0, displayWidth*0.7, displayHeight)
     frameRate(12)
      global archerTowerX 
     global archerTowerY 
     global reload
     reload == 1
     archerTowerX = 0 
     archerTowerY = 0
     
def draw():
    global soldierX, soldierY, soldierAlive, gameMode
    background(255)
    for i in range(len(soldierY)):
        img = loadImage("soldier.png")
        image(img, soldierX[i-1], soldierX[i-1], displayWidth*0.1, displayHeight*0.2)
    img = loadImage("castle.png")
    image(img, displayWidth*0.75, displayHeight*0.3, displayHeight*0.25, displayHeight*0.25)
    line(displayWidth*0.7, 0, displayWidth*0.7, displayHeight)
     
     
def mouseClicked():
     if gameMode == 0:
          for i in range(len(soldierAlive)):
               if dist(mouseX, mouseY, soldierX[i-1], soldierY[i-1])<20:
                    soldierAlive[i-1].delete()
                    soldierX[i-1].delete()
                    soldierY[i-1].delete(



class archerTower(object):
  def __init__ (mouseX,mouseY):
    def mouseClicked(): 
      archerTowerX = mouseX
      archerTowerY = mouseY
      fill(255,255,2555)
      circle(archerTowerX,archerTowerY,10)
#img(archerTower, archerTowerX,archerTowerY)
  
tower1 = archerTower(0)
  
def delayTimer():
    m = millis
    if millis == (m + 100):
        reload = 1
        
    if ((dist(archerTowerX,archerTowerY,soilderX,soilderY) > height/ 10) && (reload == 1)):
    line(archerTowerX,archerTowerY, soilderX,soilderY)
    
    if reload == 0:
    delayTimer(
