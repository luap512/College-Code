# using pygame
import pygame

# import exit method
from sys import exit

# fucntion to display score


def displayScore():
    currentTime = int((pygame.time.get_ticks() / 1000) - startTime)
    score_surf = testFont.render(
        f'SCORE: {currentTime}', False, (64, 64, 64))
    text_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, text_rect)
    print(currentTime)


# initiate pygame
pygame.init()

# create display area (width and height)
screen = pygame.display.set_mode((800, 400))

# name of the game window
pygame.display.set_caption("Luaps first fuckin game")

# create clock object for FPS
clock = pygame.time.Clock()

# create new font (font type, size)
testFont = pygame.font.Font('font/Pixeltype.ttf', 50)

# create game state
game_active = False

# create new surface load image @ 'graphics' called 'Sky.png'
skySurface = pygame.image.load('graphics/Sky.png').convert()

# create ground surface load image @ 'graphics' called 'Ground.png'
groundSurface = pygame.image.load('graphics/Ground.png').convert()

# create text surface (text, -- , color)
# textSurface = testFont.render('Pauls first fuckin game', True, (64, 64, 64))

# create text rectangel
# text_rectangle = textSurface.get_rect(center=(400, 50))

# create snail surface load image @ 'graphics' called 'Snail1.png'
snailSurface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

# create snail rectangle
snail_rect = snailSurface.get_rect(midbottom=(800, 300))

# create variable for snake position relative to x
snailXPosition = 600

# create player surface
playerSurface = pygame.image.load(
    'graphics/player/player_walk_1.png').convert_alpha()

# create player rectangle
player_rect = playerSurface.get_rect(midbottom=(80, 300))

# create variable for gravity
playerGravity = 0

# create variable for player image
playerStand = pygame.image.load(
    'graphics/player/player_stand.png').convert_alpha()
playerStandRect = playerStand.get_rect(center=(400, 200))
playerStandScaled = pygame.transform.scale(playerStand, (200, 400))

#  create start time
startTime = 0


# loop to keep code running
while True:

    # check for user input
    for event in pygame.event.get():

        # if user closes window
        if event.type == pygame.QUIT:

            # quit game loop
            pygame.quit()
            exit()

        # check if mouse collides with player rectangle
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                print(event.pos)
                print("MOUSE COLLIDES W PLAYER")
                playerGravity = -20

        # get player input
        if game_active == True:

            # if player presses a key
            if event.type == pygame.KEYDOWN:

                # if player is pressing space and touching the floor
                if event.key == pygame.K_SPACE and player_rect.bottom >= 0:

                    # jump
                    playerGravity = -20
                    print('jumping')

            # if player releases space
            if event.type == pygame.KEYUP:
                print("key up")
        # if game is not active
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                startTime = (pygame.time.get_ticks() / 1000)

    # if game is active
    if game_active == True:
        # blit = Block Image Transfer = put one surface onto another surface (surface we're placing, position )
        screen.blit(skySurface, (0, 0))

        # place ground surface on game surface @ (0,300)
        screen.blit(groundSurface, (0, 300))

        # draw text background
        # pygame.draw.rect(screen, "#c0e8ec", text_rectangle, 0, 10)
        # pygame.draw.rect(screen, "#c0e8ec", text_rectangle, 6, 10)

        # generate text
        # screen.blit(textSurface, text_rectangle)

        # display the score
        displayScore()

        # if snail X position is less than -100 pixels
        if snail_rect.right <= 0:
            # move snail to the right of screen
            snail_rect.left = 800

        # move snail
        snail_rect.left -= 4
        # place snail enemy on game surface
        screen.blit(snailSurface, snail_rect)

        # if snail X position is less than -100 pixels
        if player_rect.right <= 800:
            # move snail to the right of screen
            player_rect.left = 0

        # move player
        player_rect.left += 1

        # if snail player position is less than -100 pixels
        # if player_rect.left <= 800:
        # move snail to the right of screen
        #   player_rect.left = 0

        # make player respond to gravity
        player_rect.bottom += playerGravity

        # iterate gravity
        playerGravity += 1

        # make player respond to floor
        if player_rect.bottom >= 300:
            player_rect.bottom += 20
            player_rect.bottom = 300

        # check for collision b/w snail and player
        if snail_rect.colliderect(player_rect):

            # end game loop
            game_active = False
            snail_rect.left = 800
            player_rect.midbottom = (80, 300)

        # place player on game surface
        screen.blit(playerSurface, player_rect)

    # if game is inactive
    else:
        # fill screen with black
        screen.fill('black')
        screen.blit(playerStandScaled, playerStandRect)

    # update display surface
    pygame.display.update()

    # while loop should not run faster than 60 times per second
    clock.tick(60)
