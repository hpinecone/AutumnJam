import pygame
import pygame_gui


pygame.init()

info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

"""
add resolution scale here later
add resizable option later
"""

print("Detected resolution: ", screen_width, " X ", screen_height)

pygame.display.set_caption('Autumn') #change later
window_surface = pygame.display.set_mode((screen_width,screen_height))

background = pygame.Surface((screen_width,screen_height))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((screen_width,screen_height))

clock = pygame.time.Clock()

is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

            manager.process_events(event)
        
        manager.update(time_delta)

        window_surface.blit(background, (0,0))
        manager.draw_ui(window_surface)

        pygame.display.update()