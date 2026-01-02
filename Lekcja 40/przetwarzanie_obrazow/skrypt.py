import cv2
import numpy as np

def show_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_image(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    print(img)
    print(type(img))
    print(img.shape)
    # show_image(img)
    return img

image = read_image("image.jpg")

# show_image(cv2.flip(image, -1))

# show_image(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))


def sepia(img):
    for row in range(img.shape[0]):
        for column in range(img.shape[1]):
            B = img[row][column][0]
            G = img[row][column][1]
            R = img[row][column][2]
            # B
            img[row][column][0] = min(255, (0.272 * R + 0.534 * G + 0.131 * B))
            #G
            img[row][column][1] = min(255, (0.349  * R + 0.686 * G + 0.168 * B))
            # R
            img[row][column][2] = min(255, (0.393 * R + 0.769 * G + 0.189 * B))
    return np.array(img, dtype=np.uint8)
show_image(sepia(image))