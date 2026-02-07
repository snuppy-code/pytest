import pygame
import pygame_gui

class TestThorPy:
    def __init__(self,ctx):
        self.ctx = ctx
        # self.W = 1366
        # self.H = 768 #HD
        # W,H = 1920, 780 #Full HD
        # screen = pygame.display.set_mode((W, H))
        tp.set_default_font(("arialrounded", "arial", "calibri", "century"), 20)
        tp.init(ctx.screen, tp.theme_game2) #bind screen to gui elements and set theme
        
        bck = pygame.image.load(tp.fn("data/bck.jpg")) #load some background pic for testing
        bck = pygame.transform.smoothscale(bck, (ctx.w,ctx.h))
        
        def refresh():#some function that you call once per frame
            global my_element
            self.ctx.screen.blit(self.bck, (0,0))
            if my_pool.get_value():
                if tp.parameters.current_theme != my_pool.get_value():
                    print("replacing from", tp.parameters.current_theme,
                        "to", "theme_"+my_pool.get_value())
                    getattr(tp, "theme_"+my_pool.get_value())()
                    new_my_element = get_group(my_pool.get_value())
                    group.replace_child(my_element, new_my_element)
                    group.sort_children(gap=50)
                    group.center_on(self.ctx.screen)
                    my_element = new_my_element
        tp.call_before_gui(refresh) #tells thorpy to call refresh() before drawing gui.
        
        def get_group(group_name):
            button = tp.Button("Standard button")
            slider = tp.SliderWithText("Value :", 10, 80, 30, 100)
            text2 = tp.Text(tp.gametools.lorem_ipsum(3))
            text2.set_font_auto_multilines_width(self.w//4)
            ddlb = tp.DropDownListButton(("Camel", "Cat", "Dog", "Goat"))
            dropdownlist = tp.Labelled("Dropdown:", ddlb)
            check = tp.Labelled("Checkbox:",tp.Checkbox(True))
            radio = tp.Labelled("Radio:",tp.Radio(True))
            text_input = tp.Labelled("Text input:",tp.TextInput("", "Type text here"))
            slider = tp.SliderWithText("Value:", 10, 80, 30, 100, edit=True) #slider is labelled by default
            toggle = tp.TogglablesPool("TogglablesPool", ("Beginner", "Intermediate", "Advanced"), "Beginner")
            switch = tp.SwitchButtonWithText("Switch:", ("Foo","Bar")) #switch is labelled by default
            colorpicker =  tp.LabelledColorPicker("Colorpicker:", tp.ColorPicker())
            right_panel = tp.Box([button, text_input, slider, text2, dropdownlist, colorpicker,
                                    check, toggle, radio, switch])
            left_panel = tp.Group([tp.Button("Button "+str(i)) for i in range(12)], "grid")
            title_box = tp.Group([left_panel, right_panel], "h")
            return title_box

        tp.set_waiting_bar("Building elements...")

        my_pool = tp.TogglablesPool("", #no title
                                    tp.themes.all_themes, #possibilities
                                    tp.parameters.current_theme) #initial value

        my_element = get_group("theme_human")

        group = tp.Group([my_pool, my_element], gap=50)
        
        self.updater = group.get_updater()
        
    def onFrame(self,events):
        mouse_rel = pygame.mouse.get_rel()
        
        #update Thorpy elements and draw them
        self.updater.update(events=events,mouse_rel=mouse_rel) 