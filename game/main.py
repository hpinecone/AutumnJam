import pygame
import pygame_gui
import os


def run():
    pygame.init()

    info = pygame.display.Info()
    screen_width = info.current_w #original screen width
    screen_height = info.current_h #original screen height

    #os buttons would be cut off to remedy this implement this (resize button, exit button, etc)
    #min max
    MIN_W, MIN_H = 400, 250 #accounts for resolutions that are too small
    uscreen_w = max(MIN_W, int(screen_width * 0.9)) #updated screen width to account for buttons missing
    uscreen_h = max(MIN_H, int(screen_height * 0.9)) #updated screen height

    """
    add resolution scale here later
    """

    print(f"Detected resolution: {screen_width} X {screen_height}")
    print(f"Updated resolution(Protected): {uscreen_w} X {uscreen_h}")

    pygame.display.set_caption('Autumn') #change later
    window_surface = pygame.display.set_mode((uscreen_w, uscreen_h), pygame.RESIZABLE)

    background = pygame.Surface((uscreen_w, uscreen_h))
    background.fill(pygame.Color("#676767"))

    manager = pygame_gui.UIManager((uscreen_w, uscreen_h))

    clock = pygame.time.Clock()

    is_running = True

    tick = 0 #temp world tick

    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

                manager.process_events(event)
            
            manager.update(time_delta)

            #time manager (tick)
            tick+=1
            if(tick < 30):
                print(tick, "tick") #ensure game launches

            window_surface.blit(background, (0,0))
            manager.draw_ui(window_surface)

            pygame.display.flip() #flip over update for large scale things



#keep here for trash collection
pygame.quit()