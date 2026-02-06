import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
dt_s = 0

class MainMenu:
    def __init__(self):
        self.player_pos = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
        
    def onFrame(self):
        print("MainMenu onFrame called!")
        pygame.draw.circle(screen, "red", self.player_pos, 40)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_pos += pygame.Vector2(0,-200) * dt_s
        if keys[pygame.K_s]:
            self.player_pos += pygame.Vector2(0,200) * dt_s
        if keys[pygame.K_a]:
            self.player_pos += pygame.Vector2(-200,0) * dt_s
        if keys[pygame.K_d]:
            self.player_pos += pygame.Vector2(200,0) * dt_s

class LoadingScreen:
    def __init__(self):
        self.loading_progress = 0
        self.loading_font = pygame.font.SysFont(pygame.font.get_default_font(),50)
        
    def onFrame(self):
        if self.loading_progress >= 100:
            pass #cleanup? and transition
        else:
            self.loading_progress += 5 * dt_s
        
        screen.fill("black")
        print("LoadingScene onFrame called!")
        t = "Loading progress: "+str(self.loading_progress)+"%"
        text_surface = self.loading_font.render(t,True,(255,255,255))
        screen.blit(text_surface)

scenes = {
    "MainMenu": MainMenu(),
    "LoadingScreen": LoadingScreen(),
    
}
current_scene = "LoadingScreen"

running = True
while running:
    
    # allow closing the window,,
    # .get gives a list of all events since last call
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # call onFrame callback for each scene
    scenes[current_scene].onFrame()
    

    # renders allat to the screen !
    pygame.display.flip()
    dt_s = clock.tick(144) / 1000
    print(dt_s)

pygame.quit()