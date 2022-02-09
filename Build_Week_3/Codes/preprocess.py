import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 
import PoseModule_final as pm


#detector = pm.poseDetector()
# Option 1 Preprocessing
'''
img =cv2.imread('./situp_exp_5.jpg',0)   # gray image
img = cv2.GaussianBlur(img,(3,3),0)
img= cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,199,5)#Threshold the image 


# empty skeleton
size = np.size(img)
skel = np.zeros(img.shape, np.uint8)

# cross shaped kernel
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3)) 

while True:
    open = cv2.morphologyEx(img,cv2.MORPH_OPEN, kernel) # open an image with kernel and remove noise
    img_sub = cv2.subtract(img,open)  # noise

    erod_img = cv2.erode(img,kernel)  # erode to shrink white 
    skel =cv2.bitwise_or(skel,img_sub)
    img=erod_img.copy()
    if cv2.countNonZero(img)== 0:
        break

plt.imshow(skel,cmap='gray')
plt.show()
'''

# Option 2 Preprocessing

# img = cv2.GaussianBlur(img,(9,9),0)
# img = cv2.Canny(img,100,200)
# cv2.imwrite('C:/Users/User/Documents/Build_Week_3/data/Train/pushup/image'+str(count+1)+'.jpg',img)
# src = 'C:/Users/User/Documents/Build_Week_3/split_data/Test/situp/'
# for filename in os.listdir(src):
# print(os.getcwd())


#ret, img= cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)#Threshold the image 
#img = cv2.GaussianBlur(img,(9,9),0)
#img = cv2.Canny(img,100,200)
    # count += 1
    # cv2.imwrite('C:/Users/User/Documents/Build_Week_3/data/Test/situp/situp'+str(count)+'.jpg',img)


# count=198
# lst =[]
# src = 'C:/Users/User/Documents/Build_Week_3/500_fitness_images/Train/situp/'
# for filename in os.listdir(src):
    
#     try:
#         img =cv2.imread(src+filename) 
#         img = pm.ManualFindPose(img)
#         count += 1
#         cv2.imwrite('C:/Users/User/Documents/Build_Week_3/data_3/Train/situp/'+'image'+str(count)+'.jpg',img)
#     except:
#         print('somethimg wrong')
#         lst.append(filename)
         
src='C:/Users/User/Documents/Build_Week_3/images_pred/'
img =cv2.imread(src+'download_5.jpg') 
img = pm.ManualFindPose(img)
plt.imshow(img)
plt.show()
