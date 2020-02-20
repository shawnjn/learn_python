
import pygame, sys, random
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
        global score, score_surf, score_font
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
            hit_wall.play()
            # self.speed[0] = random.randint(1, 15) #无法起到随机速度的目的，未使用
        if self.rect.top < 0 :
            self.speed[1] = -self.speed[1]
            # self.speed[1] = random.randint(1, 10) #无法起到随机的目的，未使用
            score = score + 1
            score_wav.play()
            score_surf = score_font.render(str(score), 1, (0, 0, 0))

class mypaddlleclass(pygame.sprite.Sprite):
    def __init__(self, location=[0, 0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 20])
        image_surface.fill([0, 0, 0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
pygame.mixer.init()

size =width, height =640, 480
# color =255, 255, 255
screen = pygame.display.set_mode(size)
# screen.fill([255, 255, 255])
clock = pygame.time.Clock()
ball_speed = [10, 5]
pong_ball = pong_ballclass('wackyball.bmp', ball_speed, [50, 50])
ballGroup = pygame.sprite.Group(pong_ball)
paddle = mypaddlleclass([270, 400])
lives = 3
score = 0
hit = pygame.mixer.Sound('/Users/midou/PycharmProjects/learning2020/lean_01/PyPong/hit_paddle.wav')
hit_wall =pygame.mixer.Sound('/Users/midou/PycharmProjects/learning2020/lean_01/PyPong/hit_wall.wav')
score_wav = pygame.mixer.Sound('/Users/midou/PycharmProjects/learning2020/lean_01/PyPong/get_point.wav')
gameover_wav = pygame.mixer.Sound('/Users/midou/PycharmProjects/learning2020/lean_01/PyPong/game_over.wav')
'''创建FONT对象'''
score_font = pygame.font.Font(None, 50)
score_surf = score_font.render(str(score), 1, (0, 0, 0))
score_pos = (10, 10)
done = False
running = True
while running:
    clock.tick(30)
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:               #注意pygame.quit()与pygame.QUIT的区别；
            running = False
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]
    '''检测球与球拍之间的碰撞'''
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        hit.play()
        pong_ball.speed[1] = -pong_ball.speed[1]
    pong_ball.move()
    #移动球
    '''完全重绘图形'''
    if not done:
        screen.blit(pong_ball.image, pong_ball.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_surf, score_pos)
        for i in range(lives):
            width = screen.get_width()
            screen.blit(pong_ball.image, [width - 40 * i, 20])
            pygame.display.flip()                                   #最后刷新，显示
    if pong_ball.rect.top >= screen.get_rect().bottom:
        lives = lives - 1
        '''创建和绘制分数文本'''
        if lives == 0:
            final_text1 = 'game over'
            gameover_wav.play()
            final_text2 = 'your final score is:' + str(score)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))
            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = ft2_font.render(final_text2, 1, (0, 0, 0))
            screen.blit(ft1_surf, (screen.get_width()/2 - ft1_surf.get_width()/2, 100))
            screen.blit(ft2_surf, (screen.get_width()/2 - ft2_surf.get_width()/2, 200))
            pygame.display.flip()
            done = True
        else:
            pygame.time.delay(2000)
            pong_ball.rect.topleft = (50, 50)
pygame.quit()
