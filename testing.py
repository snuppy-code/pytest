import pygame # type: ignore

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
        self.loadingprogress = 0
        
    def onFrame(self):
        print("LoadingScene onFrame called!")
        pygame.draw.circle(screen, "blue", (200,500), 50)

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
    for scene in scenes:
        scene.onFrame()
    

    # renders allat to the screen !
    pygame.display.flip()
    dt_s = clock.tick(144) / 1000
    print(dt_s)

pygame.quit()