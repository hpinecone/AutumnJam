import pygame
import pygame_gui


pygame.init()

info = pygame.display.Info()
screen_width = info.current_w #original screen width
screen_height = info.current_h #original screen height

#os buttons would be cut off to remedy this implement this (resize button, exit button, etc)
uscreen_w = screen_width * 90 #updated screen width to account for buttons missing
uscreen_h = screen_height * 90 #updated screen height

"""
add resolution scale here later
"""

print("Detected resolution: ", screen_width, " X ", screen_height)
print("Updated resolution: ", uscreen_w, " X ", uscreen_h)

pygame.display.set_caption('Autumn') #change later
window_surface = pygame.display.set_mode((uscreen_w, uscreen_h), pygame.RESIZABLE)

background = pygame.Surface((uscreen_w, uscreen_h))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((uscreen_w, uscreen_h))

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

pygame.quit()