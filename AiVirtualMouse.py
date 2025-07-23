import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy
import pyautogui

##########################
wCam, hCam = 640, 480
frameR = 100     # Frame Reduction
smoothening = 7 # Smoothing Factor
##########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()

while True:
    # Step1: Capture frame
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # Step2: Get tip positions of index & middle finger
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]   # Index
        x2, y2 = lmList[12][1:]  # Middle
        x_thumb, y_thumb = lmList[4][1:]  # Thumb

        # Step3: Detect which fingers are up
        fingers = detector.fingersUp()

        # Draw frame boundary
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)

        # Step4: Moving Mode – only index up
        if fingers[1] == 1 and fingers[2] == 0:
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # Step5: Clicking Mode – index and middle up
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()

        # Step6: Scroll Mode – thumb + index
        if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0:
            length, img, lineInfo = detector.findDistance(4, 8, img)
            if length > 80:
                pyautogui.scroll(-100)  # scroll down
            elif length < 40:
                pyautogui.scroll(100)   # scroll up

    # Step7: FPS counter
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (28, 58), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 8, 8), 3)

    # Step8: Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
