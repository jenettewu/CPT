def setup():
    size(640, 480)
    global setting, death_background
    setting = loadImage("fish bg.jpg")
    death_background = loadImage("fish bg you died.jpg")


def draw():
    menu()


def menu():
    global setting
    image(setting, 0, 0)
    fill(0)
    textAlign(CENTER, CENTER)
    textSize(80)
    text("CHOMP!", 320, 100)
    draw_button("PLAY", 170, 185, 300, 80, (239, 201, 239))
    fill(255)
    triangle(410, 210, 410, 250, 450, 230)
    draw_button("LEADERBOARD", 60, 280, 250, 80, (239, 201, 239))
    draw_button("INSTRUCTIONS", 330, 280, 250, 80, (239, 201, 239))
    instruction()
    leaderboard()
    play()

instruction_pass = False
playing_pass = False
leaderboard_pass = False
menu_screen = True
death = False


def draw_button(button_text, button_x, button_y,
                button_width, button_height, (r, g, b)):
    global playing_pass, leaderboard_pass, instruction_pass, menu_screen, death
    noStroke()

    if mouseX in range(button_x, button_x + button_width) \
       and mouseY in range(button_y, button_y + button_height):
        fill(r - 50, g - 50, b - 50)
        if mousePressed:
            if playing_pass is False and death is False and \
               instruction_pass is False and leaderboard_pass is False:
                if button_text == "PLAY":
                    reset()
                elif button_text == "LEADERBOARD":
                    leaderboard_pass = True
                elif button_text == "INSTRUCTIONS":
                    instruction_pass = True
            if button_text == "RESTART":
                add_score()
                reset()
            elif button_text == "BACK":
                leaderboard_pass = False
                instruction_pass = False
            elif button_text == "EXIT":
                add_score()
                death = False
                menu_screen = True
                playing_pass = False

    else:
        fill(r, g, b)

    rect(button_x, button_y, button_width, button_height)

    fill(255)
    textSize(30)
    textAlign(CENTER, CENTER)
    pushMatrix()
    translate(button_x, button_y)
    text(button_text, button_width/2, button_height/2)
    popMatrix()


def reset():
    global playing_pass, menu_screen, score, death
    global o_fish_yco, o_fish_xco, o_fish_length, o_fish_width
    death = False
    playing_pass = True
    menu_screen = False
    score = 0
    o_fish_yco = []
    o_fish_xco = []
    o_fish_length = []
    o_fish_width = []
    speed = []
    generation()
    play()


player_fish_x = 0
player_fish_y = 0
player_fish_length = 75
player_fish_width = 50
old_mouseX = 320
side_change = 1


def fish_movement():
    global player_fish_x, player_fish_y, player_fish_length, player_fish_width
    global old_mouseX, side_change
    fill(0)
    ellipse(player_fish_x, player_fish_y,
            player_fish_length, player_fish_width)
    player_fish_x = mouseX
    player_fish_y = mouseY
    if old_mouseX > mouseX:  # move right
        triangle(player_fish_x + player_fish_length/3, player_fish_y,
                 player_fish_x + player_fish_length/2 + player_fish_length/4,
                 player_fish_y - player_fish_width/3,
                 player_fish_x + player_fish_length/2 + player_fish_length/4,
                 player_fish_y + player_fish_width/3)
        side_change = 0
    elif old_mouseX < mouseX:  # move left
        triangle(player_fish_x - player_fish_length/3, player_fish_y,
                 player_fish_x - player_fish_length/2 - player_fish_length/4,
                 player_fish_y + player_fish_width/3,
                 player_fish_x - player_fish_length/2 - player_fish_length/4,
                 player_fish_y - player_fish_width/3)
        side_change = 1
    if side_change == 1:
        triangle(player_fish_x - player_fish_length/3, player_fish_y,
                 player_fish_x - player_fish_length/2 - player_fish_length/4,
                 player_fish_y + player_fish_width/3,
                 player_fish_x - player_fish_length/2 - player_fish_length/4,
                 player_fish_y - player_fish_width/3)
    else:
        triangle(player_fish_x + player_fish_length/3, player_fish_y,
                 player_fish_x + player_fish_length/2 + player_fish_length/4,
                 player_fish_y - player_fish_width/3,
                 player_fish_x + player_fish_length/2 + player_fish_length/4,
                 player_fish_y + player_fish_width/3)
    old_mouseX = player_fish_x


continue_play = True


def keyPressed():
    if playing_pass is True and death is False:
        if key == ' ':
            global continue_play
            if continue_play is True:
                continue_play = False
                noLoop()
                pause()
            elif continue_play is False:
                continue_play = True
                loop()


def pause():
    fill(239, 201, 239)
    noStroke()
    rect(100, 100, 440, 280)
    fill(255)
    textSize(30)
    textAlign(CENTER, CENTER)
    text("PAUSED", 320, 240)
    textSize(20)
    text("Press the spacebar to resume", 320, 350)


def play():
    global player_fish_x, player_fish_y, setting, death, playing_pass
    if playing_pass is True:
        image(setting, 0, 0)
        other_fish()
        fish_movement()
    if death is True:
        playing_pass = False
        death_screen()


def instruction():
    global instruction_pass
    if instruction_pass is True:
        background("#6EC5E9")
        rect(120, 40, 400, 400)
        textSize(32)
        fill(0, 102, 153)
        text("INSTRUCTIONS", 315, 70)
        draw_button("BACK", 525, 350, 110, 70, (239, 201, 239))
        textSize(24)
        fill(0, 102, 153)
        textSize(20)
        text("Control the fish with your mouse.", 320, 140)
        text("Press the spacebar to pause.", 320, 180)
        text(" Your goal is to eat as many fish", 320, 220)
        text("as you can without being eaten.", 320, 260)
        text(" Good Luck ^^", 320, 300)

game_scores = []
game_num = 1


def add_score():
    global game_scores, score, game_num
    game_scores.append([score, game_num])
    game_num += 1
    game_scores.sort()
    game_scores.reverse()
    if len(game_scores) > 10:
        game_scores.pop()

word_height = 30


def leaderboard():
    global game_scores, word_height, score, game_num, leaderboard_pass
    if leaderboard_pass is True:
        background("#6EC5E9")
        rect(120, 40, 400, 400)
        textSize(32)
        fill(0, 102, 153)
        text("LEADERBOARD", 315, 70)

        for i in range(len(game_scores)):
            textSize(24)
            textAlign(TOP, CENTER)
            text("Game " + str(game_scores[i][1]), 180, 130 + word_height * i)
            text("Score " + str(game_scores[i][0]), 320, 130 + word_height * i)

        draw_button("BACK", 525, 350, 110, 70, (239, 201, 239))

o_fish_yco = []
o_fish_xco = []
o_fish_length = []
o_fish_width = []
speed = []
o_fish_colour = []


def generation():
    for fish_num in range(10):
        o_fish_yco.append(int(random(50, 430)))
        o_fish_xco.append(int(random(2)))
        o_fish_width.append(random(5, 100))
        o_fish_length.append(o_fish_width[fish_num] + o_fish_width[fish_num]/2)
        o_fish_colour.append(color(random(255), random(255), random(255)))

        # fish starts on the left and travels right
        if o_fish_xco[fish_num] == 0:
            o_fish_xco[fish_num] = int(random(-400, -40))
            speed.append(random(1, 2))

        # fish starts on the right and travels left
        else:
            o_fish_xco[fish_num] = int(random(940, 680))
            speed.append(-(random(1, 2)))

points = 0
update_points = 0
score = 0


def other_fish():
    global o_fish_length, o_fish_width, player_fish_width, player_fish_length
    global points, update_points, score, speed, death
    noStroke()
    for fish_num in range(10):
        noStroke()
        fill(o_fish_colour[fish_num])
        if (speed[fish_num] < 0 and o_fish_xco[fish_num] < -100) or \
           (speed[fish_num] > 0 and o_fish_xco[fish_num] > 740):
            o_fish_yco[fish_num] = (int(random(50, 430)))
            o_fish_xco[fish_num] = (int(random(2)))
            o_fish_colour[fish_num] = \
                (color(random(255), random(255), random(255)))
            if o_fish_xco[fish_num] == 0:
                o_fish_xco[fish_num] = int(random(-400, -40))
                speed[fish_num] = (random(1, 2))
            else:
                o_fish_xco[fish_num] = int(random(940, 680))
                speed[fish_num] = (-(random(1, 2)))

        if speed[fish_num] < 0:  # fish travels right
            ellipse(o_fish_xco[fish_num], o_fish_yco[fish_num],
                    o_fish_length[fish_num], o_fish_width[fish_num])
            triangle(o_fish_xco[fish_num] + o_fish_length[fish_num]/3,
                     o_fish_yco[fish_num],
                     o_fish_xco[fish_num] + o_fish_length[fish_num]/2 +
                     o_fish_length[fish_num]/4,
                     o_fish_yco[fish_num] - o_fish_width[fish_num]/3,
                     o_fish_xco[fish_num] + o_fish_length[fish_num]/2 +
                     o_fish_length[fish_num]/4,
                     o_fish_yco[fish_num] + o_fish_width[fish_num]/3)
            quad(o_fish_xco[fish_num],
                 o_fish_yco[fish_num] - o_fish_width[fish_num]/5,
                 o_fish_xco[fish_num] + o_fish_length[fish_num]/4.5,
                 o_fish_yco[fish_num] - o_fish_width[fish_num]/2 -
                 o_fish_width[fish_num]/4.5,
                 o_fish_xco[fish_num] + o_fish_length[fish_num]/2,
                 o_fish_yco[fish_num] - o_fish_width[fish_num]/2 -
                 o_fish_width[fish_num]/5.5,
                 o_fish_xco[fish_num] + o_fish_length[fish_num]/6,
                 o_fish_yco[fish_num] - o_fish_width[fish_num]/4)
            quad(o_fish_xco[fish_num],
                 o_fish_yco[fish_num] + o_fish_width[fish_num]/5,
                 o_fish_xco[fish_num] + o_fish_length[fish_num]/4.5,
                 o_fish_yco[fish_num] + o_fish_width[fish_num]/2 +
                 o_fish_width[fish_num]/4.5,
                 o_fish_xco[fish_num] + o_fish_length[fish_num]/2,
                 o_fish_yco[fish_num] + o_fish_width[fish_num]/2 +
                 o_fish_width[fish_num]/5.5,
                 o_fish_xco[fish_num] + o_fish_length[fish_num]/6,
                 o_fish_yco[fish_num] + o_fish_width[fish_num]/4)
            stroke(0)
            ellipse(o_fish_xco[fish_num] - o_fish_length[fish_num]/4,
                    o_fish_yco[fish_num] - o_fish_width[fish_num]/8,
                    o_fish_width[fish_num]/3.5, o_fish_width[fish_num]/3.5)
            fill(0)
            ellipse(o_fish_xco[fish_num] - o_fish_length[fish_num]/4,
                    o_fish_yco[fish_num] - o_fish_width[fish_num]/8,
                    o_fish_width[fish_num]/7, o_fish_width[fish_num]/7)
        else:  # fish travels left
            ellipse(o_fish_xco[fish_num], o_fish_yco[fish_num],
                    o_fish_length[fish_num], o_fish_width[fish_num])
            triangle(o_fish_xco[fish_num] - o_fish_length[fish_num]/3,
                     o_fish_yco[fish_num],
                     o_fish_xco[fish_num] - o_fish_length[fish_num]/2 -
                     o_fish_length[fish_num]/4,
                     o_fish_yco[fish_num] + o_fish_width[fish_num]/3,
                     o_fish_xco[fish_num] - o_fish_length[fish_num]/2 -
                     o_fish_length[fish_num]/4,
                     o_fish_yco[fish_num] - o_fish_width[fish_num]/3)
            quad(o_fish_xco[fish_num],
                 o_fish_yco[fish_num] + o_fish_width[fish_num]/5,
                 o_fish_xco[fish_num] - o_fish_length[fish_num]/4.5,
                 o_fish_yco[fish_num] + o_fish_width[fish_num]/2 +
                 o_fish_width[fish_num]/4.5,
                 o_fish_xco[fish_num] - o_fish_length[fish_num]/2,
                 o_fish_yco[fish_num] + o_fish_width[fish_num]/2 +
                 o_fish_width[fish_num]/5.5,
                 o_fish_xco[fish_num] - o_fish_length[fish_num]/6,
                 o_fish_yco[fish_num] + o_fish_width[fish_num]/4)
            quad(o_fish_xco[fish_num],
                 o_fish_yco[fish_num] - o_fish_width[fish_num]/5,
                 o_fish_xco[fish_num] - o_fish_length[fish_num]/4.5,
                 o_fish_yco[fish_num] - o_fish_width[fish_num]/2 -
                 o_fish_width[fish_num]/4.5,
                 o_fish_xco[fish_num] - o_fish_length[fish_num]/2,
                 o_fish_yco[fish_num] - o_fish_width[fish_num]/2 -
                 o_fish_width[fish_num]/5.5,
                 o_fish_xco[fish_num] - o_fish_length[fish_num]/6,
                 o_fish_yco[fish_num] - o_fish_width[fish_num]/4)
            stroke(0)
            ellipse(o_fish_xco[fish_num] + o_fish_length[fish_num]/4,
                    o_fish_yco[fish_num] - o_fish_width[fish_num]/8,
                    o_fish_width[fish_num]/3.5, o_fish_width[fish_num]/3.5)
            fill(0)
            ellipse(o_fish_xco[fish_num] + o_fish_length[fish_num]/4,
                    o_fish_yco[fish_num] - o_fish_width[fish_num]/8,
                    o_fish_width[fish_num]/7, o_fish_width[fish_num]/7)

        o_fish_xco[fish_num] += speed[fish_num]

        # Increase score
        if player_fish_width > o_fish_width[fish_num] + 5:
            if speed[fish_num] > 0:
                if player_fish_x - player_fish_length/2 in range \
                    (int(o_fish_xco[fish_num] - o_fish_length[fish_num]/3),
                     int(o_fish_xco[fish_num] + o_fish_length[fish_num]/3)) \
                    and o_fish_yco[fish_num] in range \
                    (int(player_fish_y - player_fish_width/2),
                     int(player_fish_y + player_fish_width/2)):
                        points += 1
                        o_fish_xco[fish_num] = 800
                elif player_fish_x + player_fish_length/2 in range \
                    (int(o_fish_xco[fish_num] - o_fish_length[fish_num]/2 -
                     o_fish_length[fish_num]/4),
                     int(o_fish_xco[fish_num] + o_fish_length[fish_num]/3)) \
                    and o_fish_yco[fish_num] in range \
                    (int(player_fish_y - player_fish_width/2),
                     int(player_fish_y + player_fish_width/2)):
                        points += 1
                        o_fish_xco[fish_num] = 800
            elif speed[fish_num] < 0:
                if player_fish_x + player_fish_length/2 in range \
                    (int(o_fish_xco[fish_num] - o_fish_length[fish_num]/3),
                     int(o_fish_xco[fish_num] + o_fish_length[fish_num]/2)) \
                    and o_fish_yco[fish_num] in range \
                    (int(player_fish_y - player_fish_width/2),
                     int(player_fish_y + player_fish_width/2)):
                        points += 1
                        o_fish_xco[fish_num] = -200
                elif player_fish_x - player_fish_length/2 in range \
                    (int(o_fish_xco[fish_num] - o_fish_length[fish_num]/3),
                     int(o_fish_xco[fish_num] + o_fish_length[fish_num]/2 +
                     o_fish_length[fish_num]/4)) and o_fish_yco[fish_num] \
                    in range(int(player_fish_y - player_fish_width/2),
                     int(player_fish_y + player_fish_width/2)):
                        points += 1
                        o_fish_xco[fish_num] = -200

        # death
        if player_fish_width < o_fish_width[fish_num]:
            if speed[fish_num] > 0:
                if player_fish_x - player_fish_length/2 in range \
                   (int(o_fish_xco[fish_num]),
                    int(o_fish_xco[fish_num] + o_fish_length[fish_num]/3)) \
                    and player_fish_y in range \
                    (int(o_fish_yco[fish_num] - o_fish_width[fish_num]/2),
                     int(o_fish_yco[fish_num] +
                     o_fish_width[fish_num]/2)):
                        death = True
            elif speed[fish_num] < 0:
                if player_fish_x + player_fish_length/2 in range \
                    (int(o_fish_xco[fish_num] - o_fish_length[fish_num]/3),
                     int(o_fish_xco[fish_num])) and player_fish_y in range \
                    (int(o_fish_yco[fish_num] - o_fish_width[fish_num]/2),
                     int(o_fish_yco[fish_num] +
                     o_fish_width[fish_num]/2)):
                        death = True

        if points != update_points:
            score += int(o_fish_width[fish_num] + o_fish_length[fish_num])/10
            update_points = points
        show_score()


def death_screen():
    global score, death_background, game_scores, score
    image(death_background, 0, 0)
    textSize(60)
    fill(0)
    textAlign(CENTER, CENTER)
    text("YOU DIED!", 320, 100)
    textSize(30)
    text("YOUR SCORE: " + str(score), 320, 200)
    if len(game_scores) < 1 or score >= max(game_scores[0]):
        highscore = score
    else:
        highscore = max(game_scores[0])
    text("HIGH SCORE: " + str(highscore), 320, 250)
    draw_button("EXIT", 20, 365, 250, 80, (239, 201, 239))
    draw_button("RESTART", 370, 365, 250, 80, (239, 201, 239))


def show_score():
    global score
    textSize(25)
    text("Score: " + str(score), 80, 50)
