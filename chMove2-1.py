"""Character moving level 2-1 _HR (10/11)"""

import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("야마다상의 마네키네코 탈환 작전 Level 2-1")
    screen = pygame.display.set_mode((640, 360))
    clock = pygame.time.Clock()
    img_bg = pygame.image.load("image/back2-1.png")
    img_chara = [
 
        pygame.image.load("image/mychr6.png"),
        pygame.image.load("image/mychr7.png")
    ]
    tmr = 0

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((640, 360))

        x = tmr%160
        for i in range(5):
            screen.blit(img_bg, [i*60-x, 0])
        screen.blit(img_chara[tmr%2], [124, 220])
        pygame.display.update()
        clock.tick(5)

if __name__ == '__main__':
    main()