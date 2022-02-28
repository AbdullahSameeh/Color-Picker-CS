import cv2
import numpy as np
import pandas as pd

color_preview = np.zeros((150, 150, 3), np.uint8)
color_selected = np.zeros((150, 150, 3), np.uint8)

# sample image path
img_path = "rgb.png"

# read sample image
img = cv2.imread(img_path)

# Mouse Callback function
def show_color(event, x, y, flags, param):
    G = int(img[y, x][1])
    B = int(img[y, x][0])
    R = int(img[y, x][2])
    color_preview[:] = (B, G, R)

    if event == cv2.EVENT_LBUTTONDOWN:
        color_selected[:] = (B, G, R)
        B = color_preview[10, 10][0]
        G = color_preview[10, 10][1]
        R = color_preview[10, 10][2]

        # Reading csv file with pandas and giving names to each column
        index = ["color_name", "hex", "R", "G", "B"]
        csv = pd.read_csv('colors.csv', names=index, header=None)
        res = ""
        if(len(hex(R)[2:]) == 1):
            res = res + hex(R)[2:] + "0"
        else:
            res = res + hex(R)[2:]
        if (len(hex(G)[2:]) == 1):
            res = res + hex(G)[2:] + "0"
        else:
            res = res + hex(G)[2:]
        if (len(hex(B)[2:]) == 1):
            res = res + hex(B)[2:] + "0"
        else:
            res = res + hex(B)[2:]

        output = "Red=" + str(R) + " Green=" + str(G) + " Blue=" + str(B)
        print("\n\n^^^^^^^^^^^^^^^^^^^^^\n\n")
        print(output)
        res = "#" + res.upper()
        print(csv[csv["hex"] == res])


# live update color with cursor
cv2.namedWindow('color_preview',cv2.WINDOW_NORMAL)
cv2.resizeWindow("color_preview", 50, 50)

# Show selected color when left mouse button pressed
cv2.namedWindow('color_selected',cv2.WINDOW_NORMAL)
cv2.resizeWindow("color_selected", 50, 50)

# image window for sample image
cv2.namedWindow('image')


# mouse call back function declaration
cv2.setMouseCallback('image', show_color)

# while loop to live update
while (1):

    cv2.imshow('image', cv2.resize(img, (318, 312)))
    cv2.imshow('color_preview', color_preview)
    cv2.imshow('color_selected', color_selected)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
