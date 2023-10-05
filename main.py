import os
from ultralytics import YOLO
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Canvas, Tk, Label, mainloop
import cv2


def Predict():
    model = YOLO("Modelv2.pt")
    results = model.predict("Unseen data.mp4", conf=0.7, stream=True)
    for result in results:
        img = result.orig_img
        height, width, _ = img.shape
        counter = 1
        for i in range(11, height, 23):
            text = str(counter)
            counter += 1
            img = cv2.putText(img, text, (0, i), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        for i in range(11, height, 23):
            text = str(counter)
            counter += 1
            img = cv2.putText(img, text, (100, i), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        for i in range(18, height, 23):
            text = str(counter)
            counter += 1
            img = cv2.putText(img, text, (130, i), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

        for i in range(18, height, 23):
            text = str(counter)
            counter += 1
            img = cv2.putText(img, text, (230, i), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        freespots = []
        for box in result.boxes:
            x = box.xyxy.tolist()
            start_point = (int(x[0][0]), int(x[0][1]))
            end_point = (int(x[0][2]), int(x[0][3]))
            midpoint = int(x[0][1]) + ((int(x[0][3]) - int(x[0][1])) / 2)
            if int(x[0][0]) <= 53:
                freespots.append(round((midpoint - 8) / 23) + 1)
            elif 54 <= int(x[0][0]) <= 120:
                freespots.append(round((midpoint - 8) / 23) + 12)
            elif 135 <= int(x[0][0]) <= 193:
                freespots.append(round((midpoint - 11) / 24) + 23)
            elif 194 <= int(x[0][0]):
                freespots.append(round((midpoint - 11) / 24) + 34)
            color = (0, 255, 0)
            thickness = 1
            img = cv2.rectangle(img, start_point, end_point, color, thickness)
        imS = cv2.resize(img, (500, 500))
        img2 = ImageTk.PhotoImage(image=Image.fromarray(imS))
        label.configure(image=img2)
        label.image = img2
        string_variable.set(len(result.boxes))
        freespots.sort()
        string_variable2.set(str(freespots))
        Tk.update(root)
    exit()


root = Tk()
root.geometry("700x700")
canvas = Canvas(root, width=1500, height=700)
canvas.pack()
root.eval('tk::PlaceWindow . center')

label = Label(canvas)
label.pack()
string_variable = tk.StringVar(canvas, str(""))
string_variable2 = tk.StringVar(canvas, str(""))

button = tk.Button(canvas, text='Start Video', width=50, command=Predict, font=('Arial', 20))
button.pack()
w1 = Label(canvas, text="available slots : ", font=('Arial', 20))
w1.pack()
w2 = tk.Label(canvas, textvariable=string_variable, font=('Arial', 20))
w2.pack()
w3 = Label(canvas, text="Numbers of free spots : ", font=('Arial', 20))
w3.pack()
w4 = tk.Label(canvas, textvariable=string_variable2, font=('Arial', 20))
w4.pack()

mainloop()
