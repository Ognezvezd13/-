from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y, playerr_speed):
        super().__init__()
        self.image = transform.scale(image.loaD(player_image,(65,65)))
        self.speed= player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed= key.get_pressed()
        if keys_pressed[K_LEFT] and x1 >5:
            self.rect.x -= speed
        if keys_pressed[K_RIGHT] and x1 >595:
            self.rect.x += speed
        if keys_pressed[K_UP] and y1 >5:
            self.rect.y -= speed
        if keys_pressed[K_DOWN] and y1 >395:
            self.rect.y += speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= -85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self,color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height ):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
win_width = 500
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load('background.jpg'),(win_width,win_height))
player = Player('hero.png','5',win_height - 80,4)
monster = Enemy('cyborg.png',win_width - 80,280,2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80,0)
wall1 = Wall(255,200,255,100,120,98,400)
wall2 = Wall(400,400,255, 68, 150,220,300)
wall3 = Wall(150,150,255, 45,135,58,350)
game = True
clock = time.Clock()
FPS = 60
font.__init__()
font=Font.Font(None,70)
win = font.render("You win!",True,(255,115,86))
lose= font.render("You lose!",True,(15,68,123))
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.sound('money.ogg')
kick = mixer.sound('kick.ogg')
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            run = True
    if finish != True:
        window.blit(background(0,0))
        player.update()
        monster.update()
        player.reset()
        monster.reset()
        final.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
    if sprite.collide_rect(player,monster) of sprite.collide_rect(player,wall1) or sprite.collide_rect(player,wall2) or sprite.collide_rect(player,wall3):
        finish = True
        window.blit(lose,(200,200))
        kick.play()
    if sprite.collide_rect(player,final):
        finish = True
        window.blit(win,(200,200))
        money.play()
display.update()
clock.tick(FPS)