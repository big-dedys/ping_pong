import pygame 
pygame.init()


back = (200, 255, 255)
mw = pygame.display.set_mode((500,500))
mw.fill(back)

clock = pygame.time.Clock()


class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

            
    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self, filename, x=0, y=0,  width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)

        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


ball = Picture('ball.png', 160, 200, 50, 50)
platform_1_lf = Picture('platform.png',10, 100, 30, 100)
platform_2_rg = Picture('platform.png',460, 100, 30, 100)

start_x = 5
start_y = 5
count = 9 

move_platform_y = 3
move_x = 0
move_y = 0
game_over = False

platform_1_lf_up = False
platform_1_lf_down = False
platform_2_rg_up = False 
platform_2_rg_down = False 



while not game_over:
    ball.fill()
    platform_1_lf.fill()
    platform_2_rg.fill()
                     
    ball.rect.x += move_x
    ball.rect.y += move_y

    if ball.rect.x > 450 or ball.rect.x < 0:
        move_x *= -1
    if ball.rect.y < 0:
        move_y *= -1
    if ball.rect.colliderect(platform_1_lf.rect):
                move_y *= -1
    if ball.rect.colliderect(platform_2_rg.rect):
                move_y *= -1 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True 


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                platform_1_lf_up = True
            if event.key == pygame.K_s:
                platform_1_lf_down = True
            if event.key == pygame.K_UP:
                platform_2_rg_up = True  
            if event.key == pygame.K_DOWN:
                platform_2_rg_down = True
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                platform_1_lf_up = False
            if event.key == pygame.K_s:
                platform_1_lf_down = False
            if event.key == pygame.K_UP:
                platform_2_rg_up = False
            if event.key == pygame.K_DOWN:
                platform_2_rg_down = False


#        if event.type == pygame.KEYDOWN:


#        if event.type == pygame.KEYUP:

    if platform_1_lf_up:
        platform_1_lf.rect.y -= move_platform_y
    if platform_1_lf_down: 
        platform_1_lf.rect.y += move_platform_y    

    
    if platform_2_rg_up:
        platform_2_rg.rect.y -= move_platform_y
    if platform_2_rg_down: 
        platform_2_rg.rect.y += move_platform_y    

    if ball.rect.y > 500:
        print('Ты проиграл!')
        game_over = True
    



    ball.draw()
    platform_1_lf.draw()
    platform_2_rg.draw()

    pygame.display.update()
    clock.tick(40)
pygame.display.update()