# 2020.01.06
# 学习char 18，输入方法

import pygame, sys
pygame.init()

size = width, height = 640, 480
background_color = [255, 255, 255]

screen = pygame.display.set_mode(size)
screen_name = pygame.display.set_caption('沙滩排球_tick')
background = pygame.Surface(screen.get_size())
background.fill(background_color)

clock = pygame.time.Clock()


class ball(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        if self.rect.left < screen.get_rect().left or self.rect.right > screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        '''没明白控制整个画布的意思'''
        newpos = self.rect.move(self.speed)
        self.rect = newpos


'''这里也可以将球通过for...in...的方式增加为多个，注意location和speed的对应关系（位置）'''
my_ball = ball('beach_ball.png', [20, 20], [10, 0])

'''设置按键不放时，连续输出控制；间隔时间100ms'''
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)

'''循环控制'''
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # '''键盘控制或这鼠标控制'''
        # elif event.type == pygame.KEYDOWN:
        #     '''有其他操作时，需要进行变化,上下控制'''
        #     if event.key == pygame.K_UP or event.key == pygame.K_w:
        #         my_ball.rect.top = my_ball.rect.top - 10
        #     elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        #         my_ball.rect.top = my_ball.rect.top + 10

        elif event.type == pygame.MOUSEMOTION:
            my_ball.rect.center == event.pos

    '''这里的主程序？screen.blit(对象？，位置？)，将原来所有删除？'''
    clock.tick(30)
    screen.blit(background, (0, 0))
    '''重新绘制球'''
    my_ball.move()
    screen.blit(my_ball.image, my_ball.rect)
    '''重新显示'''
    pygame.display.flip()

pygame.quit()
