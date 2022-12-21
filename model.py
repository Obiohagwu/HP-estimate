# Path: main.py
import sdl2
import sdl2.ext
from FeedDisplay import FeedDisplay

W = 1920//2
H = 1080//2

display = FeedDisplay(W, H)


def frameProcessor(img):
    img = cv2.resize(img, (width, height))


if __name__ == "__main__":
    main = Main()
    main.run()

