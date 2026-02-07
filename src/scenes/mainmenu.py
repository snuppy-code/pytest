import pygame
import pygame_gui # type: ignore

class MainMenu:
    def __init__(self,ctx):
        self.ctx = ctx
        self.hello_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((350, 275), (100, 50)),
                text='Say Hello',
                manager=self.ctx.manager
            )
    
    def onEnter(self):
        pass

    def onExit(self):
        pass
    
    def onFrame(self,events):
        print("Mainmenu onframe!!")
        w = self.ctx.w
        h = self.ctx.h
        dt_s = self.ctx.dt_s
        
        # replace with background image 
        self.ctx.screen.fill((195, 176, 165))
        
        menu = pygame.Surface((self.ctx.w,self.ctx.h))
        
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*0,400,150),0,40)
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*1,400,150),0,40)
        pygame.draw.rect(menu,(222, 212, 203),pygame.Rect(self.ctx.w/2-400/2,60+(150+20)*2,400,150),0,40)
        
        self.ctx.screen.blit(menu)
        
        for event in events:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.hello_button:
                    print('Hello World!')
        
        