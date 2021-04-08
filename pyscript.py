from PIL import ImageFont,ImageDraw,Image
import random
import re

def text_process():
    image  = Image.open("./standard.jpg")
    draw  = ImageDraw.Draw(image)

    fontlist = ['Fontsah.ttf','handw.ttf'] #array of fonts
    
    fontname = random.choice(fontlist) #select a random font from the array

    font = ImageFont.truetype(fontname,40) #assign the font

    read_text = open('a.txt')
    data = read_text.read()

    nol = len(data.splitlines())
    read_text.close()
    c = 0
    i = 0

    x = 200  #x-cordinate
    y = 165  #y-cordinate

    
    read_text = open('a.txt')
    while c<nol:
        rawdata = read_text.readline()
        c+=1    
        rawdata.strip()
        for idx,word  in enumerate(re.split(r'\s',rawdata)):
            if(idx>=0):
                while(i < len(word)):
                    ast =  word[i]
                    print(ast)
                    fontname = random.choice(fontlist)
                    font = ImageFont.truetype(fontname,40) #assign the font
                    draw.text((x,y),ast,font=font,fill=(0,0,0,255))
                    if ast=='i' or ast=='I' or ast=='l' or ast=='1':
                        x+=12

                    else:
                        x+=16
                    i+=1

                x+=25
                i=0
        y+=49.5
        x=200

    image.save("wow.png")


text_process()