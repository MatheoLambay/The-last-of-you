from tkinter import *




CONFIG = {"zombvert_city":"./img/city/greendead_haut.png",
          "zombvert_labo":"./img/labo/greendead_haut.png",
          "zombbleu_city":"./img/city/bluedead_haut.png",
          "zombbleu_labo":"./img/labo/bluedead_haut.png",
          "zombrouge_city":"./img/city/reddead_haut.png",
          "zombrouge_labo":"./img/labo/reddead_haut.png",
          "joan_info":"./img/players/joan/perso_info.png",
          "elliot_info":"./img/players/elliot/perso_info.png",
          "dofla_info":"./img/players/easter_egg.png"
          
    }

class ApplicationInfo(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        

        ### CREATION DE LA FENETRE ET SON CANVAS ###
        
        self.title("The Last Of You")
        self.iconbitmap("./img/logo.ico")
        self.geometry("1080x720+200+30")
        self.resizable(width = False, height = False)

          
        self.feninf = Frame(self, width = 1080, height = 720)
        self.feninf.pack()
        
        self.caninf = Canvas(self.feninf, width = 1080, height = 720, bg = 'Black')
        self.caninf.pack(expand = YES)
        
        ### CREATION DES DIFFERENTS TEXTE (l'histoire, nom des zombies, description des zombies) ###
    
        self.text = Label(self.caninf, text = "Information", font = ('karmatic Arcade', 25), bg = 'Black', fg = 'White')
        self.text.place(x = 420, y = 20)
        
        self.texthist = Label(self.caninf, text = "Nous sommes en 2033, le monde d'aujourd'hui est totalement en ruine, plus de 70 % de la population s'est éteinte seul quelques personnes survive. \n Mais comment est-on en arrivé là...? Un seul mot : le Cordybiceps, une infection qui a touché toute la planète Terre \n transformant ainsi les humains en horrible infectée, zombie...", font = ('Arial', 12), bg = 'Black', fg = 'White')
        self.texthist.place(x = 32, y = 75)
        
        self.textzombvNom = Label(self.caninf, text = "Les Claquées", font = ('Comic Sans MS', 18), bg = 'Black', fg = 'Green')
        self.textzombvNom.place(x = 160, y = 200)
        
        self.textzombv = Label(self.caninf, text = "les zombies les plus fréquents, mais \n les moins dangereux. Suffit d'une balle \n pour les tuer. (1 Point de Vie)", font = ('Arial', 12), bg = 'Black', fg = 'White')
        self.textzombv.place(x = 150, y = 234)
        
        self.textzombbNom = Label(self.caninf, text = "Les Marcheurs", font = ('Comic Sans MS', 18), bg = 'Black', fg = 'Blue')
        self.textzombbNom.place(x = 160, y = 400)
        
        self.textzombb = Label(self.caninf, text = "Un peu plus dangereux, les Marcheurs \n ce font un peu plus rare que les Claquées \n mais sont plus résistants. (2 Points de Vie)", font = ('Arial', 12), bg = 'Black', fg = 'White')
        self.textzombb.place(x = 150, y = 432)
        
        self.textzombrNom = Label(self.caninf, text = "Les Shlageurs", font = ('Comic Sans MS', 18), bg = 'Black', fg = 'Red')
        self.textzombrNom.place(x = 160, y = 600)
        
        self.textzombr = Label(self.caninf, text = " Seuls les braves arriveront jusqu'à eux... \n Les zombies les plus dangereux que \n la terre est connu. (3 points de Vie)", font = ('Arial', 12), bg = 'Black', fg = 'White')
        self.textzombr.place(x = 150, y = 636)
         
        self.btnrtr = Button(self.feninf, text = "Retour", width = -7, height = -5, font = ('Karmatic Arcade', 25), bg = 'Black', fg = 'White', command = self.mainMenu2)
        self.btnrtr.place(x = 830, y = 650)

        self.textperso = Label(self.caninf, text = "Ancienne mère, Joan a vu naître le début de l'apocalypse. \n Aujourd'hui, Joan survie comme elle peut et fait la rencontre \n d'un jeune garçon nommée Elliot. \n Tout deux sont à la recherche de l'unique coton tige. \n (nom de l'antidote qui peut sauver l'humanité)", font = ('Arial', 12), bg = 'Black', fg = 'White')
        self.textperso.place(x = 630, y = 450)
    
        

        self.zomb = PhotoImage(file=CONFIG["zombvert_city"])
        self.zomb2 = PhotoImage(file=CONFIG["zombvert_labo"])
        self.zomb3 = PhotoImage(file=CONFIG["zombbleu_city"])
        self.zomb4 = PhotoImage(file=CONFIG["zombbleu_labo"])
        self.zomb5 = PhotoImage(file=CONFIG["zombrouge_city"])
        self.zomb6 = PhotoImage(file=CONFIG["zombrouge_labo"])
        self.joa = PhotoImage(file=CONFIG["joan_info"])
        self.eli = PhotoImage(file=CONFIG["elliot_info"])
        self.dof = PhotoImage(file=CONFIG["dofla_info"])
        
        
        self.Zombvert()
        self.Zombbleu()
        self.Zombrouge()
        self.Joan()
        
       ### CREATION DES DIFFERENT BOUTON AVEC LEURS IMAGES ### 
           
    def Zombvert(self):
        self.btnzomb = self.caninf.create_image(100, 250, image = self.zomb)
        self.caninf.tag_bind(self.btnzomb, "<Button-1>", self.ZombinfoV)
                  
    def Zombvert2(self):                      
        self.btnzomb2 = self.caninf.create_image(100, 250, image = self.zomb2)
        self.caninf.tag_bind(self.btnzomb2, "<Button-1>", self.ZombinfoV2)
                                   
    def Zombbleu(self):
        self.btnzomb3 = self.caninf.create_image(100, 450, image = self.zomb3)
        self.caninf.tag_bind(self.btnzomb3, "<Button-1>", self.ZombinfoB)
                    
    def Zombbleu2(self):
        self.btnzomb4 = self.caninf.create_image(100, 450, image = self.zomb4)
        self.caninf.tag_bind(self.btnzomb4, "<Button-1>", self.ZombinfoB2)
                    
    def Zombrouge(self):       
        self.btnzomb5 = self.caninf.create_image(100, 650, image = self.zomb5)
        self.caninf.tag_bind(self.btnzomb5, "<Button-1>", self.ZombinfoR)
                    
    def Zombrouge2(self):
        self.btnzomb6 = self.caninf.create_image(100, 650, image = self.zomb6)
        self.caninf.tag_bind(self.btnzomb6, "<Button-1>", self.ZombinfoR2)
        
        
    def Joan(self):
        self.btnjoa = self.caninf.create_image(850, 360, image = self.joa)
        self.caninf.tag_bind(self.btnjoa, "<Button-1>", self.JoanInfo)
        self.textperso.configure(text = "Ancienne mère, Joan a vu naître le début de l'apocalypse. \n Aujourd'hui, Joan survie comme elle peut et fait la rencontre \n d'un jeune garçon nommée Elliot. \n Tout deux sont à la recherche de l'unique coton tige. \n (nom de l'antidote qui peut sauver l'humanité)") # configure le texte du perso par rapport a sa fonction
        
    def Elliot(self):
        self.btneli = self.caninf.create_image(850, 360, image = self.eli)
        self.caninf.tag_bind(self.btneli, "<Button-1>", self.ElliotInfo)
        self.textperso.configure(text = "Elliot est un jeune orphelin de 12 ans qui n'a pas peur aux \n yeux. Il fait la rencontre de Joan lors d'une mission de \n sauvetage menée par Joan et un ancien \n policier nommé Hope, où celui-ci meurt lors de la \n mission et donne sa casquette fétiche a Elliot \n juste avant d'émettre son dernier souffle.") # configure le texte du perso par rapport a sa fonction
        
        
    def Dofla(self):
        self.btndfa = self.caninf.create_image(850, 360, image = self.dof)
        self.caninf.tag_bind(self.btndfa, "<Button-1>", self.DoflaInfo)
        self.textperso.configure(text = "(Esteer egg) Doflamingo (tiré du manga One Piece) a servi de \n modèle de base du personnage avant d'être remplacer par \n Joan et Elliot. \n *le skin Doflamingo non-inclus dans le jeu*") # configure le texte du perso par rapport a sa fonction
        
                
    def mainMenu2(self): # fonction permettant de detruire la fenetre et retourner sur le menu principal
        self.destroy()
        from main import application
        app = application()
        app.mainloop()
        
    ### FONCTION PERMETTANT DE SWITCH D'IMAGE EN CLIQUANT DESSUS ###    
        
    def ZombinfoV(self, event):
        self.caninf.delete(self.btnzomb) # supprime la 1er image
        self.Zombvert2() # appele la fonction qui créer la 2eme image
        
        
    def ZombinfoV2(self, event):
        self.caninf.delete(self.btnzomb2) # supprime la 2eme image
        self.Zombvert() # appele la fonction qui créer la 1er image
        
            
    def ZombinfoB(self, event):
        self.caninf.delete(self.btnzomb3)
        self.Zombbleu2()
            
        
    def ZombinfoB2(self, event):
        self.caninf.delete(self.btnzomb4)
        self.Zombbleu()
            
        
    def ZombinfoR(self, event):
        self.caninf.delete(self.btnzomb5)
        self.Zombrouge2()
                       
        
    def ZombinfoR2(self, event):
        self.caninf.delete(self.btnzomb6)
        self.Zombrouge()
        
        
    def JoanInfo(self, event):
        self.caninf.delete(self.btnjoa)
        self.Elliot()
  

    def ElliotInfo(self, event):
        self.caninf.delete(self.btneli)
        self.Dofla()
        
        
    def DoflaInfo(self, event):
        self.caninf.delete(self.btndfa)
        self.Joan()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
