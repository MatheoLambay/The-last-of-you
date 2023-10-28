#by Mathéo Lambay and Zakaria Ouafi
from tkinter import *
from game import *
from score import ApplicationScore
from info import ApplicationInfo

#TLOY FINAL

CONFIG = {
    
    "score_btn":"./img/menu_choixPM/bouton_score.png",
    "start_btn":"./img/menu_choixPM/bouton_start.png",
    "titre":"./img/menu_choixPM/titre_menu2.png",
    "carte1":"./img/menu_choixPM/carte1select.png",
    "carte2":"./img/menu_choixPM/carte2select.png",
    "elliot":"./img/menu_choixPM/elliotprime.png",
    "joan":"./img/menu_choixPM/joanprime.png",
    "menu1":"./img/menu_choixPM/fond_Menu1.png",
    "menu2":"./img/menu_choixPM/fond_Menu2.png",
    "menu3":"./img/menu_choixPM/fond_Menu3.png",
    "menu4":"./img/menu_choixPM/fond_Menu4.png"
}

PLAYER = {
    "joueur":"",
    "carte":"",
    "mode":""
}

class application(Tk):

    def __init__(self):
        Tk.__init__(self)

###############################################################################

        def ouvrirScore():
            self.destroy()
            ApplicationScore(new=False)
            
        def ouvrirInfo():
            self.destroy()
            ApplicationInfo()

        def ouvrirFperso():
            self.fen1.pack_forget()
            self.fen2.pack()

        def retour1():
            self.fen2.pack_forget()
            self.fen1.pack()

        def ouvrirFcarte(joueur):
            PLAYER["joueur"] = joueur
            self.fen2.pack_forget()
            self.fen3.pack()

        def retour2():
            self.fen3.pack_forget()
            self.fen2.pack()

        def ouvrirFmode(carte):
            PLAYER["carte"] = carte
            self.fen3.pack_forget()
            self.fen4.pack()

        def retour3():
            self.fen4.pack_forget()
            self.fen3.pack()

        def startGame(mode):
            PLAYER["mode"] = mode
            self.destroy()
            lancement(PLAYER["joueur"],PLAYER["carte"],PLAYER["mode"])
        
        
            
      




        ############## FENETRE DU MENU PRINCIPALE ###############


        self.fen1 = Frame(self, width = 1080, height = 720)
        self.resizable(width = False, height = False)
        self.fen1.pack()

        self.title("The Last Of You")

        self.iconbitmap("./img/logo.ico")
        
        self.geometry("1080x720+200+30")

        self.Can1 = Canvas(self.fen1, width = 1080, height = 720, bg = 'Black')
        self.Can1.pack()


        # FOND MENU #

        self.fondmenu = PhotoImage(file=CONFIG["menu1"])
        self.Can1.create_image(540, 360, image = self.fondmenu)


        # TITRE MENU #

        self.titreimage = PhotoImage(file=CONFIG["titre"])
        self.Can1.create_image(250, 360, image = self.titreimage)


        # BOUTON START/ SCORE/ QUITTER

        self.btnstr = Button(self, text = "Start", width = -7, height = -5, font = ('Karmatic Arcade', 25), bg = 'Black', fg = '#750101', command = ouvrirFperso)
        self.btnstr.place(x = 700, y = 250)

        self.btnsco = Button(self, text = "Score", width = -7, height = -5, font = ('Karmatic Arcade', 25), bg = 'Black', fg = '#750101', command= ouvrirScore)
        self.btnsco.place(x = 700, y = 350)

        self.btnqui = Button(self, text = "Quitter", width = -7, height = -5, font = ('Karmatic Arcade', 25), bg = 'Black', fg = 'White', command = self.destroy)
        self.btnqui.place(x = 830, y = 656)
        
        self.btninf = Button(self, text = "Info", width = -7, height = -5, font = ('Karmatic Arcade', 25), bg = 'Black', fg = 'White', command = ouvrirInfo)
        self.btninf.place(x = 16, y = 656)


        ############## FENETRE DU MENU PERSONNAGE ###############


        self.fen2 = Frame(self, width = 1080, height = 720)


        self.Can2 = Canvas(self.fen2, width = 1080, height = 720)
        self.Can2.pack(expand = YES)


        # FOND DU MENU 2 #

        self.fondmenu2 = PhotoImage(file=CONFIG["menu2"])
        self.Can2.create_image(540, 360, image = self.fondmenu2)


        # TEXTE : SELECTION PERSO #

        self.textperso = Label(self.Can2, text = "Selection  personnages", font = ('Karmatic Arcade', 30), bg = 'Black', fg = 'White')
        self.textperso.place(x = 215, y = 100)


        # BOUTON RETOUR #

        self.btnrtr = Button(self.fen2, text = "Retour", width = -7, height = -5, font = ('Karmatic Arcade', 25), bg = 'Black', fg = 'White', command = retour1)
        self.btnrtr.place(x = 830, y = 650)


        # BOUTON PERSO JOAN #

        self.joan = PhotoImage(file=CONFIG["joan"])
        self.btnjoa = self.Can2.create_image(280, 400, image = self.joan)
        self.Can2.tag_bind(self.btnjoa, "<Button-1>", lambda event : ouvrirFcarte('joan'))


        # BOUTON PERSO ELLIOT #

        self.elliot = PhotoImage(file=CONFIG["elliot"])
        self.btnelio = self.Can2.create_image(820, 400, image = self.elliot)
        self.Can2.tag_bind(self.btnelio, "<Button-1>", lambda event : ouvrirFcarte('elliot'))


        ############## FENETRE DU MENU CARTE ###############


        self.fen3 = Frame(self, width = 1080, height = 720)


        self.Can3 = Canvas(self.fen3, width = 1080, height = 720)
        self.Can3.pack(expand = YES)


        # FOND MENU 3 #

        self.fondmenu3 = PhotoImage(file=CONFIG["menu3"])
        self.Can3.create_image(540, 360, image = self.fondmenu3)


        # BOUTON RETOUR #

        self.btnrtr = Button(self.fen3, text = "Retour", width = -7, height = -5, font = ('Karmatic Arcade', 25), bg = 'Black', fg = 'White', command = retour2)
        self.btnrtr.place(x = 830, y = 650)


        # BOUTON DE SELECTION DE LA CARTE 1 #

        self.carte1 = PhotoImage(file=CONFIG["carte1"])
        self.btnmap1 = self.Can3.create_image(240, 200, image = self.carte1)
        self.Can3.tag_bind(self.btnmap1, "<Button-1>", lambda event : ouvrirFmode('city'))


        # BOUTON DE SELECTION DE LA CARTE 2 #

        self.carte2 = PhotoImage(file=CONFIG["carte2"])
        self.btnmap2 = self.Can3.create_image(540, 480, image = self.carte2)
        self.Can3.tag_bind(self.btnmap2, "<Button-1>",lambda event : ouvrirFmode('labo'))


        ############## FENETRE DU MENU MODE DE JEU###############


        self.fen4 = Frame(self, width = 1080, height = 720)


        self.Can4 = Canvas(self.fen4, width = 1080, height = 720)
        self.Can4.pack(expand = YES)


        # FOND MENU 4 #

        self.fondmenu4 = PhotoImage(file=CONFIG["menu4"])
        self.Can4.create_image(540, 360, image = self.fondmenu4)


        # TEXTE : MODE DE JEU #

        self.textperso = Label(self.Can4, text = "Mode  de  Jeu", font = ('Karmatic Arcade', 30), bg = 'Black', fg = 'White')
        self.textperso.place(x = 360, y = 100)


        # BOUTON RETOUR #

        self.btnrtr = Button(self.fen4, text = "Retour", width = -7, height = -5, font = ('Karmatic Arcade', 25), bg = 'Black', fg = 'White', command = retour3)
        self.btnrtr.place(x = 830, y = 650)


        # BOUTON MODE LIBRE

        self.btnlbr = Button(self.fen4, text = "Mode Libre", width = 12, height = -12, font = ('Karmatic Arcade', 25), bg = 'Black', fg = '#108AE3', command=lambda : startGame('libre'))
        self.btnlbr.place(x = 150, y = 320)
        
        self.textlibre = Label(self.Can4, text = "Votre  but  est  de  faire \n le  meilleur  score  en  tuant \n un  max  de  zombies", font = ('Karmatic Arcade', 12), bg = 'Black', fg = 'White')
        self.textlibre.place(x = 154, y = 400)

        # BOUTON MODE SURVIE

        self.btnsrv = Button(self.fen4, text = "Mode Survie", width = 12, height = -12, font = ('Karmatic Arcade', 25), bg = 'Black', fg = '#20B01C', command=lambda : startGame('survie'))
        self.btnsrv.place(x = 580, y = 320)
        
        self.textsurvie = Label(self.Can4, text = "Votre  but  est  de  survivre \n dans  un  temps  imparti.\n Quand  le  temps  atteint  0 \n vous  avez  gagnee", font = ('Karmatic Arcade', 12), bg = 'Black', fg = 'White')
        self.textsurvie.place(x = 590, y = 400)





###############################################################################



# AFFICHAGE DU PROGRAMME
if __name__ == '__main__':
    app = application()
    app.mainloop()