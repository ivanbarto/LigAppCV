import os

import cv2
import pymysql
import base64
import recognitionTrainer

DATABASE_NAME = "bdligapp"
DATABASE_PASSWORD = "654654654Da"
DATABASE_USER = "fedecurto98"
DATABASE_HOST = "db4free.net"
DATABASE_PORT = "3306"
DATABASE_URL = DATABASE_HOST
GET_ALL_PLAYERS_QUERY = "SELECT * FROM player"
PATH_FOLDER_PLAYERS = 'faces/data/'

faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")


# LE PASAS UNA IMAGEN Y LA GUARDA
def write_file(filename, data):
    person_directory = PATH_FOLDER_PLAYERS + filename
    person_photo_path = person_directory + "/" + filename + ".png"
    if not os.path.exists(person_directory):
        os.makedirs(person_directory)
    # Convert binary data to proper format and write it on Hard Disk

    with open(person_photo_path, 'wb') as file:
        file.write(base64.decodebytes(data))
    ''' hasta aca es guardar el archivo '''
    img = cv2.imread(person_photo_path)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 5)
    face_identified = False
    for (x, y, w, h) in faces:
        face_identified = True
        faceCropped = img[y:y + h, x:x + w]
        # formateo la img porque todas deben ser iguales para entrenar el modelo
        faceCropped = cv2.resize(faceCropped, (150, 150), interpolation=cv2.INTER_CUBIC)
        # guardo la cara redimensionada en su dir
        cv2.imwrite(person_photo_path, faceCropped)

    if not face_identified:
        os.remove(person_photo_path)
        os.removedirs(person_directory)

class DataBaseConnection:
    def __init__(self):
        self.connection = pymysql.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            db=DATABASE_NAME
        )

        self.cursor = self.connection.cursor()

        print("connection to database succesfully")

    # obtiene la foto de jugadores de un team en particualr

    def get_instance(self):
        return self

    def select_players(self, teamId):
        print('getting players from database...')
        sql = 'SELECT * FROM player WHERE idTeam = %s'
        id = teamId

        try:
            self.cursor.execute(sql, id)
            teamPlayers = self.cursor.fetchall()

            for player in teamPlayers:
                # el index 10 tiene la foto
                if not player[10] == None:
                    print('     formatting player\'s face')
                    playerCompleteName = player[1] + " " + player[2]
                    image = player[10]
                    write_file(playerCompleteName, image)
            print('Process finished.')

        except Exception as e:
            print('ERROR: getting players from database.')
            raise

        recognitionTrainer.train_model()

    # obtiene la foto de todos los jugadores QUE TENGAN FOTO
    # def select_players(self):
    #     sql = GET_ALL_PLAYERS_QUERY
    #     try:
    #         self.cursor.execute(sql)
    #         user = self.cursor.fetchall()
    #
    #         for player in user:
    #             print("Id:", player[0])
    #             print("Name:", player[1])
    #             print("lastname: ",player[3])
    #             # el index 10 tiene la foto
    #
    #             if not player[10] == None:
    #                 playerName = player[1]
    #                 playerLastname = player[2]
    #                 playerCompleteName = playerName + " " + playerLastname
    #                 image = player[10]
    #                 write_file(playerCompleteName, image)
    #
    #     except Exception as e:
    #         raise


database = DataBaseConnection()
# database.select_players(1)
