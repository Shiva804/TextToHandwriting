from PIL import ImageFont,ImageDraw,Image
import random
import re
from docx2python import docx2python
import img2pdf
import os



s = input('Select paper type: ')



def text_process(x_axis,y_axis,filetype):
    
    image  = Image.open(filetype)
    draw  = ImageDraw.Draw(image)

    fontlist = ['./fonts/Fontsah.ttf','./fonts/handw.ttf','./fonts/Fontsah.ttf'] #array of fonts
    
    fontname = random.choice(fontlist) #select a random font from the array
    

    font = ImageFont.truetype(fontname,40) #assign the font

    read_text = open('./sample text/a.txt')
    data = read_text.read()


    nol = len(data.splitlines())
    read_text.close()
    c = 0
    i = 0
    p=0

  

    x=x_axis
    y=y_axis
    f=False
    read_text = open('./sample text/a.txt')
    while c<nol:
        rawdata = read_text.readline()
        
        c+=1    
        a_data = re.split(r'\s',rawdata)
        a_data = [i for i in a_data if i]
        # print(a_data)
        color = (13, 10, 158,255)
        for idx,word  in enumerate(a_data):
            

            if('*' in a_data[0]):
                color = (0, 0, 0,255)
            else:
                color = (13, 10, 158,255)

            if('*' in word[i]):
                    word = word[1:]
                   
            if(idx>=0):
                while(i < len(word)):
                    ast =  word[i]
                    # print(ast)
                    fontname = random.choice(fontlist)
                    font = ImageFont.truetype(fontname,40) #assign the font

                    if(ast=='#'):
                        y+=49.5
                        x=x_axis
                        f=True

                    else:
                        draw.text((x,y),ast,font=font,fill=color)
                        if(ast=='.' and a_data[-1]==word):
                            y+=49.5
                            x=x_axis
                            f=True
                            
                        else:

                            if ast=='i' or ast=='I' or ast=='l' or ast=='1' or ast==',':   
                                x+=12

                            else:
                                x+=16
                        
                    i+=1

                if(x>=1005):
                    if(y>=1590):
                        image.save("./output images/"+"img"+str(p)+'.png')
                        image  = Image.open(filetype)
                        draw  = ImageDraw.Draw(image)

                        x=x_axis
                        y=y_axis
                        p+=1
                    else:
                        y+=49.5
                        x=x_axis
                else:
                    if(f==False):
                        x+=25
                    else:
                        f=False

                i=0

        if(len(a_data)==0):
            if(y>=1590):
                image.save("./output images/"+"img"+str(p)+'.png')

                image  = Image.open(filetype)
                draw  = ImageDraw.Draw(image)
                x=x_axis
                y=y_axis
                p+=1
            else:
                y+=49.5
                x=x_axis

    image.save("./output images/"+"img"+str(p)+'.png')

    





def img_to_pdf():
    os.chdir('output images')
    
    k = False
    t=0

    while k!=True:
        filename = 'final'+str(t)+'.pdf'
        if(os.path.isfile('../pdfs/'+filename)):
            t+=1
        else:
            k=True
    filename = 'final'+str(t)+'.pdf'




    with open("../pdfs/"+filename, "wb") as f:
        f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith(".png")]))

    

if(s=='ruled'):

    x=200
    y=165
    filetype='./template/standard.jpg'

else:
    x=125
    y=165
    filetype='./template/standard1.jpg'




text_process(x,y,filetype)

img_to_pdf()