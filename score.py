import tkinter as tk
import json

class ApplicationScore(tk.Tk):
    def __init__(self,nom=None,score=None,new=True):
        tk.Tk.__init__(self)
        
        self.title("the Last Of You")
        self.geometry("1080x720+200+30")
        self.resizable(width = False, height = False)
        self.iconbitmap("./img/logo.ico")
        self.configure(bg="black")

        self.nom = nom
        self.score = score
        self.new = new
        
        self.frameprincipal=tk.Frame(self,width=1080,height=720, bg = 'Black') #frame pour les scores 
        
        self.titre = tk.Label(self, text="Tableau des scores",font = ('Karmatic Arcade', 25), bg = 'Black', fg = 'white') 
        self.titre.pack()

        self.btnqui = tk.Button(self, text = "retour", width = -7, height = -5, font = ('Karmatic Arcade', 25), bg = 'Black', fg = 'White', command = self.mainMenu)
        self.btnqui.place(x = 830, y = 656)

        self.frameprincipal.pack()

        if new:
            self.showNewScore(self.nom,self.score) 
        else:
            self.showScore()

    def mainMenu(self): #retour menu principal
        self.destroy()
        from main import application
        app = application()
        app.mainloop()

    def showNewScore(self,nom,score):#fonction appelée en fin de partie 
        data = self.openData()
        for i,j in data.items():
            if i == nom and j > score:
                new_data = self.sortData(data)
                self.showData(new_data)
                break
        else:
            data[nom]=score             
            new_data = self.sortData(data)
            self.showData(new_data)
            self.newData(new_data)
    
    def showScore(self): #fonction appelée depuis le menu principal
        data = self.openData()
        self.showData(data)

    def openData(self): #ouvre le fichier json
        with open('data.json','r') as f:
            return json.load(f)        
       
    def sortData(self,data): #trie le dict en fonction du score
        new_data = sorted(data.items(),key=lambda x:x[1], reverse=True) #lambda est une fonction anonyme x est un argument 
        if len(new_data) == 11:
            new_data.pop(-1)
        return dict(new_data)
    
    def newData(self,data): #enrgistre les données dans le json
        with open('data.json','w') as f:
            return json.dump(data,f)
        
    def showData(self,data):  #affiche les scores à l'écran
        for i,j in data.items(): 
            bg = 'black'
            if i == self.nom:
                bg = 'green'
            self.score_label=tk.Label(self.frameprincipal,text="%s : %i"%(i,j),bg=bg,fg="white",font=('Arial',20)).pack() 
        if self.new:
            self.my_score=tk.Label(self.frameprincipal,text= 'ton score : %i'%(self.score),bg="black",fg="red",font=('Arial',20)).pack()