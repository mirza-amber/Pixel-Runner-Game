import pygame
from sys import exit

pygame.init()

game_active = True

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\\Pixeltype.ttf' ,50)
test_font2 = pygame.font.Font('font\\Pixeltype.ttf' ,100)

sky_surface = pygame.image.load('graphics\\Sky.jpg').convert()
sky_rect = sky_surface.get_rect(topleft=(0,0))
ground_surface = pygame.image.load('graphics\\ground.jpg').convert()

snail_1 = pygame.image.load('graphics\\snail\\snail1.png').convert_alpha()
snail_rect = snail_1.get_rect(bottomleft=(1100, 390))

player_surface = pygame.image.load('graphics\\Player\\player_stand.png').convert_alpha()
# player_rect = player_surface.get_rect(bottom =(390), left=(50))                                  #This command just creates a rectangle of the size of image it is built in reference to and just placed on the screen as per the positional arguments.
player_rect = player_surface.get_rect(bottomleft=(50, 390))                                         #This command just creates a rectangle of the size of image it is built in reference to and just placed on the screen as per the positional arguments.
player_gravity = 0

text_surf_start = test_font2.render('Play Game', False , 'Black')
text_surf_start_rect = text_surf_start.get_rect(center=(500,300))

actual_score = 0
score_surface = test_font.render(f'Score : {actual_score} ' , True, 'Black')
score_rect = score_surface.get_rect(center=(500,100))

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            # print(event.pos)
            mousepos = event.pos
        if player_rect.bottom == 390 and game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # if event.key == pygame.K_SPACE:
                #     # print(player_rect.y)
                #     # print(player_gravity)
                player_gravity = -12
            elif event.type == pygame.MOUSEBUTTONDOWN and player_rect.collidepoint(event.pos):
                # print('Press Mouse')
                player_gravity = -12
        
    if game_active:

        screen.blit(sky_surface, (0,-70))
        screen.blit(ground_surface, (0,390))
        pygame.draw.rect(screen, '#8694BA', score_rect, 0 , 3)
        pygame.draw.rect(screen, '#8694BA', score_rect, 10, 3)

        snail_rect.left -= 7
        if snail_rect.left < -50: snail_rect.left = 1100
        screen.blit(snail_1, snail_rect)

        player_gravity += 0.6
        player_rect.y += player_gravity
        if player_rect.bottom >= 390: player_rect.bottom = 390 
        screen.blit(player_surface, (player_rect))                                                  #Here instead of giving the coordinates directly we place the image(player_surface) isnide the rectangle that has already been placed on the screen

        if player_rect.colliderect(snail_rect): game_active=False                                   #Game Ends on collision

        if snail_rect.bottomleft[0] == 50 :                                                         #Score when snail clears the player_rect boundary without collision
            actual_score += 1
            score_surface = test_font.render(f'Score : {actual_score} ' , True, 'Black')
        screen.blit(score_surface, score_rect)


    else:
        screen.blit(sky_surface, (0,-70))
        screen.blit(ground_surface, (0,390))
        screen.blit(text_surf_start, text_surf_start_rect)
        pygame.draw.rect(screen, '#8694BA', score_rect, 0 , 3)
        pygame.draw.rect(screen, '#8694BA', score_rect, 10, 3)
        screen.blit(score_surface, score_rect)

        if event.type == pygame.KEYDOWN and pygame.K_KP_ENTER:
            actual_score = 0
            player_rect.bottom = 390
            snail_rect.left = 1100
            score_surface = test_font.render(f'Score : {actual_score} ' , True, 'Black')
            game_active = True

    # if player_rect.colliderect(snail_rect): screen.blit(text_surf_lost, (450, 225))
    # mousepos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mousepos)) : print('collision')
    
    pygame.display.update()
    clock.tick(60)                                                                              #limit the frames per second (60 per sec in this case)
    