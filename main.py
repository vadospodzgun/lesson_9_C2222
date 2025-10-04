import cv2
from PIL import Image

image_path = 'cat1.jpg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade. detectMultiScale(image)
#print(cat_face)
cat = Image.open(image_path)
glasses = Image.open('glasses.png')
for (x,y,w,h) in cat_face:
    glasses = glasses.resize((w*5, h*3))
    cat.paste(glasses, (int(x-110), int(y-80)),glasses)
    cat.save("cat_with_glasses.png")
    cat_with_glasses = cv2.imread("cat_with_glasses.png")
    cv2.imshow("Cat_with_glasses", cat_with_glasses)

    # cv2.imshow("Cat", image)
    cv2.waitKey()