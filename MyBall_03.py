#学习《python入门书籍01--父与子的编程之旅：与小卡特一起学Python（高清中文版）》
#创建球碰撞

import pygame,sys
from random import *

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file) #编写程序时出现self.image.load(image_file)错误
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
        
"""撞击使用的是rect，非像素"""
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

def animate(group):
    screen.fill([255, 255, 255])
    for ball in group:
        group.remove(ball)
        if pygame.sprite.spritecollide(ball, group, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]

        group.add(ball)
        ball.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    # pygame.time.delay(20)


"""主程序"""
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen_name = pygame.display.set_caption('球之间的碰撞')
screen.fill([255, 255, 255])
                                    #学习时，这里程序多写 pygame.display.flip()导致报错
img_file = "beach_ball.png"
clock = pygame.time.Clock()         #line 34删除pygame.time.delay()后使用的
group = pygame.sprite.Group()

# balls = []
for row in range(0, 2):
    for column in range(0, 2):
        location = [column * 180 + 10, row * 180 + 10]
        speed = [choice([-2, 5]), choice([-2, 3])]
        ball = MyBallClass(img_file, location, speed)
        # balls.append(ball)
        group.add(ball)
        
 """这里是创建多个程序运行时使用的，此处注释掉了"""
# for ball in balls:
#     screen.blit(ball.image, ball.rect)
# pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           # 编写时会，注意防止出现pygame.quit()的情况
            frame_rate = clock.get_fps()        # 检测帧数
            print("frame rate = ", frame_rate)  # 检测帧数输出
            running = False
            
    """注释掉程序主要是创建多个球时使用"""
    # pygame.time.delay(20)
    # screen.fill([255, 255, 255])
    # for ball in balls:
    #     ball.move()
    #     screen.blit(ball.image, ball.rect)
    # pygame.display.flip()
    animate(group)
    clock.tick(30)                            #clock.tick控制帧率

pygame.quit()
