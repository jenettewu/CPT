x = 0
page = 0
looping = True

def setup():
    size(640, 480)
    
def draw():
    global x
    background(255)
    fill(0)
    ellipse(x, 240, 40, 40)
    if x >= 640:
        x = 0
    x += 1
    
def keyPressed():
    global looping
    
    if key == ' ':
        if looping == True:
            looping = False
            noLoop()
        elif looping == False:
            looping = True
            loop()
