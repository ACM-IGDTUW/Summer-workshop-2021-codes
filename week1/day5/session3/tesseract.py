from PIL import Image
import pytesseract


img = Image.open('image.png')

gray = img.convert('L')

bw = gray.point(lambda x: 0 if x < 100 else 255)
# bw.save('captcha_gray.png')

print(pytesseract.image_to_string(bw))

print(pytesseract.image_to_boxes(bw).split('\n'))

letters = pytesseract.image_to_boxes(bw)
letters = letters.split('\n')
letters = [letter.split() for letter in letters]

import cv2
img = cv2.imread('image.png')
h, w, _ = img.shape

for i, letter in enumerate(letters):
    cv2.rectangle(img, (int(letter[1]), h - int(letter[2])), (int(letter[3]), h - int(letter[4])), (0,0,255), 1)

cv2.imshow('img', img)
cv2.waitKey(0)

# https://gist.github.com/skt7/f98042c6c9c8bd81095fedadd322094e
# https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_processing_captcha.htm
# for path errors: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
