import cv2
import uuid
import time

def read_data():
    # our signs
    labels = ['hello', 'iloveyou', 'yes', 'no', 'thankyou' ]
    
    # the path to the folder that will contain the images
    data_path = 'D:\self-grinding\deeplearning\object-detection\sign-language-detector\sign-language-dataset'
    
    cap = cv2.VideoCapture(0)
    
    for label in labels:
        print(f'collecting images for {label}')
        for i in range(100):
            
            
            
            ret, frame = cap.read()
            
            frame_path =  data_path + label
            
            