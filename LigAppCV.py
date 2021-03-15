import tkinter
import tkinter.font as font
import PIL.ImageTk as ImageTk
import PIL.Image as Image

from mySQLConnector import DataBaseConnection


window = tkinter.Tk(className='LigAppCV')
window.geometry("800x500")
window.configure(bg='black')

fontFooter = font.Font(weight="bold")
fontLbl = font.Font(weight="bold", size="20")
fontBtn = font.Font(weight="bold", size="10")

lblAppVersion = tkinter.Label(window, text="LigApp - V 1.3", bg="#11125c", fg="white")
lblAppVersion['font'] = fontFooter
lblAppVersion.pack(side=tkinter.BOTTOM, fill=tkinter.X)

lblInputCode = tkinter.Label(window, text="Código del partido", anchor='center', bg='black', fg="white")
lblInputCode['font'] = fontLbl
entGameCode = tkinter.Entry(window, font="Helvetica 24", justify='center', bg='#535c52', fg='white', width=10)

lblWait = tkinter.Label(window, text="Obteniendo datos del servidor. Por favor, espere...", anchor='center',
                        bg='green', fg="white")

img = ImageTk.PhotoImage(Image.open("resources/iconoApp.png"))
imgLogo = tkinter.Label(window, image=img, bg = 'black')


def finish_loop():
    window.destroy()



def get_game_code():
    lblWait.pack()
    game_id = entGameCode.get()
    try:
        DataBaseConnection.get_teams(DataBaseConnection(), game_id)
        lblWait['text'] = "Datos listos. Abriendo cámara..."
    except Exception as e:
        lblWait['text'] = "Ocurrió un error. Por favor, inténtalo de nuevo."


btnAccept = tkinter.Button(window, text="Confirmar", padx=50, command=get_game_code, bg="#11125c")

#btnAccept = tkinter.Button(window, text="Confirmar", padx=50, bg="#4af723")
btnAccept['font'] = fontBtn

lblInputCode.pack(pady=(150, 0))
entGameCode.pack()
btnAccept.pack(pady=(20, 0))
imgLogo.pack()

window.iconphoto(True, tkinter.PhotoImage(file='resources/icon.png'))
window.mainloop()
