import pygame
import pygame.locals
import pygame_gui
from display import Display
import files_functions
import predict_one
import os

class ExpressionModify(object):
    def __init__(self):
        pygame.init()
        self.display = Display()
        self.fps_clock = pygame.time.Clock()


    def handle_events(self):

        time_delta = self.fps_clock.tick(1000)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                    if event.ui_element == self. display.loadButton:
                        self.__init__()
                        self.display.neutral_picture=files_functions.pick_photo()
                        self.display.modified_picture = None
                        self.display.draw()
                        f = open("tmp/neutral_path.txt", "w")
                        f.write(self.display.neutral_picture)
                        f.close()


                    if event.ui_element == self. display.happyButton:
                        self.__init__()
                        f = open("tmp/neutral_path.txt", "r")
                        if (os.stat("tmp/neutral_path.txt").st_size != 0):
                            name= f.read()
                            self.display.modified_picture=predict_one.transform_image(name,"happy")
                            f2=open("tmp/modified_path.txt","w")
                            f2.write(self.display.modified_picture)
                            self.display.neutral_picture=name
                            f2.close()
                        self.display.draw()
                        f.close()

                    if event.ui_element == self. display.sadButton:
                        self.__init__()
                        f = open("tmp/neutral_path.txt", "r")
                        if (os.stat("tmp/neutral_path.txt").st_size != 0):
                            name = f.read()
                            self.display.modified_picture = predict_one.transform_image(name, "sad")
                            f2 = open("tmp/modified_path.txt", "w")
                            f2.write(self.display.modified_picture)
                            self.display.neutral_picture = name
                            f2.close()
                        self.display.draw()
                        f.close()

                    if event.ui_element == self. display.fearButton:
                        self.__init__()
                        f = open("tmp/neutral_path.txt", "r")
                        if (os.stat("tmp/neutral_path.txt").st_size != 0):
                            name = f.read()
                            self.display.modified_picture = predict_one.transform_image(name, "fear")
                            f2 = open("tmp/modified_path.txt", "w")
                            f2.write(self.display.modified_picture)
                            self.display.neutral_picture = name
                            f2.close()
                        self.display.draw()
                        f.close()

                    if event.ui_element == self. display.angerButton:
                        self.__init__()
                        f = open("tmp/neutral_path.txt", "r")
                        if (os.stat("tmp/neutral_path.txt").st_size != 0):
                            name = f.read()
                            self.display.modified_picture = predict_one.transform_image(name, "anger")
                            f2 = open("tmp/modified_path.txt", "w")
                            f2.write(self.display.modified_picture)
                            self.display.neutral_picture = name
                            f2.close()
                        self.display.draw()
                        f.close()

                    if event.ui_element == self. display.surpriseButton:
                        self.__init__()
                        f = open("tmp/neutral_path.txt", "r")
                        if (os.stat("tmp/neutral_path.txt").st_size != 0):
                            name = f.read()
                            self.display.modified_picture = predict_one.transform_image(name, "surprised")
                            f2 = open("tmp/modified_path.txt", "w")
                            f2.write(self.display.modified_picture)
                            self.display.neutral_picture = name
                            f2.close()
                        self.display.draw()
                        f.close()

                    if event.ui_element == self. display.disgustButton:
                        self.__init__()
                        f = open("tmp/neutral_path.txt", "r")
                        if (os.stat("tmp/neutral_path.txt").st_size != 0):
                            name = f.read()
                            self.display.modified_picture = predict_one.transform_image(name, "disgust")
                            f2 = open("tmp/modified_path.txt", "w")
                            f2.write(self.display.modified_picture)
                            self.display.neutral_picture = name
                            f2.close()
                        self.display.draw()
                        f.close()

                    if event.ui_element == self. display.infoButton:
                        files_functions.display_info()



            self. display.manager.process_events(event)

        self. display.manager.update(time_delta)
        self. display.manager.draw_ui(self. display.surface)
        pygame.display.update()

        return False

    def run(self):
        self.display.draw()
        while not self.handle_events():
            pass

if __name__ == '__main__':
    app = ExpressionModify()
    app.run()
