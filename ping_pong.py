from pygame import *
font.init()
font = font.Font(None,35)
lose1 = font.render('PLAYER1 LOSE!',True,(180,0,0))
lose2 = font.render('PLAYER2 LOSE!',True,(180,0,0))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,wight,height):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(wight,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('ping pong')
back = (251, 208, 188)
window.fill(back)
racket1 = Player('rakket.png',30,200,4,50,150)
racket2 = Player('rakket.png',520,200,4,50,150)
ball = GameSprite('tennis.png',200,200,6,50,50)
FPS = 60
clock = time.Clock()
game = True
finish = False
speed_x = 6
speed_y = 6
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2,(200,200))
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
