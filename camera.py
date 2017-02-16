import cv2
from PIL import Image, ImageChops
import time
import numpy

cv2.namedWindow("lll")
cap = cv2.VideoCapture(1)

reference = None

while cap.isOpened():
    ret, img = cap.read()
    image = Image.fromarray(img)

    if reference is not None:
        difference = ImageChops.difference(image, reference)

        # image.save("image.png")
        # reference.save("reference.png")
        # difference.save("difference.png")

        grey_difference = difference.convert("L")
        # grey_difference.save("difference.png")

        # binary_difference = difference.convert("1")
        # binary_difference.save("difference.png")

        image_to_show = grey_difference

        im_arr = numpy.fromstring(image_to_show.tobytes(), dtype=numpy.uint8)
        im_arr = im_arr.reshape((image_to_show.size[1], image_to_show.size[0], 1))

        cv2.imshow("lll", im_arr)

    reference = image

    # cv2.imshow("lll", img)
    k = cv2.waitKey(10)
    if k == 27:
        break

    # time.sleep(0.01)
