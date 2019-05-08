from bs4 import *
import requests
from tkinter import *
from functools import partial
import urllib.request
import webbrowser
from PIL import Image
from PIL import ImageTk
global url
c=0
def link(url1):
        webbrowser.open_new('https://cartoonhd.cz/movie/'+url1)
def link1(url2):
        webbrowser.open_new('https://www.imdb.com/'+url2)
def listing(url):    
    root1 = Tk() 
    root1.title("Movie Suggestion")
    canvas1 = Canvas(root1, height = 1000, width = 1000)
    scroll_y = Scrollbar(root1, orient=VERTICAL, command=canvas1.yview)
    scroll_x=Scrollbar(root1,orient=HORIZONTAL,command=canvas1.xview)
    f= Frame(canvas1)
    Label(f,text="Movie Name").grid(row=0,column=0)
    Label(f,text = "Year of Release").grid(row=0,column=2)
    Label(f,text = "Description").grid(row=0,column=3)
    Label(f,text = "Imdb Rating").grid(row=0,column=5)
    Label(f,text = "Director").grid(row=0,column=6)
    Label(f,text="Watch Online").grid(row=0,column=7)
    canvas1.pack()
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    d = soup.find_all('div',class_="lister-item mode-advanced") 
    c=0
    for i in d:
            name = i.find_all('div',class_="lister-item-content")[0].a
            yr = i.find_all('span',class_="lister-item-year text-muted unbold")[0]
            des = i.find_all('p',class_="text-muted")
            dr = i.find_all('p',class_="")[0].a
            if len(i.find_all('div',class_='inline-block ratings-imdb-rating'))==0:
                    pass
                    Label(f,text="-").grid(row=c+1,column=5)
            else:
                    rat = i.find_all('div',class_='inline-block ratings-imdb-rating')[0]
                    Label(f,text=rat.text).grid(row=c+1,column=5)
            url2 = name['href']
            '''asd=url2.index('?')
            url2 = url2[0:asd]
            if url.endswith('.com'):
                    url = url[:-4]
            print(url2)'''
            name1 = name.text
            name1 = name1.lower()
            nam = name1.replace(" ", "-")
            url1 = nam
            but = Button(f,text=name.text,height=4,width=25,bg="white",activebackground ="green",command=partial(link1,url2)).grid(row=c+1,column=0)
            Label(f,text=yr.text).grid(row=c+1,column=2)
            Label(f,text=des[1].text).grid(row=c+1,column=3)
            Label(f,text=dr.text).grid(row=c+1,column=6)
            but1 = Button(f,text=name.text,height=4,width=25,bg="white",activebackground ="green",command=partial(link,url1)).grid(row=c+1,column=7)
            c=c+1
    root.destroy()
    canvas1.create_window(0, 0, anchor='nw', window=f)
    canvas1.update_idletasks()
    canvas1.configure(scrollregion=canvas1.bbox('all'),  yscrollcommand=scroll_y.set )
    canvas1.configure(scrollregion=canvas1.bbox('all'),xscrollcommand=scroll_x.set)      
    canvas1.pack(fill='both', expand=True, side='left')
    scroll_y.pack(fill=Y, side='right')
    scroll_x.pack(fill=X,side='bottom')
def colorclick():
        But.configure(bg = "red")
        ButtonClick()
def colorclick1():
        But1.configure(bg = "red")
        ButtonClick()
def colorclick2():
        But2.configure(bg = "red")
        ButtonClick()
def colorclick3():
        But3.configure(bg = "red")
        ButtonClick()
def ButtonClick():
        s = But.cget('bg')
        s1 = But1.cget('bg')
        s2 = But2.cget('bg')
        s3 = But3.cget('bg')
        if(s=="red"):
                value = 1
        elif s1=="red":
                value = 2
        elif s2=="red":
                value = 3
        elif s3=="red":
                value = 4
        else:
                Label(canvas,text="Error")
        canvas.delete('all')
        if value==1:
                url="https://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter"
        elif value==2:
                url="https://www.imdb.com/search/title?genres=comedy&groups=top_1000&sort=user_rating&title_type=feature"
        elif value==3:
                url="https://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter"
        elif value==4:
                url="https://www.imdb.com/search/title?&genres=biography&explore=title_type,genres"
        else:
                print("ERROR")
        listing(url)
root = Tk()
root.title("Movie Suggestions")
width = 300
height = 300
canvas = Canvas(root, height = 1000, width = 1000)
img1 = Image.open("spongebob.png")
img1 = img1.resize((width,height), Image.ANTIALIAS)
photoImg1 =  ImageTk.PhotoImage(img1)
img2 = Image.open("sad.png")
img2 = img2.resize((width,height), Image.ANTIALIAS)
photoImg2 =  ImageTk.PhotoImage(img2)
img3 = Image.open("angry.png")
img3 = img3.resize((width,height), Image.ANTIALIAS)
photoImg3 =  ImageTk.PhotoImage(img3)
img4 = Image.open("demotivated.png")
img4 = img4.resize((width,height), Image.ANTIALIAS)
photoImg4 =  ImageTk.PhotoImage(img4)
But = Button(canvas,image = photoImg1,command = colorclick)
But1 = Button(canvas,image = photoImg2,command = colorclick1)
But2 = Button(canvas,image = photoImg3,command = colorclick2)
But3 = Button(canvas,image = photoImg4,command = colorclick3)
But.pack(side="left", fill='both', expand=True, padx=4, pady=4)
But1.pack(side="left", fill='both', expand=True, padx=4, pady=4)
But2.pack(side="left", fill='both', expand=True, padx=4, pady=4)
But3.pack(side="left", fill='both', expand=True, padx=4, pady=4)
canvas.pack()
root.mainloop()