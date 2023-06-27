import pygame
#from gi.repository import Gtk

pygame.init()
#width = Gtk.screen_width()
#height = Gtk.screen_height()
screen = pygame.display.set_mode((1080, 720))
screen.fill((0, 0, 35))
color = (0, 255, 0)
start_pos = (0, 250)
end_pos = (250, 800)
pygame.display.set_caption("Disnosour Game")
pygame.display.update()
while True:
    for event in pygame.event.get():
        # print(event)
        #pygame.draw.line(screen, color, start_pos, end_pos, 1)

        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
