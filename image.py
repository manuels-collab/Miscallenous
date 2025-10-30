from tkinter import *
from track_iss import IssPosition
import time


class Map:
    position = IssPosition()
    def __init__(self, position):
        self.position = position
        self.window = Tk()
        self.window.title('ISS Viewer')
        self.window.maxsize(width=1000, height=600)
        self.canvas = Canvas(width=1730, height=765)
        self.image_file = PhotoImage(file="my_map.png")
        self.image = self.canvas.create_image(200, 200 , image=self.image_file)
        self.tracker = '🟢'
        self.canvas_text = self.canvas.create_text(position.latitude + 1000 , position.longitude + 1000, text=self.tracker)
        self.canvas.pack()

        self.move_tracker()
        self.window.mainloop()


    def move_tracker(self):
        splitted_text = self.position.get_tracking_state()
        latitude =  float(splitted_text[0])
        longitude = float(splitted_text[1])
        print(latitude, longitude)
        self.canvas.move(self.canvas_text, latitude, longitude)
        self.window.after(3000, self.move_tracker)


