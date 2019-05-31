from tkinter import *
from PIL import Image, ImageTk
import cv2,time
import webbrowser

def contract_start():
    url = "https://www.facebook.com/profile.php?id=100003360365929&ref=bookmarks"
    webbrowser.open(url)

def start_button() :
    
    faceCascade = cv2.CascadeClassifier("facial_recognition_model.xml")

    video_capture = cv2.VideoCapture(0)

    while True:
    # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
        #flags=cv2.CV_HAAR_SCALE_IMAGE
                )

    # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
            cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
             break

# When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
    return 0
    
    
window = Tk()
window.title("Face")
window.geometry("400x400")
window.maxsize(width=400,height=400)
intro = Label(text="โปรแกรมจำลองใบหน้า")
intro.pack(pady=5)
bt = Button(window,text="เริ่ม",command=start_button)
bt.pack(pady=5)
contract = Label(text="จัดทำโดย ธีรพล อยู่คง")
contract.pack(pady=5)
bt2 = Button(window,text="ติดต่อ",command=contract_start)
bt2.pack(pady=5) 
load = Image.open("abc.jpg")
render = ImageTk.PhotoImage(load)
img = Label(window, image=render)
img.image = render
img.place(x=100,y=150,height=200,width=200)
window.mainloop()
