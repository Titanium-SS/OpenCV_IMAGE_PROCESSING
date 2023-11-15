# This code was not part of the Video Series
"""
Haar Cascade namely 'haarcascade_car.xml that I trained was not so good at 
detecting cars, hence removed from the repo.
"""

import cv2

car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in cars:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, "CAR", (x-y, y-h), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
