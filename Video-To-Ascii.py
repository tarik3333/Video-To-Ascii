import PIL.Image
import cv2
import numpy as np
vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
success,image = vidcap.read()
frame = 0
while success:
  cv2.imwrite("frame%d.jpg" % frame, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  frame += 1

ASCII_CHAR=["@","#","S","%","?","*","+",";",":",",","."]


def resize(image,new_width=100):
    width,height=image.size
    ratio=height/width   
    print(width,height)
    new_height=int(new_width*ratio)
    print(new_width,new_height)
    resized_image=image.resize((new_width,new_height))
    return(resized_image)

def togray(image):
    grayedimage=image.convert("L")
    return grayedimage

def pixelto(image):
    pixel=image.getdata()
    chars="".join([ASCII_CHAR[pix//25] for pix in pixel])
    return(chars)
def main(new_width=100):
    vidcap = cv2.VideoCapture('deneme3.mp4')
    success,image = vidcap.read()
    frame = 0
    while success:
        cv2.imwrite("frame%d.jpg" % frame, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        frame+= 1
        
    for i in range(frame-1):  
        img=PIL.Image.open("frame%d.jpg" % i)
        New=pixelto(togray(resize(img))) 
        count=len(New)
        ascii_image="\n".join(New[i:(i+new_width)]for i in range(0,count,new_width))
        #print(ascii_image)
        with open("frame%d.txt" % i,"w") as f:
            f.write(ascii_image)
        

main()
    
