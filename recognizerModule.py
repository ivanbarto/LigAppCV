import cv2
import os
import numpy as np


def start_recogntion_camera():

    absolutePath = "D:/PyCharmProjects/LigAppRecognizer"
    facesPath = "/faces/data"
    dataPath = absolutePath + facesPath

    # generamos una lista con cada carpeta
    peopleList = os.listdir(dataPath)

    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    # leemos el modelo
    face_recognizer.read("modeloEigenFace.xml")
    faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            face = auxFrame[y:y + h, x:x + w]
            face = cv2.resize(face, (150, 150), interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(face)

            cv2.putText(frame, '{}'.format(result), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

            if result[1] < 5000:
                cv2.putText(frame, '{}'.format(peopleList[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else:
                cv2.putText(frame, "desconocido", (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("Frame", frame)
        # k = cv2.waitKey(1)
        # if k == 27:
        #    break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

