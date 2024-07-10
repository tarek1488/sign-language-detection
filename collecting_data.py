import cv2
import uuid
import time
import os

def read_data():
    # our signs
    labels = ['hello', 'iloveyou', 'yes', 'no', 'thankyou']
    
    # the path to the folder that will contain the images
    data_path = 'sign-language-dataset'
    
    # create the folder if it doesn't exist
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    
    # setting capture
    cap = cv2.VideoCapture(0)
    
    for label in labels:
        print(f'collecting images for {label}')    
        # sleep before start taking images for each label
        time.sleep(5) # 5 seconds 
        
        for i in range(15):
            # reading a frame
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture image")
                continue
            # setting image name
            image_name = os.path.join(data_path, label + '-' + '{}.jpg'.format(str(uuid.uuid1())))
            
            cv2.imwrite(image_name, frame)
            
            cv2.imshow('frame', frame)
            
            # wait for 2 seconds
            time.sleep(2)
            
            if cv2.waitKey(1) and 0xff == ord('q'):
                break
    
    cap.release()
    cv2.destroyAllWindows()
            
read_data()
