#encoding = utf-8

import turtle as t
import time
t.color("red", "yellow")
t.speed(10)
t.begin_fill()
for i in range(50):
    t.forward(200)
    t.left(170)
t.end_fill()
time.sleep(10)