import cv2
import os
import numpy as np
import recognizerModule

def train_model():
    # establecemos el directorio donde estan las carpetas con las caras de los jugadores
    absolutePath = "D:/PyCharmProjects/LigAppRecognizer"
    facesPath = "/faces/data"
    dataPath = absolutePath + facesPath

    # generamos una lista con cada carpeta
    peopleList = os.listdir(dataPath)

    labels = []
    facesData = []
    label = 0

    # leemos las imagenes de cada jugador
    print("Images reading...")
    for nameDirectory in peopleList:
        personPath = dataPath + "/" + nameDirectory
        print("     " + personPath)
        for photo in os.listdir(personPath):
            print("          " + photo)
            # ahora almacenamos foto + etiqueta
            labels.append(label)
            img = cv2.imread(personPath + "/" + photo)
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            facesData.append(imgGray)  # con el 0 trasnformarmos a greyscale
        # img = cv2.imread(personPath + photo, 0)
        label = label + 1

    print("\nPeople identified: ")
    print(labels)

    # ahora se entrena el modelo
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    print("\n\nTraining model...")
    face_recognizer.train(facesData, np.array(labels))
    print("Saving model...")
    face_recognizer.write("modeloEigenFace.xml")
    print("Model ready.")

    recognizerModule.start_recogntion_camera()
