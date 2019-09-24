def bird(x0: int, y0: int):
    background()
    nose(0 + x0, -425 + y0)
    tail(0 + x0 + x0, -420 + y0)
    wing(60 + x0, -450 + y0)
    wing(0 + x0, -430 + y0)
    albatrols(0 + x0, -125 + y0)
    leg(40 + x0, -475 + y0)
    leg(0 + x0, -450 + y0)


def nose(xnose: int, ynose: int):
    penColor('black')
    brushColor(255, 230, 128)
    polygon(([(570 + xnose, 792 + ynose), (571 + xnose, 786 + ynose), (608 + xnose, 780 + ynose),
              (628 + xnose, 779 + ynose), (643 + xnose, 796 + ynose), (637 + xnose, 793 + ynose)]))
    polygon(([(569 + xnose, 786 + ynose), (580 + xnose, 790 + ynose), (603 + xnose, 793 + ynose),
              (633 + xnose, 793 + ynose), (643 + xnose, 790 + ynose), (629 + xnose, 807 + ynose),
              (565 + xnose, 799 + ynose)]))


def tail(xtail: int, ytail: int):
    penColor('black')
    brushColor('white')
    polygon([(162 + xtail, 807 + ytail), (202 + xtail, 713 + ytail), (280 + xtail, 839 + ytail)])


def leg(xleg: int, yleg: int):
    feet(xleg, yleg)
    penSize(40)
    penColor('white')
    brushColor('white')
    line(315 + xleg, 853 + yleg, 358 + xleg, 928 + yleg)
    penSize(1)
    circle(315 + xleg, 853 + yleg, 20)
    circle(358 + xleg, 928 + yleg, 20)
    penSize(20)
    line(350 + xleg, 926 + yleg, 428 + xleg, 944 + yleg)
    penSize(1)
    circle(428 + xleg, 944 + yleg, 9)


def feet(xfeet: int, yfeet: int):
    penColor(0, 0, 0)
    brushColor(255, 230, 128)
    polygon(([(428 + xfeet, 954 + yfeet), (434 + xfeet, 958 + yfeet), (429 + xfeet, 963 + yfeet),
              (428 + xfeet, 985 + yfeet),
              (433 + xfeet, 988 + yfeet), (435 + xfeet, 989 + yfeet), (440 + xfeet, 961 + yfeet),
              (445 + xfeet, 957 + yfeet),
              (454 + xfeet, 958 + yfeet), (496 + xfeet, 974 + yfeet), (474 + xfeet, 957 + yfeet),
              (461 + xfeet, 955 + yfeet),
              (478 + xfeet, 954 + yfeet), (500 + xfeet, 964 + yfeet), (478 + xfeet, 950 + yfeet),
              (463 + xfeet, 951 + yfeet),
              (473 + xfeet, 946 + yfeet), (488 + xfeet, 946 + yfeet), (498 + xfeet, 952 + yfeet),
              (494 + xfeet, 944 + yfeet),
              (484 + xfeet, 939 + yfeet), (474 + xfeet, 938 + yfeet), (463 + xfeet, 940 + yfeet),
              (452 + xfeet, 944 + yfeet),
              (442 + xfeet, 949 + yfeet), (438 + xfeet, 946 + yfeet)]))


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


def wing(xwing: int, ywing: int):  # a,b
    penColor(0, 0, 0)
    brushColor(255, 255, 255)
    polygon(
        ([(54 + xwing, 645 + ywing), (56 + xwing, 651 + ywing), (60 + xwing, 657 + ywing), (64 + xwing, 663 + ywing),
          (95 + xwing, 700 + ywing), (102 + xwing, 708 + ywing), (117 + xwing, 716 + ywing), (137 + xwing, 721 + ywing),
          (169 + xwing, 725 + ywing), (183 + xwing, 729 + ywing), (196 + xwing, 736 + ywing),
          (210 + xwing, 748 + ywing),
          (223 + xwing, 766 + ywing), (243 + xwing, 781 + ywing), (266 + xwing, 794 + ywing),
          (345 + xwing, 814 + ywing),
          (340 + xwing, 773 + ywing), (333 + xwing, 752 + ywing), (322 + xwing, 727 + ywing),
          (309 + xwing, 706 + ywing),
          (295 + xwing, 690 + ywing), (277 + xwing, 686 + ywing), (244 + xwing, 685 + ywing),
          (220 + xwing, 687 + ywing),
          (198 + xwing, 687 + ywing), (177 + xwing, 685 + ywing), (163 + xwing, 684 + ywing),
          (143 + xwing, 681 + ywing),
          (116 + xwing, 674 + ywing), (91 + xwing, 664 + ywing), (79 + xwing, 657 + ywing), (68 + xwing, 650 + ywing),
          (60 + xwing, 644 + ywing)]))


def albatrols(xalbat: int, yalbat: int):
    penColor(255, 255, 255)
    c.create_oval(250 + xalbat, 460 + yalbat, 450 + xalbat, 560 + yalbat, fill='white', outline='white')
    c.create_oval(420 + xalbat, 490 + yalbat, 520 + xalbat, 530 + yalbat, fill='white', outline='white')
    c.create_oval(500 + xalbat, 460 + yalbat, 570 + xalbat, 510 + yalbat, fill='white', outline='white')
    c.create_oval(540 + xalbat, 480 + yalbat, 555 + xalbat, 490 + yalbat, fill='black', outline='white')


def main(movement: int):
    flag = False
    bird(movement, movement)
    if flag == True:
        movement += 5
    else:
        movement -= 5
    if movement > 40:
        flag = False
    elif movement < 0:
        flag = True
    return movement

def nothing():
    pass


from graph import *

c = canvas()
windowSize(790, 1100)
canvasSize(790, 1100)
mov=0
onTimer(nothing, 10)
main(mov)
mov = main(mov)
run()