import cv2
import numpy as np
import os
import operator

def autodetect():
    quadrant_scores = {"1": 0, "2": 0, "3": 0, "4": 0}

    img = cv2.imread("temp.png", 0)
    img2 = img.copy()
    files = [os.path.join("images", f) for f in os.listdir("images") if os.path.isfile(os.path.join("images", f))]

    for template_image in files:
        img = img2.copy()

        template = cv2.imread(template_image, 0)
        w, h = template.shape[::-1]

        # apply template match
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # determine quadrants
        width, height = img.shape[::-1]
        mid_width = width / 2
        mid_height = height / 2

        selected_mid_x = ((bottom_right[0] - top_left[0]) / 2) + top_left[0]
        selected_mid_y = ((top_left[1] - bottom_right[1]) / 2) + bottom_right[1]

        if selected_mid_x < mid_width and selected_mid_y < mid_height:
            quadrant = "1"
        elif selected_mid_x > mid_width and selected_mid_y < mid_height:
            quadrant = "2"
        elif selected_mid_x < mid_width and selected_mid_y > mid_height:
            quadrant = "3"
        else:
            quadrant = "4"

        quadrant_scores[quadrant] += max_val

    for score in quadrant_scores:
        quadrant_scores[score] = quadrant_scores[score] / len(files)

    quad_key = max(quadrant_scores.items(), key=operator.itemgetter(1))[0]
    return quad_key, str(int(quadrant_scores[quad_key]*100)) + "%"
