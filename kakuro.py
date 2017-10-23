# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from utils import *
from csp import *
from search import *
from Tkinter import *
import time

EPADDING=8
__author__ = "Christian"

easy=[[ ['black']    ,['black']      ,['grey',4,0]   ,['grey',10,0]  ,['black']      ,['black']      ,['black']     ],
      [ ['black']    ,['grey',0,4]   ,['white']      ,['white']      ,['black']      ,['grey',3,0]   ,['grey',4,0]  ],
      [ ['black']    ,['grey',0,3]   ,['white']      ,['white']      ,['grey',11,4]  ,['white']      ,['white']     ],
      [ ['black']    ,['grey',3,0]   ,['grey',4,10]  ,['white']      ,['white']      ,['white']      ,['white']     ],
      [ ['grey',0,11],['white']      ,['white']      ,['white']      ,['white']      ,['grey',4,0]   ,['black']     ],
      [ ['grey',0,4] ,['white']      ,['white']      ,['grey',0,4]   ,['white']      ,['white']      ,['black']     ],
      [ ['black']    ,['black']      ,['black']      ,['grey',0,3]   ,['white']      ,['white']      ,['black']     ]]
   
      
medium=[[ ['black']       ,['grey',23,0]  ,['grey',30,0]  ,['black']      ,['black']      ,['grey',27,0]  ,['grey',12,0]  ,['grey',16,0]  ],
        [ ['grey',0,16]   ,['white']      ,['white']      ,['black']      ,['grey',17,24] ,['white']      ,['white']      ,['white']      ],
        [ ['grey',0,17]   ,['white']      ,['white']      ,['grey',15,29] ,['white']      ,['white']      ,['white']      ,['white']      ],
        [ ['grey',0,35]   ,['white']      ,['white']      ,['white']      ,['white']      ,['white']      ,['grey',12,0]  ,['black']      ],
        [ ['black']       ,['grey',0,7]   ,['white']      ,['white']      ,['grey',7,8]   ,['white']      ,['white']      ,['grey',7,0]   ],
        [ ['black']       ,['grey',11,0]  ,['grey',10,16] ,['white']      ,['white']      ,['white']      ,['white']      ,['white']      ],
        [ ['grey',0,21]   ,['white']      ,['white']      ,['white']      ,['white']      ,['grey',0,5]   ,['white']      ,['white']      ],
        [ ['grey',0,6]    ,['white']      ,['white']      ,['white']      ,['black']      ,['grey',0,3]   ,['white']      ,['white']      ]]

difficult=[[ ['black']       ,['black']      ,['black']      ,['grey',14,0]  ,['grey',25,0]  ,['black']      ,['black']      ,['black']      ,['grey',6,0]   ,['grey',13,0]  ,['black']      ,['black']      ],
         [ ['black']       ,['grey',14,0]  ,['grey',12,8]  ,['white']      ,['white']      ,['black']      ,['grey',15,0]  ,['grey',11,5]  ,['white']      ,['white']      ,['grey',10,0]  ,['grey',22,0]  ], 
         [ ['grey',0,29]   ,['white']      ,['white']      ,['white']      ,['white']      ,['grey',15,33] ,['white']      ,['white']      ,['white']      ,['white']      ,['white']      ,['white']      ],
         [ ['grey',0,14]   ,['white']      ,['white']      ,['grey',7,25]  ,['white']      ,['white']      ,['white']      ,['white']      ,['grey',12,0]  ,['grey',16,9]  ,['white']      ,['white']      ],
         [ ['black']       ,['grey',12,0]  ,['grey',4,11]  ,['white']      ,['white']      ,['white']      ,['grey',22,0]  ,['grey',15,27] ,['white']      ,['white']      ,['white']      ,['white']      ],
         [ ['grey',0,20]   ,['white']      ,['white']      ,['white']      ,['white']      ,['grey',9,29]  ,['white']      ,['white']      ,['white']      ,['white']      ,['grey',10,0]  ,['grey',6,0]   ],
         [ ['grey',0,11]   ,['white']      ,['white']      ,['grey',12,0]  ,['grey',11,16] ,['white']      ,['white']      ,['white']      ,['grey',25,0]  ,['grey',5,10]  ,['white']      ,['white']      ],
         [ ['black']       ,['grey',16,0]  ,['grey',24,23] ,['white']      ,['white']      ,['white']      ,['white']      ,['grey',11,19] ,['white']      ,['white']      ,['white']      ,['white']      ],
         [ ['grey',0,27]   ,['white']      ,['white']      ,['white']      ,['white']      ,['grey',5,0]   ,['grey',9,11]  ,['white']      ,['white']      ,['white']      ,['grey',10,0]  ,['grey',16,0]  ],
         [ ['grey',0,15]   ,['white']      ,['white']      ,['grey',4,0]   ,['grey',12,11] ,['white']      ,['white']      ,['white']      ,['white']      ,['grey',14,16] ,['white']      ,['white']      ],
         [ ['grey',0,35]   ,['white']      ,['white']      ,['white']      ,['white']      ,['white']      ,['white']      ,['grey',0,27]  ,['white']      ,['white']      ,['white']      ,['white']      ],
         [ ['black']       ,['black']      ,['grey',0,5]   ,['white']      ,['white']      ,['black']      ,['black']      ,['grey',0,8]   ,['white']      ,['white']      ,['black']      ,['black']      ]]
                
class Kakuro(CSP):
                        
    __vars=[]
    __whites=[]
    __domains={}
    __grid=[]
    
    #Find the __vars and the horizontal combination of [grey],[white],[white]....
    def __search_horizontal(self):
        row=[]
        rows=[]
        for i in range(0,len(self.__grid)):   
            for j in range (0,len(self.__grid)):
                if(self.__grid[i][j][0]=='white' and self.__grid[i][j-1][0]=='grey'):
                    row=[]
                    row_neighbor=[]
                    name='X'+`i`+"_"+`j`
                    self.__vars.append(name)
                    row.append(self.__grid[i][j-1][2]) #every row has the sum that the variables at this row must have
                    row.append(name)
                elif(self.__grid[i][j][0]=='white'):
                    name='X'+`i`+"_"+`j`
                    self.__vars.append(name)
                    row.append(name)
                    if(j==len(self.__grid[0])-1):
                        rows.append(tuple(row))
                elif((self.__grid[i][j][0]=='black' or self.__grid[i][j][0]=='grey') and self.__grid[i][j-1][0]=='white'):
                    rows.append(tuple(row))
        return list(set(rows))

	#Find the vertical combination of [grey],[white],[white]....	
    def __search_vertical(self):
        i=0
        col=[]
        cols=[]
        columns=zip(*self.__grid)
        for column in columns:
            for j in range(len(column)):
                if(column[j][0]=='white' and column[j-1][0]=='grey'):
                    col=[]
                    name='X'+`j`+"_"+`i`
                    col.append(column[j-1][1])  #every col has the sum that the variables at this col must have
                    col.append(name)
                elif(column[j][0]=='white'):
                    name='X'+`j`+"_"+`i`
                    col.append(name)
                    if(j==len(column)-1):
                          cols.append(tuple(col)) 
                elif((column[j][0]=='black' or column[j][0]=='grey') and column[j-1][0]=='white'): 
                    cols.append(tuple(col))     
            i+=1
        return list(set(cols)) 
    
    def __constraints(self,A,a,B,b):
        if (a==b): 
            return False
        for w in self.__whites:
            if (A in w and B in w): 
                i=1
                values = []
                n = copy.deepcopy(list(w)) 
                s=n.pop(0) 
                for v in n:
                    if (v in self.assignments): 
                        if (v==A):
                            i=i-1
                        i=i+1
                for v in n:
                    if (v in self.assignments and v!=A and v!=B):
                        values.append(self.assignments[v])
                        s=s-self.assignments[v]
                if (a not in values):
                    s=s-a
                if (b not in values):
                    s=s-b          
                if (i<len(n) and s<=0) or (i==len(n) and s!=0):
                    return False
        return True                    
 
    def __init__(self,grid):
        self.__whites=[]
        self.__vars=[]
        self.__domains={}
        self.neighbors={}
        self.__grid=grid
        rows=self.__search_horizontal()
        cols=self.__search_vertical()
        for i in rows:
            self.__whites.append(i) # __whites is a list of tuples in which every tuple has some vars and the sum that they must have
        for i in cols:
            self.__whites.append(i)
            
        #Instantiate the domain
        for var in self.__vars:
            self.__domains[var]=range(1,10)

        #Find the neighbors
        for var in self.__vars:
            self.neighbors[var]=[]
            for w in self.__whites:
                if(var in w):
                    for v in w:
                        if(type(v)!=int and var!=v):
                            self.neighbors[var].append(v)
                            
        CSP.__init__(self, self.__vars, self.__domains, self.neighbors, self.__constraints)

class KakuroUI(Frame):

    __puzzle=[]
    __solution={}	
    
    def __init__(self, parent):
        self.parent = parent
        Frame.__init__(self, parent)
        self.parent.title("Kakuro")
        self.__start_game()

    #Creates the initial menu that lets you choose a puzzle	
    def __start_game(self):
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.grid_columnconfigure(1,weight=1)
        self.parent.grid_columnconfigure(2,weight=1)
        l=Label(self.parent,text="Choose a difficulty")
        l.grid(row=0,column=1,sticky=N+E+W,rowspan=2)
        variable = StringVar(self.parent)
        variable.set("Easy") # default value
        w=OptionMenu(self.parent,variable,"Easy","Medium","Difficult")
        w.grid(row=2,column=1,sticky=W+E+N+S)

        def __choose_puzzle():
            if variable.get()=="Easy":
                kak=Kakuro(easy)		#Creates a Kakuro csp
                k=backtracking_search(kak)	#Solves it with backtracking
                self.__solution=kak.display(k)	#Gets the solution
                self.__puzzle=easy
                self.__draw_puzzle()
            elif variable.get()=="Medium":
                kak=Kakuro(medium)
                k=backtracking_search(kak)
                self.__solution=kak.display(k)
                self.__puzzle=medium
                self.__draw_puzzle()
            else:
                kak=Kakuro(difficult)
                k=backtracking_search(kak)
                self.__solution=kak.display(k)
                print(self.__solution)
                self.__puzzle=difficult
                self.__draw_puzzle()
        
        b=Button(self.parent,text="PLAY",command=__choose_puzzle)
        b.grid(row=3,column=1,sticky=S+E+W)
        
    #Draws the chosen puzzle in another window using the entry widget
    def __draw_puzzle(self):
        top=Toplevel()
        top.title("Kakuro puzzle")
		
	#Checks if the input value is correct(Using the solution from the backtracking)
        def check_puzzle(event,row,col):
            var='X'+`row`+'_'+`col`
            tval=self.__solution[var]
            uval=event.widget.get()
            if uval==str(tval):
                del self.__solution[var]
                event.widget.config(disabledbackground="white",state=DISABLED)
                if(len(self.__solution)==0):	#If its the last correct input show victory screen
                    w=Canvas(top, width=100, height=50,background="green")
                    w.create_text(50,25,text="You Won!",justify=CENTER,font="Helvetica 12 bold")
                    w.place(relx=.5, rely=.5, anchor="center")
            elif uval!="" and uval!=str(tval):
                event.widget.config(bg="red")
            
        
        for row in range(len(self.__puzzle)):
            for col in range(len(self.__puzzle[0])):
                if self.__puzzle[row][col][0]=="white":		
                    e=Entry(top,font="Helvetica 8",justify=CENTER,width=3)
                    e.grid(row=row,column=col,ipady=EPADDING,ipadx=EPADDING)
                    e.bind("<KeyRelease>",lambda event,r=row,c=col: check_puzzle(event,r,c))
                elif self.__puzzle[row][col][0]=="black":
                    Entry(top,state=DISABLED,disabledbackground="black",width=3).grid(row=row,column=col,ipady=EPADDING,ipadx=EPADDING)
                else:   #Grey Blocks
                    if self.__puzzle[row][col][2]==0:
                        val=`self.__puzzle[row][col][1]`
                    elif self.__puzzle[row][col][1]==0:
                        val=`self.__puzzle[row][col][2]`
                    else:
                        val=`self.__puzzle[row][col][1]`+'\\'+`self.__puzzle[row][col][2]`
                    sv=StringVar(parent, value=val)
                    e=Entry(top,state=DISABLED,borderwidth=0,font = "Helvetica 8",
                            justify=CENTER,textvariable=sv,width=3).grid(row=row,column=col,ipady=EPADDING,ipadx=EPADDING)
               
        def __solve_puzzle():	#Solves the puzzle using the backtracking solution
            for key in self.__solution:
                val=self.__solution[key]
                sv=StringVar(top, value=val)
                Entry(top,font = "Helvetica 8",state=DISABLED,disabledbackground="white",
                      justify=CENTER,textvariable=sv,width=3).grid(row=key.split("_")[0][1:], #Split X12_9 to X12 and 9(for column)
                                    column=key.split("_")[1],ipady=EPADDING,ipadx=EPADDING)   #and remove the X

        def __help_puzzle():	#Helps the player with a random block of the puzzle and removes the answer from the solution
            if(len(self.__solution)>0):
                key=random.choice(self.__solution.keys())
                val=self.__solution[key]
                sv=StringVar(top, value=val)
                Entry(top,font = "Helvetica 8",state=DISABLED,disabledbackground="white",
                    justify=CENTER,textvariable=sv,width=3).grid(row=key.split("_")[0][1:],
                    column=key.split("_")[1],ipady=EPADDING,ipadx=EPADDING)
                del self.__solution[key]
            
        b1=Button(top,text="SOLVE",command=__solve_puzzle)
        b1.grid(row=len(self.__puzzle)+1,column=0,columnspan=2,sticky=S+W)
        b2=Button(top,text="HELP",command=__help_puzzle)
        b2.grid(row=len(self.__puzzle)+1,column=len(self.__puzzle)-2,columnspan=2,sticky=S+E)
        
    
parent=Tk()
kakui=KakuroUI(parent)
kakui.mainloop()
