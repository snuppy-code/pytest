import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
w,h = screen.get_width(),screen.get_height()
clock = pygame.time.Clock()
dt_s = 0

# must be up here because later stuff calls it
def transition_scene_to(newSceneName):
    global current_scene
    current_scene = newSceneName

class OurFonts:
    def __init__(self):
        self.normal = pygame.font.SysFont(pygame.font.get_default_font(),50)
        self.funky = pygame.font.SysFont(pygame.font.get_default_font(),50)

class MainMenu:
    def __init__(self):
        pass
        
    def onFrame(self):
        # replace with background image 
        screen.fill((195, 176, 165))
        
        menu = pygame.Surface((w,h))
        
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(w/2-400/2,60+(150+20)*0,400,150),0,40)
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(w/2-400/2,60+(150+20)*1,400,150),0,40)
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(w/2-400/2,60+(150+20)*2,400,150),0,40)
        
        screen.blit(menu)
        

class Example_RedDotWASD:
    def __init__(self):
        self.player_pos = pygame.Vector2(w/2,h/2)
        
    def onFrame(self):
        screen.fill("black")
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
        
        # initial variables to get width/height that doesn't change as text changes
        # fixes text jittering during loading
        t = f"Loading progress: {self.loading_progress:.2f}%"
        s = self.loading_font.render(t,True,(255,255,255))
        self.initial_w = s.width
        self.initial_h = s.height
        
        
    def onFrame(self):
        if self.loading_progress >= 100:
            transition_scene_to("MainMenu")
        else:
            self.loading_progress += 60 * dt_s
        
        screen.fill("black")
        
        print("LoadingScene onFrame called!")
        
        t = f"Loading progress: {self.loading_progress:.2f}%"
        s = self.loading_font.render(t,True,(255,255,255))
        p = (w/2-self.initial_w/2,h/2-self.initial_h/2)
        screen.blit(s,p)

scenes = {
    "LoadingScreen": LoadingScreen(),
    "MainMenu": MainMenu(),

}
current_scene = "MainMenu"

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