class Farmplot:
    def __init__(self, ctx):
        self.ctx = ctx

    def onEnter(self):
        pass

    def onExit(self):
        pass

    def onFrame(self, events):
        self.ctx.vscreen.blit(self.ctx.images["farmplot.png"])

    def alwaysTick(self, events):
        pass

'''

'''