import pygame
import pygame.locals
import pygame_gui
from constants import *

class Display(object):
    def __init__(self):
        self.surface = pygame.display.set_mode(RESOLUTION, 0, 32)
        pygame.display.set_caption('Changing facial expression')
        self.background = pygame.Surface(RESOLUTION)

        self.manager = pygame_gui.UIManager(RESOLUTION)

        self.loadButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_LOADBUTTON, SIZE_LOADBUTTON),
            text='Load picture',
            manager=self.manager)
        
        self.happyButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_HAPPYBUTTON, SIZE_HAPPYBUTTON),
            text='HAPPY',
            manager=self.manager)
        
        self.sadButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_SADBUTTON, SIZE_SADBUTTON),
            text='SAD',
            manager=self.manager)
        
        self.disgustButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_DISGUSTBUTTON, SIZE_DISGUSTBUTTON),
            text='DISGUST',
            manager=self.manager)

        self.angerButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_ANGERBUTTON, SIZE_ANGERBUTTON),
            text='ANGER',
            manager=self.manager)

        self.fearButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_FEARBUTTON, SIZE_FEARBUTTON),
            text='FEAR',
            manager=self.manager)

        self.surpriseButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_SURPRISEBUTTON, SIZE_SURPRISEBUTTON),
            text='SURPRISE',
            manager=self.manager)

        self.infoButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(POSITION_INFOBUTTON, SIZE_INFOBUTTON),
            text='INFO',
            manager=self.manager)


        self.neutral_picture = None
        self.modified_picture = None


    def draw(self):

        if self.neutral_picture:
            img = pygame.image.load(self.neutral_picture)
            img = pygame.transform.scale(img, SIZE_PICTURES)
            self.surface.blit(img, POSITION_NEUTRALPICTURE)

        if self.modified_picture:
            img = pygame.image.load(self.modified_picture)
            img = pygame.transform.scale(img, SIZE_PICTURES)
            self.surface.blit(img, POSITION_MODIFIEDPICTURE)

        pygame.font.init()

        myfont = pygame.font.SysFont('Book Antiqua', 24)
        textsurface = myfont.render('Pick an emotion', False,
                                    FONT_COLOR)

        self.surface.blit(textsurface, POSITION_TASK)

        myfont_info = pygame.font.SysFont('Book Antiqua', 12)
        textsurface_info = myfont_info.render(TEXT_INFO, False,
                                    FONT_COLOR)
        self.surface.blit(textsurface_info, POSITION_INFO)


        pygame.display.update()