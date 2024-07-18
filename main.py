from tkinter import *
from PIL import Image,ImageTk
from random import randint 


root = Tk()
root.title("Rock Scissor Paper")

root.configure(background = '#9b59b6')

rock_img = ImageTk.PhotoImage(Image.open('rockHuman.png'))
paper_img = ImageTk.PhotoImage(Image.open('paperHuman.jpg'))
scissors_img = ImageTk.PhotoImage(Image.open('scissorsHuman.png'))
rock_img_comp = ImageTk.PhotoImage(Image.open('rockComp.png'))
paper_img_comp = ImageTk.PhotoImage(Image.open('paperComp.png'))
scissors_img_comp = ImageTk.PhotoImage(Image.open('scissorsComp.png'))


 
#insert Image
user_label= Label(root,image=scissors_img,bg= '#9b59b6')
comp_label= Label(root,image=scissors_img_comp,bg= '#9b59b6')
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#score
playerScore=Label(root,text=0,font=100,bg= '#9b59b6',fg='white')
computerScore=Label(root,text=0,font=100,bg= '#9b59b6',fg='white')
playerScore.grid(row=1,column=3)
computerScore.grid(row=1,column=1)


#Indicator
user_indicator =Label(root,font=50,text='USER',bg= '#9b59b6',fg='white')
comp_indicator = Label(root,font=50,text='COMPUTER',bg= '#9b59b6',fg='white')
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#Massage
msg= Label(root, font=50,bg='#9b59b6', fg='white', text='YOU LOOSE')
msg.grid(row=3,column=2 )
# update massage

def updateMessage(x):
    msg['text']=x

#update user score
def updateUserScore():
    score= int(playerScore['text'])
    score += 1
    playerScore['text']= str(score)


#update Computer Score
def updateCompScore():
    score= int(computerScore['text'])
    score += 1
    computerScore['text']= str(score)



#check Winner
def checkWin(player, computer):
    if player == computer  :
        updateMessage("Its a tie !!!")
    elif player == 'rock':
        if computer =='paper':
            updateMessage('You Loose')
            updateCompScore()
        else:
            updateMessage('You Win')
            updateUserScore()
    elif player == 'paper':
        if computer =='scissors':
            updateMessage('You Loose')
            updateCompScore()
        else:
            updateMessage('You Win')
            updateUserScore()
    else:
        if computer =='rock':
            updateMessage('You Loose')
            updateCompScore()
        else:
            updateMessage('You Win')
            updateUserScore()
    # else:pass

#update choice

choices=['rock','paper','scissors']

def updateChoice(x):
# for computer
    compChoice = choices[randint(0,2)]
    if compChoice == 'rock':
        comp_label.configure(image=rock_img_comp)
    elif compChoice == 'paper':
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissors_img_comp)
    # else:
    #     pass
    
#for User
    if x=='rock':
        user_label.configure(image=rock_img)
    elif x=='paper':
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)
    # else:pass
    checkWin(x, compChoice)  
        


#buttons
rock= Button(root,width=20, height=2,text='ROCK',bg='#FF9E4D',fg='white', command= lambda:updateChoice('rock')).grid(row=2,column=1)
paper= Button(root,width=20,height=2,text='PAPER',bg='#FAD02E',fg='white',command= lambda:updateChoice('paper')).grid(row=2,column=2)
scissors= Button(root,width=20,height=2,text='SCISSORS',bg='#0ABDE3',fg='white',command= lambda:updateChoice('scissor')).grid(row=2,column=3)



root.mainloop()

