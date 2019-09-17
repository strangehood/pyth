
def background():
    brushColor(33, 33, 120)
    penColor(33, 33, 120)
    polygon([(0, 0), (790, 0), (790, 120), (0, 120)])

    brushColor(141, 95, 211)
    penColor(141, 95, 211)
    polygon([(0, 120), (790, 120), (790, 180), (0, 180)])

    brushColor(205, 135, 222)
    penColor(205, 135, 222)
    polygon([(0, 180), (790, 180), (790, 280), (0, 280)])

    brushColor(222, 135, 170)
    penColor(222, 135, 170)
    polygon([(0, 280), (790, 280), (790, 430), (0, 430)])

    brushColor(255, 153, 85)
    penColor(255, 153, 85)
    polygon([(0, 430), (790, 430), (790, 550), (0, 550)])

    brushColor(0, 102, 128)
    penColor(0, 102, 128)
    polygon([(0, 550), (790, 550), (790, 1100), (0, 1100)])


def albatrols():
   penColor(0, 0, 0)
   


from graph import *

windowSize(790, 1100)
canvasSize(790, 1100)

run()
