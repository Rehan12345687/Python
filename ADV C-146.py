from tkinter import *
root = Tk()

root.title("ADV C-146")
root.geometry("400x500")

i = Label(root,text = "fibvonacci series")
label_flower = Label(root)
label_spiral = Label(root)

def fibo(): 
    num = 10
    f_no = 0
    s_no = 1
    sum = 0
    counter = 1
    while(counter<=num):
        i["text"]+=str(sum)+" "
        counter = counter+1
        f_no = s_no
        s_no = sum
        sum = f_no + s_no
    label_flower["text"]="flower is fully bloomed"
    label_spiral["text"]="spiral in right direction are "+str(f_no)+" and spirals in left direction are " +str(s_no)+"\n. Total spirals are "+ str(sum)       
    
btn = Button 