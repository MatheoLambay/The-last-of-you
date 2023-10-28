import tkinter as tk
from tkinter import *
import random
from score import ApplicationScore

CONFIG = {
    #paramètre de jeu
    "width": 1080,
    "height": 720,
    "zombieVitesse": 60,
    "zombieSpawn": 500,
    "temps": 60,
    "cheminAcces":"",
    "cheminAccesjoueur":"", 
    "fontColor":"",
    "mode":"",

    #texture
    "map":"map.png",
    "gameover":"gameover.png",
    "victoire":"victoire.png",
    "wall_droite":"wall.png",
    "wall_gauche":"wall2.png",

    "greendead_haut":"greendead_haut.png",
    "greendead_bas":"greendead_bas.png",
    "greendead_gauche":"greendead_gauche.png",
    "greendead_droite":"greendead_droite.png", 

    "bluedead_haut":"bluedead_haut.png",
    "bluedead_bas":"bluedead_bas.png",
    "bluedead_gauche":"bluedead_gauche.png",
    "bluedead_droite":"bluedead_droite.png",  
    "bluedead_haut_blessure":"bluedeadblesse_haut.png",
    "bluedead_bas_blessure":"bluedeadblesse_bas.png",
    "bluedead_gauche_blessure":"bluedeadblesse_gauche.png",
    "bluedead_droite_blessure":"bluedeadblesse_droite.png",

    "reddead_haut":"reddead_haut.png",
    "reddead_bas":"reddead_bas.png",
    "reddead_gauche":"reddead_gauche.png",
    "reddead_droite":"reddead_droite.png",   
    "reddead_haut_blessure1":"reddeadblesse1_haut.png",
    "reddead_bas_blessure1":"reddeadblesse1_bas.png",
    "reddead_gauche_blessure1":"reddeadblesse1_gauche.png",
    "reddead_droite_blessure1":"reddeadblesse1_droite.png",
    "reddead_haut_blessure2":"reddeadblesse2_haut.png",
    "reddead_bas_blessure2":"reddeadblesse2_bas.png",
    "reddead_gauche_blessure2":"reddeadblesse2_gauche.png",
    "reddead_droite_blessure2":"reddeadblesse2_droite.png",

    "player_haut":"player_haut.png",
    "player_bas":"player_bas.png",
    "player_gauche":"player_gauche.png",
    "player_droite":"player_droite.png",
    "player_haut_droite":"player_haut_droite.png",
    "player_haut_gauche":"player_haut_gauche.png",
    "player_bas_droite":"player_bas_droite.png",
    "player_bas_gauche":"player_bas_gauche.png",
    "player_mort":"player_mort.png",
    "player_victoire":"player_victoire.png" 
}
SCORE = 0

class ApplicationJeux(tk.Tk):
    
    def __init__(self,vie_joueur=3,atk_joueur=1):
        tk.Tk.__init__(self)

        self.iconbitmap("./img/logo.ico") 
        self.title("The Last Of You")
        
    
        # CREATION VIE ET SCORE JOUEUR
        self.score_joueur = 0
        self.life_joueur = vie_joueur
        self.atk_joueur = atk_joueur
        self.temps = CONFIG["temps"]
        
        # CREATION D'UN DICT POUR LISTER LES ZOMBIES PRESENT SUR LA MAP
        self.zombies = {}

        ############## INTERFACE ##############

        # FENETRE PRINCIPALE
        self.resizable(width = False, height = False)
        self.geometry("1495x720+10+30")
        self.jeux = tk.Frame(self, width = 1080, height = 720)
        
        self.jeux.pack()

        # INTERFACE DU MILIEU (canvas écran jeux) #

        self.ecran = tk.Frame(self.jeux)
        
        self.canvas = tk.Canvas(self.ecran, width=CONFIG["width"], height=CONFIG["height"], bg='black',cursor="tcross")
        
        self.ecran.grid(row=1,column=2) # placement de la frame
        
        # CREATION DU JOUEUR

        self.joueur = Joueur(self.canvas,self.life_joueur,self.atk_joueur) # vie, attaque

        # INTERFACE DE GAUCHE (canvas gauche) #
        
        self.ecran_gauche = tk.Frame(self.jeux)
        
        self.canvas_gauche = tk.Canvas(self.ecran_gauche,width=200 , height=CONFIG["height"],bg=CONFIG["fontColor"])
        self.wall2 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["wall_gauche"])
        self.canvas_gauche.create_image(105,360,image = self.wall2)
        
        # Creer l'affichage du Chronometre et l'applique dans le mode de jeu "Survie"
        
        if CONFIG["mode"] ==  'survie':
            self.timer = self.canvas_gauche.create_text(100,110, text="00:00:00", font=("Arial", 24),fill=CONFIG["fontColor"])
            self.survie_mode = True
            self.demarrerTimer()
        else:
            self.survie_mode = False
            
        self.canvas_gauche.pack()
        
        self.ecran_gauche.grid(row=1,column=1)  # placement de la frame 

        #INTERFACE DE DROITE (canvas droite, score et vie) #
        
        self.ecran_droite = tk.Frame(self.jeux)
        
        self.canvas_droite = tk.Canvas(self.ecran_droite,width=200 , height=CONFIG["height"],bg=CONFIG["fontColor"])
        self.wall  = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["wall_droite"])
        self.canvas_droite.create_image(105,360,image = self.wall)
        
        self.score_text = self.canvas_droite.create_text(100,110,text=self.score_joueur,font=("Comic Sans MS",14),fill=CONFIG["fontColor"])
        self.life_text = self.canvas_droite.create_text(100,320,text=self.life_joueur,font=("Comic Sans MS",14),fill=CONFIG["fontColor"])
        if not(self.survie_mode):
            self.ultimate_indicator = self.canvas_droite.create_text(100,490,text="Ultimate",font=("Comic Sans MS",25),fill=CONFIG["fontColor"])
            self.ultimate_text = self.canvas_droite.create_text(100,530,text=self.joueur.ultime_state,font=("Comic Sans MS",25),fill=CONFIG["fontColor"])

        self.canvas_droite.pack()
        self.ecran_droite.grid(row=1,column=3) # placement de la frame 

        self.background = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["map"])
        self.canvas.create_image(CONFIG["width"]/2,CONFIG["height"]/2,image=self.background)
        
        # TEXTURES DES ZOMBIES
        self.green_gauche = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["greendead_gauche"])
        self.green_droite = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["greendead_droite"])
        self.green_haut = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["greendead_haut"])
        self.green_bas = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["greendead_bas"])
        
        self.red_gauche = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["reddead_gauche"])
        self.red_droite = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["reddead_droite"])
        self.red_haut = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["reddead_haut"])
        self.red_bas = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["reddead_bas"])
        self.red_haut_damaged1 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["reddead_haut_blessure1"])
        self.red_bas_damaged1 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["reddead_bas_blessure1"])
        self.red_gauche_damaged1 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["reddead_gauche_blessure1"])
        self.red_droite_damaged1 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["reddead_droite_blessure1"]) 
        self.red_haut_damaged2 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["reddead_haut_blessure2"])
        self.red_bas_damaged2 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["reddead_bas_blessure2"])
        self.red_gauche_damaged2 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["reddead_gauche_blessure2"])
        self.red_droite_damaged2 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["reddead_droite_blessure2"])                                                               

        self.blue_gauche = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["bluedead_gauche"])
        self.blue_droite = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["bluedead_droite"])
        self.blue_haut = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["bluedead_haut"])
        self.blue_bas = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["bluedead_bas"])
        self.blue_haut_damaged1 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["bluedead_haut_blessure"])
        self.blue_bas_damaged1 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["bluedead_bas_blessure"])
        self.blue_gauche_damaged1 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["bluedead_gauche_blessure"])
        self.blue_droite_damaged1 = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["bluedead_droite_blessure"])

        # AFFICHAGE DU PERSONNAGE SUR LA MAP#
        self.joueur_gauche = PhotoImage(file=CONFIG["cheminAccesjoueur"]+CONFIG["player_gauche"])
        self.joueur_droite = PhotoImage(file=CONFIG["cheminAccesjoueur"]+CONFIG["player_droite"])
        self.joueur_haut = PhotoImage(file=CONFIG["cheminAccesjoueur"]+CONFIG["player_haut"])
        self.joueur_bas = PhotoImage(file=CONFIG["cheminAccesjoueur"]+CONFIG["player_bas"])
        self.joueur_haut_droite = PhotoImage(file=CONFIG["cheminAccesjoueur"]+CONFIG["player_haut_droite"])
        self.joueur_haut_gauche = PhotoImage(file=CONFIG["cheminAccesjoueur"]+CONFIG["player_haut_gauche"])
        self.joueur_bas_droite = PhotoImage(file=CONFIG["cheminAccesjoueur"]+CONFIG["player_bas_droite"])
        self.joueur_bas_gauche = PhotoImage(file=CONFIG["cheminAccesjoueur"]+CONFIG["player_bas_gauche"])
        
        self.victoire = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["victoire"])
        self.victoirepose = PhotoImage(file=CONFIG["cheminAccesjoueur"]+CONFIG["player_victoire"])
        
        self.joueur_canvas = self.canvas.create_image(CONFIG["width"]/2,CONFIG["height"]/2,image =self.joueur_droite)

        self.canvas.grid(row=1, column=1) # placement du canvas
        
        
        
        self.canvas.bind("<Button-1>", self.on_click) # appelle la fonction on_clique grace au clique gauche dans le canvas (ecran de jeux)
        self.canvas.bind("<Motion>", self.orientationJoueur)
        
        if not(self.survie_mode):
            self.canvas.bind('<Button-3>',self.ultime)

        # LANCEMENT DU JEU
        self.spawn()
        self.animate()
        
        
    ############## APPARATION DES ZOMBIES ET GESTION DES TIRS,POINT,MORT,ETC ##############
        # Mode de jeu survie (application d'un chronometre etc...)#
        
    def demarrerTimer(self):
        if self.temps != 0 and self.life_joueur > 0: # condition : le temps est different de 0 ET que le joueur est en vie
            self.temps -= 1 # enleve 1sec au chronometre
            self.canvas_gauche.itemconfig(self.timer,text=self.formatter_temps(self.temps)) # importe et place l'affichage du chronometre dans le canvas de gauche
            self.canvas_gauche.after(1000, self.demarrerTimer)
        
        elif self.life_joueur > 0 : # Supprime tout les zombien quand seulement (=condtion) le joueur est en vie
            for i in self.zombies:
                self.canvas.delete(i)
            self.zombies = {}
            
            self.canvas.itemconfig(self.joueur_canvas,image = self.victoirepose) # modifie l'image du joueur en pose victoire    
            self.canvas.create_image(CONFIG["width"]/2,CONFIG["height"]/2,image=self.victoire) # ajout de l'image Win
            
            if CONFIG["mode"] == "libre":
                
                self.quit_button = tk.Button(self.canvas_gauche, text = "Quit", command =  lambda : verifNom(self.name_entry,self.canvas_gauche,self.label_error),width = 10,font = ('Arial', 20),fg='white',bg="#d92e2e")
                self.name_entry = tk.Entry(self.canvas_gauche)
                self.canvas_gauche.create_window(105, 150, window=self.quit_button)
                self.label_error = self.canvas_gauche.create_text(105,200,fill='red')
                self.canvas_gauche.create_window(105, 180, window=self.name_entry)
                
            else:
                
                self.quit_button = tk.Button(self.canvas_gauche, text = "Quit", command = quitter,width = 10,font = ('Arial', 20),fg='white',bg="#d92e2e")
                self.canvas_gauche.create_window(105, 150, window=self.quit_button)

    def formatter_temps(self, temps): # Convertie tout les uniter de temps (exemple : 60s = 1min)
        heures = temps // 3600
        minutes = (temps % 3600) // 60
        secondes = temps % 60
        return f"{heures:02d}:{minutes:02d}:{secondes:02d}"
    
    
    # DEFINITION DES VAGUES DE ZOMBIE ET LA VITESSE DE SPAWN EN FONCTION DES POINTS #
   
    def spawn(self):
        vitesse = self.vitesseSpawn()
        if self.life_joueur != 0 and self.temps !=0:

            if self.score_joueur > 8000:

                self.vagueZombie('rouge','bleu',chance=50)

            elif self.score_joueur > 5000:

                self.vagueZombie('rouge','bleu',chance=40)

            elif self.score_joueur > 4000:

                self.vagueZombie('rouge','bleu',chance=30)

            elif self.score_joueur > 3000:

                self.vagueZombie('rouge','bleu',chance=20)

            elif self.score_joueur > 1200 :

                self.vagueZombie('rouge','bleu',chance=10)
            
            elif  self.score_joueur >= 500:
                
                self.vagueZombie('bleu')

            elif self.score_joueur < 500:
                
                self.vagueZombie()
                
            #appelle de la fonction vitesse de spawn
            
            
            self.canvas.after(vitesse, self.spawn) #répète la fonction en boucle  toute les 200ms
        
    def vitesseSpawn(self): #modifie la vitesse de spawn en fonction du score

        vitesse = CONFIG["zombieSpawn"]

        if self.score_joueur > 3000:
            new_vitesse = vitesse - 250
        elif self.score_joueur > 2500:
            new_vitesse = vitesse - 200
        elif self.score_joueur > 2000:
            new_vitesse = vitesse - 150
        elif self.score_joueur > 1500:
            new_vitesse = vitesse - 100
        elif self.score_joueur > 1000:
            new_vitesse = vitesse - 50
        elif self.score_joueur > 500:
            new_vitesse = vitesse - 25
        else:
            new_vitesse = vitesse
        return new_vitesse
        
    def vagueZombie(self,color1='vert',color2='vert',color3='vert',chance=100):
        
        color_random = random.choice([color1,color2,color3]) # Choisit aléatoirement la couleurs du zombie
        
        if color_random == 'rouge': #réduit les chances de tomber sur un zombies rouge(zombie le plus puissant)
            nbr = random.randint(0,100)
            if  nbr >= chance:
                color_random = 'vert'
                
        type_zombie = self.colorZombie(color_random) #appelle la fonction colorZombie qui renvoit les textures en fonction de la  couleur du zombies généré 
        startPosition =  random.choice([(0,360),(540,0),(1080,360),(540,720)]) #position aléatoire de départ du zombie
        x,y = startPosition[0],startPosition[1]
        
        if startPosition == (0,360):#associe l'orientation de la texture du zombie en fonction du lieu de spawn sur l'écran
            orientation = type_zombie[0]
            
        elif startPosition == (540,0):
            orientation = type_zombie[2]
            
        elif startPosition == (1080,360):
            orientation = type_zombie[1]
            
        else: #(540,720)
            orientation = type_zombie[3]
        
        if color_random == 'vert':
            new_zombie = Zombie(self.canvas,self.canvas_gauche,self.joueur_canvas,startPosition,x,y,orientation,1,1,10,'vert') # vie,attaque,score
            
        elif color_random == 'rouge':
            new_zombie = Zombie(self.canvas,self.canvas_gauche,self.joueur_canvas,startPosition,x,y,orientation,3,1,30,'rouge') # vie,attaque,score
   
        elif color_random == 'bleu': 
            new_zombie = Zombie(self.canvas,self.canvas_gauche,self.joueur_canvas,startPosition,x,y,orientation,2,1,20,'bleu') # vie,attaque,score
        
        self.zombies[new_zombie.id] = new_zombie #ajout du zombie dans le dict zombies(initialisé au début du code)
    
    def colorZombie(self,color): # renvoit 4 images orienté dans des directions différentes en fonction de la couleur fourni
    
        if color == 'vert':
            zombie_gauche = self.green_gauche
            zombie_droite = self.green_droite
            zombie_haut = self.green_haut
            zombie_bas = self.green_bas
            
        elif color == 'rouge':
            zombie_gauche = self.red_gauche
            zombie_droite = self.red_droite
            zombie_haut = self.red_haut
            zombie_bas = self.red_bas
            
        elif color == 'bleu':
            zombie_gauche = self.blue_gauche
            zombie_droite = self.blue_droite
            zombie_haut = self.blue_haut
            zombie_bas = self.blue_bas
            
        return zombie_gauche,zombie_droite,zombie_haut,zombie_bas
         
    # DEPLACE LES ZOMBIES SUR LE CANVAS

    def animate(self):
    
        for zombie in self.zombies.values(): #parcours le dict zombies via une boucle (zombie contient l'id d'un objet, ici un zombie)
            coord_zombie = zombie.move() #pour chaque élément de la boucle appelle la fonction move et reçois en retour les coordonnées du zombies
        
            if coord_zombie[0] == 540 and coord_zombie[1] == 360: #détecte quand un zombie est au centre
                
                zombie.attack(self.joueur) #pour chaque élément qui respecte la condition lance la fonction attack
                if self.life_joueur != 0: #permet de modifier l'indicateur de vie sur le canva à droite
                    self.life_joueur -= 1
                    self.canvas_droite.itemconfig(self.life_text,text=self.life_joueur)
                                
        self.canvas.after(CONFIG["zombieVitesse"], self.animate)   #répète la fonction en boucle  toute les 60ms
    
       
        
    # ORIENTATION DU JOUEUR VERS LE CLIQUE ET CONFIGURATION DE LA ZONE DE TIRE #

    def on_click(self, event):
        
        if self.joueur.life > 0 and self.temps !=0: #permet au joueur de tirer sur un zombies seulement si il est en vie
            
            x,y = event.x,event.y 
            
            ids = self.canvas.find_overlapping(x,y,x,y)#cette méthode retourne les objets dans le rectangle donné (ici jsute un point  )
            
            for id in ids: #on parcours les objets détecter dans ids via une boucle
                if id in self.zombies: #si un zombies dans le dict zombie à été trouver 
                    
                    if  not(502 < x <562 and 336 < y <383): # création d'une zone ou le personnage ne peut pas tirer (quand le zombie est sur le joueur)
                        
                        self.joueur.tirer(self.zombies[id]) # appelle la fonction tirer

                        if self.zombies[id].life <= 0: #si la vie du zombies égale à 0
                            self.canvas.itemconfig(self.zombies[id],image = self.blue_gauche_damaged1)
                            self.score_joueur+= self.zombies[id].score   

                            #reduction décompte ultime
                            self.joueur.ultime_state -= 1
                            if not(self.survie_mode):
                                if self.joueur.ultime_state <= 0:
                                    self.canvas_droite.itemconfig(self.ultimate_text,text="ready",fill='green')
                                    
                                else:
                                    self.canvas_droite.itemconfig(self.ultimate_text,text=self.joueur.ultime_state)
                                # Mise à jour du Score #    
                            global SCORE
                            
                            SCORE=self.score_joueur
                            self.canvas_droite.itemconfig(self.score_text,text=self.score_joueur)
    
                            # suppression du zombie du canvas et du dict 
                            self.zombies.pop(id, None)
                            self.canvas.delete(id)   
    
                        elif(self.zombies[id].life == 1):
                            self.damagedZombie(self.zombies[id],1)
    
                        else:
                            self.damagedZombie(self.zombies[id])

    def damagedZombie(self,zombie,vie=None):

        if vie == 1:
            if zombie.couleur == 'bleu':
                if zombie.coord_start == (0,360):#associe l'orientation de la texture du zombie en fonction du lieu de spawn sur l'écran
                    self.canvas.itemconfig(zombie.id,image = self.blue_gauche_damaged1)#modifie l'image du joueur en cadavre  
                    
                elif zombie.coord_start == (540,0):
                    self.canvas.itemconfig(zombie.id,image = self.blue_haut_damaged1)#modifie l'image du joueur en cadavre  
                    
                elif zombie.coord_start == (1080,360):
                    self.canvas.itemconfig(zombie.id,image = self.blue_droite_damaged1)#modifie l'image du joueur en cadavre  
                    
                else: #(540,720)
                    self.canvas.itemconfig(zombie.id,image = self.blue_bas_damaged1)#modifie l'image du joueur en cadavre  
            else:
                if zombie.coord_start == (0,360):#associe l'orientation de la texture du zombie en fonction du lieu de spawn sur l'écran
                    self.canvas.itemconfig(zombie.id,image = self.red_gauche_damaged2)#modifie l'image du joueur en cadavre  
                    
                elif zombie.coord_start == (540,0):
                    self.canvas.itemconfig(zombie.id,image = self.red_haut_damaged2)#modifie l'image du joueur en cadavre  
                    
                elif zombie.coord_start == (1080,360):
                    self.canvas.itemconfig(zombie.id,image = self.red_droite_damaged2)#modifie l'image du joueur en cadavre  
                    
                else: #(540,720)
                    self.canvas.itemconfig(zombie.id,image = self.red_bas_damaged2)#modifie l'image du joueur en cadavre  
        else:
            if zombie.coord_start == (0,360):#associe l'orientation de la texture du zombie en fonction du lieu de spawn sur l'écran
                self.canvas.itemconfig(zombie.id,image = self.red_gauche_damaged1)#modifie l'image du joueur en cadavre  
                
            elif zombie.coord_start == (540,0):
                self.canvas.itemconfig(zombie.id,image = self.red_haut_damaged1)#modifie l'image du joueur en cadavre  
                
            elif zombie.coord_start == (1080,360):
                self.canvas.itemconfig(zombie.id,image = self.red_droite_damaged1)#modifie l'image du joueur en cadavre  
                
            else: #(540,720)
                self.canvas.itemconfig(zombie.id,image = self.red_bas_damaged1)#modifie l'image du joueur en cadavre  
                                                                 
    def orientationJoueur(self, event): #modifie l'iamge du joueur en fonction du clique sur le canva
        if self.joueur.life > 0 and self.temps !=0:
            x,y = event.x,event.y
            if   0 < x < 500 and 0 < y < 320: #clique en haut gauche écran
                self.canvas.itemconfig(self.joueur_canvas,image = self.joueur_haut_gauche)
            elif 580 < x < 1080 and 0 < y < 320: 
                self.canvas.itemconfig(self.joueur_canvas,image = self.joueur_haut_droite)
            elif 0 < x < 500 and 400 < y < 720: #clique gauche écran
                self.canvas.itemconfig(self.joueur_canvas,image = self.joueur_bas_gauche)
            elif 580 < x < 1080 and 400 < y < 720: #clique droit
                self.canvas.itemconfig(self.joueur_canvas,image = self.joueur_bas_droite)
            elif 0 < x < 500 and 320 < y < 400:
                self.canvas.itemconfig(self.joueur_canvas,image = self.joueur_gauche)
            elif 500 < x < 580 and 0 < y < 320:
                self.canvas.itemconfig(self.joueur_canvas,image = self.joueur_haut)
            elif 580 < x < 1080 and 320 < y < 400:
                self.canvas.itemconfig(self.joueur_canvas,image = self.joueur_droite)
            elif 500 < x < 580 and 400 < y < 720:
                self.canvas.itemconfig(self.joueur_canvas,image = self.joueur_bas)

    def ultime(self, event):
    
        if self.joueur.ultime_state <= 0 and self.joueur.life > 0:
            for i in self.zombies:
                self.canvas.delete(i)
                self.score_joueur += 10
                global SCORE
                SCORE = self.score_joueur
            self.zombies = {}
            self.joueur.ultime_state = 20
            self.canvas_droite.itemconfig(self.score_text,text=SCORE)
            self.canvas_droite.itemconfig(self.ultimate_text,text=self.joueur.ultime_state,fill=CONFIG["fontColor"])
           
class Zombie:   
    def __init__(self,canvas,canvas_gauche,canvas_joueur,coord_start,coord_x,coord_y,orientation,life=1,atk=1,score=10,couleur='vert'):
        
        self.life = life
        self.atk = atk
        self.coord_start = coord_start
        self.canvas = canvas
        self.canvas_gauche = canvas_gauche
        self.canvas_joueur = canvas_joueur
        self.score = score
        self.orientation = orientation
        self.couleur = couleur

        self.id = self.canvas.create_image(coord_x,coord_y,image=self.orientation) #créée une image sur le canvas pour chaques zombies

    def attack(self,cible):
        cible.life -= self.atk 
        if cible.life == 0:
            
            self.gameover = PhotoImage(file=CONFIG["cheminAcces"]+CONFIG["gameover"])
            self.mort = PhotoImage(file=CONFIG["cheminAccesjoueur"]+CONFIG["player_mort"])

            self.canvas.itemconfig(self.canvas_joueur,image = self.mort)#modifie l'image du joueur en cadavre    
            
            self.canvas.create_image(CONFIG["width"]/2,CONFIG["height"]/2,image=self.gameover)#ajout de l'image gameover

            #création du bouton vers le score qui apparait lorsque le joueur meurt
            
            self.quit_button = tk.Button(self.canvas_gauche, text = "Quit", command = lambda : verifNom(self.name_entry,self.canvas_gauche,self.label_error),width = 10,font = ('Arial', 20),fg='white',bg="#d92e2e")
             
            if CONFIG["mode"] == "libre":
                
                self.quit_button = tk.Button(self.canvas_gauche, text = "Quit", command =  lambda : verifNom(self.name_entry,self.canvas_gauche,self.label_error),width = 10,font = ('Arial', 20),fg='white',bg="#d92e2e")
                self.name_entry = tk.Entry(self.canvas_gauche)
                self.canvas_gauche.create_window(105, 150, window=self.quit_button)
                self.label_error = self.canvas_gauche.create_text(105,200,fill='red')
                self.canvas_gauche.create_window(105, 180, window=self.name_entry)
                
            else:
                 self.quit_button = tk.Button(self.canvas_gauche, text = "Quit", command = quitter,width = 10,font = ('Arial', 20),fg='white',bg="#d92e2e")
                 self.canvas_gauche.create_window(105, 150, window=self.quit_button)

    
    
    def move(self):#déplace le zombie dans une direction en fonction de son spawn et renvois ses coordonnées
        
        coord_zombie = self.canvas.coords(self.id) 
       
        if self.coord_start == (0,360):
            self.canvas.move(self.id,5,0)

        elif self.coord_start == (540,0):
            self.canvas.move(self.id,0,5)

        elif self.coord_start == (1080,360):
            self.canvas.move(self.id,-5,0)

        else: #(540,720)
            self.canvas.move(self.id,0,-5)

        return coord_zombie 

            
class Joueur:
    def __init__(self,canvas,life=3,atk=1):
        self.canvas = canvas
        self.life = life
        self.atk = atk
        self.ultime_state = 20
        
    def tirer(self,cible):
        
        cible.life -= self.atk 


def verifNom(entry_name,canvas,error): #vérifier le nom avant de l'envoyer 
    name = entry_name.get()
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9']
    
    if len(name) == 3: 
        for i in name:
            if not(i.lower() in char):
                canvas.itemconfigure(error,text="pas de caractères spéciaux",font=('Arial',11))
                break    
        else:
            game.destroy()
            ApplicationScore(name,SCORE,True)   
    else:
        canvas.itemconfigure(error,text="3 lettres",font=('Arial',15))

def quitter():
    game.destroy()
    ApplicationScore(new=False)
    
def lancement(joueur,carte,mode): #définition du joueur et de la map
    
    CONFIG["cheminAcces"] = "./img/%s/"%(carte)
    CONFIG["cheminAccesjoueur"] = "./img/players/%s/"%(joueur)
    CONFIG["mode"] = mode
    
    if carte == 'city':
        CONFIG["fontColor"] = 'white'
    else:
       CONFIG["fontColor"] = 'black'
    
    global game
    game = ApplicationJeux(3,1)#vie joueur,attaque joueur
    game.mainloop()        