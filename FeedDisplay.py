import sdl2
import sdl2.ext


class FeedDisplay(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = sdl2.ext.Window("Feed", size=(width, height))
        self.window.show()

    def update(self, data):
        self.window.refresh()



