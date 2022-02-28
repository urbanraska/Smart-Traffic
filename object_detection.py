from typing import Counter
from xml.dom.expatbuilder import theDOMImplementation
import cv2
import numpy as np
import operator


net=cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes=[]
with open('coco.names.txt','r') as f:
    classes=f.read().splitlines()

# cap= cv2.VideoCapture('resource/road.mp4')
#cap= cv2.VideoCapture(0)

Output_img = np.zeros((512, 912, 3), np.uint8)
img1=cv2.imread('Resources/traffic_jam.jpg')
img2=cv2.imread('Resources/no_jam_3.jpg')
img3=cv2.imread('Resources/traffic_jam_2.jpg')
img4=cv2.imread('Resources/traffic_jam_3.jpg')


# while True:
#  _, img=cap.read()


#image 1:
height,width,_=img1.shape

blob=cv2.dnn.blobFromImage(img1,1/255,(416,416),(0,0,0),swapRB=True,crop=False)
net.setInput(blob)
output_layers_names=net.getUnconnectedOutLayersNames()
layerOutputs=net.forward(output_layers_names)

boxes=[]
confidences=[]
class_ids=[]

center_x=0
center_y=0
counter1 = 0

for output in layerOutputs:
    for detection in output:
        scores=detection[5:]
        class_id=np.argmax(scores)
        confidence=scores[class_id]

        if confidence>0.5:
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)

        w =int(detection[2]*width)
        h =int(detection[3]*height)

        x= int(center_x - w/2)
        y= int(center_y - h/2)
        
        boxes.append([x,y,w,h])
        confidences.append((float(confidence)))
        class_ids.append(class_id)


indexes=cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)

font=cv2.FONT_HERSHEY_PLAIN
colors=np.random.uniform(0,255,size=(len(boxes),3))
    
   
# if len(indexes)>0:
for i in indexes.flatten():
    x,y,w,h=boxes[i]
    label=str(classes[class_ids[i]])
    #counting vehicles
    if label=='car' or 'truck' or 'bus' or 'motorcycle' or 'bicycle' :
        counter1 +=1
    confidence=str(round(confidences[i],2))
    color=colors[i]
    cv2.rectangle(img1,(x,y),(x+w, y+h),color,2)
    cv2.putText(img1,label+" "+confidence, (x, y+20),font,2,(255,255,255),2)


#image 2:
height,width,_=img2.shape

blob=cv2.dnn.blobFromImage(img2,1/255,(416,416),(0,0,0),swapRB=True,crop=False)
net.setInput(blob)
output_layers_names=net.getUnconnectedOutLayersNames()
layerOutputs=net.forward(output_layers_names)

boxes=[]
confidences=[]
class_ids=[]

center_x=0
center_y=0
counter2 = 0


for output in layerOutputs:
    for detection in output:
        scores=detection[5:]
        class_id=np.argmax(scores)
        confidence=scores[class_id]

        if confidence>0.5:
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)

        w =int(detection[2]*width)
        h =int(detection[3]*height)

        x= int(center_x - w/2)
        y= int(center_y - h/2)
        
        boxes.append([x,y,w,h])
        confidences.append((float(confidence)))
        class_ids.append(class_id)


indexes=cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)

font=cv2.FONT_HERSHEY_PLAIN
colors=np.random.uniform(0,255,size=(len(boxes),3))
    
   
# if len(indexes)>0:
for i in indexes.flatten():
    x,y,w,h=boxes[i]
    label=str(classes[class_ids[i]])
    if label=='car' or 'truck' or 'bus' or 'motorcycle' or 'bicycle' :
        counter2 +=1
    confidence=str(round(confidences[i],2))
    color=colors[i]
    cv2.rectangle(img2,(x,y),(x+w, y+h),color,2)
    cv2.putText(img2,label+" "+confidence, (x, y+20),font,2,(255,255,255),2)


#image 3:
height,width,_=img3.shape

blob=cv2.dnn.blobFromImage(img3,1/255,(416,416),(0,0,0),swapRB=True,crop=False)
net.setInput(blob)
output_layers_names=net.getUnconnectedOutLayersNames()
layerOutputs=net.forward(output_layers_names)

boxes=[]
confidences=[]
class_ids=[]

center_x=0
center_y=0
counter3 = 0


for output in layerOutputs:
    for detection in output:
        scores=detection[5:]
        class_id=np.argmax(scores)
        confidence=scores[class_id]

        if confidence>0.5:
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)

        w =int(detection[2]*width)
        h =int(detection[3]*height)

        x= int(center_x - w/2)
        y= int(center_y - h/2)
        
        boxes.append([x,y,w,h])
        confidences.append((float(confidence)))
        class_ids.append(class_id)


indexes=cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)

font=cv2.FONT_HERSHEY_PLAIN
colors=np.random.uniform(0,255,size=(len(boxes),3))
    
   
# if len(indexes)>0:
for i in indexes.flatten():
    x,y,w,h=boxes[i]
    label=str(classes[class_ids[i]])
    if label=='car' or 'truck' or 'bus' or 'motorcycle' or 'bicycle' :
        counter3 +=1
    confidence=str(round(confidences[i],2))
    color=colors[i]
    cv2.rectangle(img3,(x,y),(x+w, y+h),color,2)
    cv2.putText(img3,label+" "+confidence, (x, y+20),font,2,(255,255,255),2)


#image 4:
height,width,_=img4.shape

blob=cv2.dnn.blobFromImage(img4,1/255,(416,416),(0,0,0),swapRB=True,crop=False)
net.setInput(blob)
output_layers_names=net.getUnconnectedOutLayersNames()
layerOutputs=net.forward(output_layers_names)

boxes=[]
confidences=[]
class_ids=[]

center_x=0
center_y=0
counter4 = 0


for output in layerOutputs:
    for detection in output:
        scores=detection[5:]
        class_id=np.argmax(scores)
        confidence=scores[class_id]

        if confidence>0.5:
            center_x = int(detection[0]*width)
            center_y = int(detection[1]*height)

        w =int(detection[2]*width)
        h =int(detection[3]*height)

        x= int(center_x - w/2)
        y= int(center_y - h/2)
        
        boxes.append([x,y,w,h])
        confidences.append((float(confidence)))
        class_ids.append(class_id)


indexes=cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)

font=cv2.FONT_HERSHEY_PLAIN
colors=np.random.uniform(0,255,size=(len(boxes),3))
    
   
# if len(indexes)>0:
for i in indexes.flatten():
    x,y,w,h=boxes[i]
    label=str(classes[class_ids[i]])
    if label=='car' or 'truck' or 'bus' or 'motorcycle' or 'bicycle' :
        counter4 +=1
    confidence=str(round(confidences[i],2))
    color=colors[i]
    cv2.rectangle(img4,(x,y),(x+w, y+h),color,2)
    cv2.putText(img4,label+" "+confidence, (x, y+20),font,2,(255,255,255),2)


print("Total Vehicles in Road 1:" + str(counter1))
print("Total Vehicles in Road 2:" + str(counter2))
print("Total Vehicles in Road 3:" + str(counter3))
print("Total Vehicles in Road 4:" + str(counter4))
print('\n')
 
    # cv2.putText(img, "VEHICLE COUNTER :" + str(counter), (250, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
cv2.imshow('Image1',img1)
cv2.imshow('Image2',img2)
cv2.imshow('Image3',img3)
cv2.imshow('Image4',img4)


#dictionary declaration
con={}

#check for congestion
congestion=35
if counter1 >congestion:
    x='Road1'
    y=counter1
    con[x]=y
if counter2 >congestion:
    x='Road2'
    y=counter2
    con[x]=y
if counter3 >congestion:
    x='Road3'
    y=counter3
    con[x]=y
if counter4 >congestion:
    x='Road4'
    y=counter4
    con[x]=y

# print(con)

#check no. of congested road is one or not
if len(con)==1:
    for key in con:
        print("Give Green signal on",key)
        text=key
        # print(text)
        cv2.putText(Output_img, "Give Green signal on "+text, (220, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 0), 2)
        cv2.imshow("Output", Output_img)

elif len(con)>1:
    #soring the dictionary
    sorted_dict = sorted(con.items(),
    key = operator.itemgetter(1))

    sorted_dict = dict( sorted(con.items(), key=operator.itemgetter(1),reverse=True))

    # Printing sorted dictionary
    # print("Sorted dictionary is :")
    # print(sorted_dict)
    k=200
    c=1
    for key in sorted_dict:
        print("Give Green signal on",key)
        text=key
        cv2.putText(Output_img,str(c)+". Give Green signal on "+text, (220, k), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 0), 2)
        k=k+50
        c=c+1
    cv2.imshow("Output", Output_img)
else:
    print("NO TRAFFIC JAM DETECTED!!!! TRAFFIC IS SMOOTH!!!")      
    cv2.putText(Output_img, "NO TRAFFIC JAM DETECTED!!!! TRAFFIC IS SMOOTH!!!", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 0), 2)
    cv2.imshow("Output", Output_img)            







cv2.waitKey(0)
#     if cv2.waitKey(1) == 13:
#         break
# cap.release()
cv2.destroyAllWindows()



