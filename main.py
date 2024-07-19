from tkinter import *
from tkinter import messagebox as mb #importing message box to display the result
import json
from datetime import *
from time import *
import random

root=Tk()  #creating an instance of Tk()
root.geometry("905x500") 
root.title("QUIZ")
with open("quiz.json") as f:
    obj=json.load(f) 
#converting json array to python lists
q=(obj['ques'])
options=(obj['options'])
a=(obj['ans'])

class Quiz:
    def __init__(self):
        self.qn=0
        self.opt_selected=IntVar() #initialised to int,can hold only integer values
        self.opts=self.radiobtns() #to create 4 radio buttons for 4 options
        self.ques=self.question(self.qn)
        self.display_options(self.qn)
        self.buttons()
        self.correct=0
          
    def question(self,qn): #to display questions
        t=Label(root,text="QUIZ",width=75,bg="#F2A30F",fg="white",font=("times",15,"bold"))
        t.place(x=0,y=2)
        z=Label(root,text="Instructions: (i)If the question is unattempted or wrong no marks are awarded\n(ii)Each correct answer is awarded 1 mark",width=75,bg="black",fg="white",font=("times",15,"bold"))
        z.place(x=0,y=450)
        qn=Label(root,text=random.choice(q[qn]),width=60,font=("times",16,"bold"),anchor="w")
        qn.place(x=70,y=100)
        return qn
    def radiobtns(self): #to create radio buttons
        val=0
        b=[]
        yp=150
        while val<4:
            btn=Radiobutton(root,text=" ",variable=self.opt_selected,value=val+1,font=("times",14))
            b.append(btn)
            btn.place(x=100,y=yp)
            val+=1
            yp+=40
        return b
    def display_options(self,qn): #to display options
        val=0
        self.opt_selected.set(0) #ensuring no radio button is selected by default
        self.ques['text']=q[qn]
        for op in options[qn]:
            self.opts[val]['text']=op
            val+=1
    def buttons(self):  #to display next and quit buttons
        nbutton=Button(root,text="Next",command=self.next_btn,width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton.place(x=395,y=380)
        quitbutton=Button(root,text="Quit",command=root.destroy,width=10,bg="red",fg="white",font=("times",16,"bold"))
        quitbutton.place(x=775,y=50)
    def checkans(self,qn):  #to check answers
        if self.opt_selected.get()==a[qn]:
            return True
    def next_btn(self):     #to display questions simultaneously
        if self.checkans(self.qn):
            self.correct+=1
        self.qn+=1
        if self.qn==len(q):
            root.destroy()
            self.display_result()
            
        else:
            self.display_options(self.qn)
    def display_result(self):  #to display reuslt
        score=int(self.correct/len(q)*100)
        result=("Score:"+str(score)+"%")
        wc=len(q)-self.correct
        correct="No.of correct answers:"+str(self.correct)
        wrong="No.of wrong answers:"+str(wc)
        if score>=90:
            s="Excellent, Keep it up!!!"
        elif score>=80 and score<90:
            s="Very Good!!"
        elif score>=70 and score<80:
            s="Good"
        elif score>=60 and score<70:
            s="Needed to improve"
        elif score<60:
            s="Work Hard!!"
        mb.showinfo("Result","\n".join([result,correct,wrong,s]))
        
        
qquiz=Quiz()
#root.mainloop()
def counter(times=timedelta(seconds=901)):
        times=times-timedelta(seconds=1)
        time.configure(text=times)
        time.after(800,lambda n=times:counter(n))
        now=datetime.now()-datetime.now()
        if times==now:
            root.destroy()
            qquiz.display_result()
time=Label(root,font=("Arial",20,"bold"))
time.pack()

k=Label(root,command=counter(),font=("Arial",20,"bold"))
k.pack(x=500,y=200)
root.mainloop()
