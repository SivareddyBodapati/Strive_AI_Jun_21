import cv2
import mediapipe as mp
import os

def frame_taker_time_based(exercise_category, dir_name, videopath, time_skip, time_interval_start, time_interval_end):
    #Time Basis - Multiple Time Interval
    cap = cv2.VideoCapture(videopath)
    count = 0
    time_skip = float(time_skip)

    # Set the Time Interval
    start_time = time_interval_start #in miliseconds
    end_time = time_interval_end #in miliseconds
    cap.set(0, start_time) #0 refers to time position of the video


    while (cap.isOpened()):
        ret, frame = cap.read() 

        if ret:
            #Saving individual frames
            #Saving every 60 frames
        
            #Creating Strings & Process
            directory = exercise_category
            parent_directory = 'C:/Users/User/Documents/Build_Week_3/data'
            path = os.path.join(parent_directory, directory)
            if not os.path.exists(path):
                os.mkdir(path)

            image_name = dir_name +'_timenum'+str(cap.get(0)//1000)+'_s_index_' + str(count+1) + '.jpg'
            image_dir = os.path.join(path, image_name) 

            print('Creating...'+image_dir)
        
            #Saving
            cv2.imwrite(image_dir, frame)
        
            #counter
            count += 1
            current_timestep = cap.get(0)
            next_timestep = cap.get(0) + time_skip

            cap.set(0, next_timestep) #0 is for position of video in miliseconds

            if next_timestep >= end_time:
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()

    return

def frame_taker_frame_based(dir_name, videopath, frame_skip, frame_interval_start, frame_interval_end):
    cap = cv2.VideoCapture(videopath)
    count = 0

    # Set the Frame Interval
    start_frame = frame_interval_start
    end_frame = frame_interval_end
    cap.set(0, start_frame) #0 refers to time position of the video

    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret:
            #Saving individual frames
            #Saving every 60 frames
        
            #Creating Strings & Process
            directory = dir_name
            parent_directory = 'C:/Users/ASUS/Documents/Codes/Fitness_CV/data'
            path = os.path.join(parent_directory, directory)
            if not os.path.exists(path):
                os.mkdir(path)

            image_name = dir_name + '_framenum'+str(count)+'.jpg'
            image_dir = os.path.join(path, image_name) 

            print('Creating...'+image_dir)
        
            #Saving
            cv2.imwrite(image_dir, frame)
        
            #counter
            count += frame_skip
            cap.set(1, count) # 1 is for index of frames

            if count >= frame_interval_end:
                break
        else:
            break
            
    cap.release()
    cv2.destroyAllWindows()

    return