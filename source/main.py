#TODO: Include parameters for width and height
#TODO: Maybe including parameters for controlling time
#TODO: Now is using grey image to simplify things, Maybe have a distance function
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 #File Name : bg_remove.py
 #Creation Date : 31-07-2019
 #Created By : Rui An
#_._._._._._._._._._._._._._._._._._._._._.
import cv2
import time
import numpy as np

background_set_time = 5
cap = cv2.VideoCapture(0) 
bg_storage_path = "../background/"
pixel_diff_threshold = 20


def check_legal_choice(choice):
    if (choice == 'N' or choice == 'P' or choice == 'Q'): 
        return True 
    else: 
        return False 


def set_up_environment(bg_name):
    print("Please Make Sure No One is In Front Of the Camera")
    print("Will Take the Background Photo in 10 Seconds")
    counter = 0
    while (counter<10):
        print(counter)
        counter += 1
        time.sleep(1)
    print("Take New Background Photo")
    ret, frame = cap.read()
    while(True):
        cv2.imshow('Press y to save the file',frame) 
        if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
            cv2.imwrite('../background/' + bg_name, frame)
            cv2.destroyAllWindows()
            break


def extract_foreground(current_background):
    bg_path = bg_storage_path + current_background
    bg_img = cv2.imread(bg_path) 
    cv2.imshow('Current Background', bg_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    bg_height, bg_width, channel = bg_img.shape 
    # Create White Images
    white_image = 255 * np.ones(shape=[bg_height, bg_width, channel], dtype=np.uint8)
    print("Will Extract Foreground in 2 Seconds")
    time.sleep(2)
    print("Start Extract Foreground")
    while(True):
        ret, frame = cap.read()
        # bw_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_diff = np.abs(frame - bg_img) 
        height, width, channle = frame_diff.shape
        for i in range(height):
            for j in range(width):
                pixel_diff = frame_diff[i][j]
                to_cover = True 
                for k in range(3):
                    if (pixel_diff[k] > pixel_diff_threshold):
                        to_cover = False
                        break
                if (to_cover):
                    frame[i][j] = [255, 255, 255] 
        cv2.imshow('fuckthis', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

                

                
def main():
    print("-----------------Running Palimpsest Passage------------------")
    prompt = "N: Set Up New Environment, P: Use the Previous Environment Setting, Q: Quit\n"
    user_input = input(prompt)
    while(not check_legal_choice(user_input)):
        print("Illegal Choice!!! Please Reenter")
        user_input = input(prompt)
    if (user_input == 'N'):
        print("-----------------Setting Up New Environment-----------------")
        bg_file_name = input("Type in the New Background File Name\n") + ".jpg"
        print("--------------Creating New Background File " + bg_file_name + "--------------")
        set_up_environment(bg_file_name)
        print("----------------New Background Created--------------")
        print("----------------Start Main Process--------------")
        extract_foreground(bg_file_name)
    if (user_input == 'P'):
        bg_file_name = input("Type in the Previous Background File Name\n") + ".jpg"
        print("----------------Start Main Process--------------")
        extract_foreground(bg_file_name)

        



        

if __name__=="__main__":
    main()
