from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from game_classes import *


class DisplayModule:
    oval = None
    test_canvas = None
    root = None
    images_library = None
    opened_library = None
    game = None

    def __init__(self):
        self.images_library = []
        self.opened_library = {}

    def start_display(self, game):
        self.game = game
        self.root = Tk()
        self.root.geometry("1650x850")
        self.root.title("CATAN")

        canvas = Canvas(self.root, bg="tomato2", width=1650, height=850)
        self.test_canvas = canvas
        canvas.place(x=0, y=0)
        self.oval = canvas.create_oval(10, 10, 25, 25, fill="purple1")

        # draw all elements
        for drawable in Element.icons:
            self.draw_element(canvas, drawable)

        testButton = Button(self.root, text="press", command=lambda: game.HighlightSomething())
        testButton.place(x=0, y=0)
        self.root.mainloop()

    def draw_element(self, canvas, drawable):
        loaded_image: object
        if drawable.image_location in self.opened_library:
            loaded_image = self.opened_library[drawable.image_location]
        else:
            loaded_image = Image.open(drawable.image_location)
            self.opened_library[drawable.image_location] = loaded_image
        image = ImageTk.PhotoImage(loaded_image)
        if image not in self.images_library:
            self.images_library.append(image)
        canvas.create_image(drawable.localX, drawable.localY,
                            image=image, anchor=NW)

    def refresh_display(self):
        # draw all elements
        for drawable in Element.icons:
            self.draw_element(self.test_canvas, drawable)
