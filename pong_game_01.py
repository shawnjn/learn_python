
import pygame, sys
# from pygame.locals import *

class pong_ballclass(pygame.sprite.Sprite):

    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)      #注意获取image时，使用pygame.image.load(image_file)，
                                                        # 不是self.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

class mypaddlleclass(pygame.sprite.Sprite):
    def __init__(self, location=[0, 0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 20])
        image_surface.fill([0, 0, 0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
size =width, height =640, 480
# color =255, 255, 255
screen = pygame.display.set_mode(size)
# screen.fill([255, 255, 255])
clock = pygame.time.Clock()
ball_speed = [10, 5]
pong_ball = pong_ballclass('wackyball.bmp', ball_speed, [50, 50])
ballGroup = pygame.sprite.Group(pong_ball)
paddle = mypaddlleclass([270, 400])


running = True
while running:
    clock.tick(30)
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:               #注意pygame.quit()与pygame.QUIT的区别；
            running = False
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        pong_ball.speed[1] = -pong_ball.speed[1]
    pong_ball.move()
    screen.blit(pong_ball.image, pong_ball.rect)
    screen.blit(paddle.image, paddle.rect)
    pygame.display.flip()
pygame.quit()
