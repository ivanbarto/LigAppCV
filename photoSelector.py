import cv2
import os


# creo el directorio que tiene las fotos de Ivan
# por cada jugador, podria crear un directorio nuevo
absolutePath = "D:/PyCharmProjects/LigAppRecognizer"
dataPath = "/faces/data"

personName = "alucard"
personPath = absolutePath + dataPath + "/" + personName
if not os.path.exists(personPath):
    os.makedirs(personPath)

personName = "ivan"
personPath = absolutePath + dataPath + "/" + personName
if not os.path.exists(personPath):
    os.makedirs(personPath)

personName = "paul"
personPath = absolutePath + dataPath + "/" + personName
if not os.path.exists(personPath):
    os.makedirs(personPath)

# preparo el clasificador
faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")

# cargo la foto - deberia hacerlo por cada una de las fotos a este proceso
img = cv2.imread(personPath + "/paul.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray, 1.2, 5)
for (x, y, w, h) in faces:
    faceCropped = img[y:y + h, x:x + w]
    # formateo la img porque todas deben ser iguales para entrenar el modelo
    faceCropped = cv2.resize(faceCropped, (150, 150), interpolation=cv2.INTER_CUBIC)
    # guardo la cara redimensionada en su dir
    cv2.imwrite(personPath + "/paul.jpg", faceCropped)
# cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)  esto dibuja el rectangulo



