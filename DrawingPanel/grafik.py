from drawingpanel import *


def car(x=10, y=10):
    panel.canvas.create_polygon(0+x, 10+y, 10+x, 0+y, 180+x, 0+y, 190+x,
                                10+y, 190+x, 80+y, 180+x, 90+y, 10+x, 90+y, 0+x, 80+y, fill="cornflower blue", outline="blue")
    panel.canvas.create_oval(20+x, 65+y, 60+x, 105+y,
                             fill="gray20", outline="gray7")
    panel.canvas.create_oval(30+x, 75+y, 50+x, 95+y,
                             fill="gray30", outline="")
    panel.canvas.create_oval(130+x, 65+y, 170+x, 105+y,
                             fill="gray20", outline="gray7")
    panel.canvas.create_oval(140+x, 75+y, 160+x, 95+y,
                             fill="gray30", outline="")
    panel.canvas.create_rectangle(
        120+x, 20+y, 190+x, 50+y, fill="LightSkyBlue1", outline="blue")


def sign(x=10, y=10, ):
    panel.canvas.create_polygon(0+x, 20+y, 20+x, 0+y, 60+x, 0+y, 80+x,
                                20+y, 80+x, 60+y, 60+x, 80+y, 20+x, 80+y, 0+x, 60+y, fill="firebrick", outline="IndianRed2")
    panel.canvas.create_rectangle(
        35+x, 80+y, 45+x, 150+y, fill="IndianRed3")


def background():
    panel.canvas.create_rectangle(
        0, 250, 500, 300, fill="lightGrey", outline="")


panel = DrawingPanel(500, 300)
panel.set_background("linen")

car_speed = 1
sign_speed = 3
car_x = 0
sign_x = 600

for i in range(0, 100):
    panel.clear()
    sign_x -= sign_speed
    sign(sign_x, 100)
    background()
    car_x += car_speed
    car(car_x, 180)
    panel.sleep(10)
