from pygame import *
window = display.set_mode((1920, 1080))
bacgraund = transfofm.scale(image.load('legir.webp'))
display.set_caption('пинпонг')
tic = time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed

     def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed


p1 = Player('pinbi', 20, 50, 5)
p2 = Player('pinbi', 20, 50, 5)
game = True 
while game:
    window.blit(legir ,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    tic.tick(60)
    display.update
