import tkinter as tk

import astra_test_driver
import cv2

switch_flag = False
shoot_flag = False


def switchCallBack():
    global switch_flag
    switch_flag = True


def shootCallBack():
    global shoot_flag
    shoot_flag = True


root = tk.Tk()
b = tk.Button(root, text="Enable Switch", command=switchCallBack)
b.pack()

b2 = tk.Button(root, text="Shoot Ball", command=shootCallBack)
b2.pack()

d = astra_test_driver.Driver()

while True:
    d.run(view=True)
    if switch_flag:
        d.switch()
        switch_flag = False
    if shoot_flag:
        d.shooter()
        shoot_flag = False
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

    root.update()
    root.update_idletasks()
