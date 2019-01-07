death = True
score = 20

def setup():
    size(640, 480)
    
def draw():
    background(255)
    death_screen()
    
def draw_button(button_text, button_x, button_y, button_width, button_height, (r, g, b)):
    global playing_pass, leaderboard_pass, pause_pass
    noStroke()
    
    rect(button_x, button_y, button_width, button_height)
    if mouseX in range(button_x, button_x + button_width) and mouseY in range(button_y, button_y + button_height):
        fill(r - 50, g - 50, b - 50)
        if mousePressed:
            if button_text == "PLAY" or button_text == "RESTART":
                playing_pass = True
                menu_screen = False
            elif button_text == "LEADERBOARD":
                leaderboard_pass = True 
            elif button_text == "":
                pause_pass = True
            elif button_text == "EXIT":
                menu_screen = True
                playing_pass = False
            elif button_text == "RESUME":
                pause_pass = False

    else:
        fill(r, g, b)

    rect(button_x, button_y, button_width, button_height)
    
    fill(255)
    textSize(30)
    textAlign(CENTER,CENTER)
    pushMatrix()
    translate(button_x, button_y)
    text(button_text, button_width/2, button_height/2)
    popMatrix()
    
def death_screen():
    background("#6EC5E9")
    global score
    
    if death == True:
        textSize(60)
        fill(0)
        textAlign(CENTER, CENTER)
        text("YOU DIED!", 320, 100)
        textSize(30)
        text("YOUR SCORE: " + str(score), 320, 200)
        
        draw_button("EXIT", 120, 300, 140, 140, (239, 201, 239))
        draw_button("RESTART", 400, 300, 140, 140, (239, 201, 239))
        
        
