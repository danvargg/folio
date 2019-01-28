import glob
import cv2
import pandas as pd
from sklearn.metrics import r2_score
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
import os

dir = 'C:/Users/...' ## put the directory here

os.chdir(dir)

def read_images_in_folder():
    image_stack = []
    for img in glob.glob('./Training/*.png'): # All png images
        image_stack.append(cv2.imread(img))
    return image_stack

def resize_image(image_stack): # Image resizing is performed here
    im_resized_stack = []
    for img in image_stack:
        im_resize = cv2.resize(img, (250, 250), interpolation=cv2.INTER_CUBIC) # Setting image size to 100x100 pixels
        im_resized_stack.append(im_resize)
    return im_resized_stack

if __name__ == '__main__':
    image_stack = read_images_in_folder()
    image_resized_stack = resize_image(image_stack)

training = pd.read_csv('./Training/training.csv')

x_train = np.array(image_resized_stack)
x_train = np.reshape(x_train, (x_train.shape[0], -1))
y_train = np.array(training[['value']])
y_train = y_train.ravel()

def read_images_in_folder():
    image_stack2 = []
    for img in glob.glob('./Evaluation/*.png'): # All png images
        image_stack2.append(cv2.imread(img))
    return image_stack2

def resize_image(image_stack2): # Image resizing is performed here
    im_resized_stack2 = []
    for img in image_stack2:
        im_resize = cv2.resize(img, (250, 250), interpolation=cv2.INTER_CUBIC) # Setting image size to 100x100 pixels
        im_resized_stack2.append(im_resize)
    return im_resized_stack2

if __name__ == '__main__':
    image_stack2 = read_images_in_folder()
    image_resized_stack2 = resize_image(image_stack2)

evaluation = pd.read_csv('./Evaluation/evaluation.csv')

x_eval = np.array(image_resized_stack2)
x_eval = np.reshape(x_eval, (x_eval.shape[0], -1))
y_eval = np.array(evaluation[['value']])
y_eval = y_eval.ravel()

# Models
# Random Forest Regression
rf = RandomForestRegressor(n_estimators = 300, random_state = 0, verbose = 3)
rf.fit(x_train, y_train)

rf_predicted_train = rf.predict(x_train) 
rf_predicted_test = rf.predict(x_eval) # This is the prediction

rf_train_accuracy = r2_score(y_train, rf_predicted_train) # training accuracy

if  np.isnan(y_eval).any():
    print("ERROR: NO EVALUATION VALUE")
else:
    rf_eval_accuracy = r2_score(y_eval, rf_predicted_test) # evaluation accuracy, only if you provide the evaluation criteria

# SVR
svc = SVR(kernel = 'rbf', C = 10, verbose = 3)
svc.fit(x_train, y_train)

svc_predicted_train = svc.predict(x_train) 
svc_predicted_test = svc.predict(x_eval) # This is the prediction

svc_train_accuracy = r2_score(y_train, svc_predicted_train) # training accuracy

if  np.isnan(y_eval).any():
    print("ERROR: NO EVALUATION VALUE")
else:
    svc_eval_accuracy = r2_score(y_eval, svc_predicted_test) # evaluation accuracy, only if you provide the evaluation criteria


# --------------------------------------- Black and White Images ------------------------------------------- #

def recolor_image(im_resized_stack): # Image resizing is performed here
    im_recolor_stack = []
    for img in im_resized_stack:
        im_recolor = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        im_recolor_stack.append(im_recolor)
    return im_recolor_stack

if __name__ == '__main__':
    image_recolor_stack = recolor_image(image_resized_stack)

training = pd.read_csv('./Training/training.csv')

x_train_bw = np.array(image_recolor_stack)
x_train_bw = np.reshape(x_train_bw, (x_train_bw.shape[0], -1))
y_train_bw = np.array(training[['value']])
y_train_bw = y_train_bw.ravel()

# Evaluation set
def recolor_image(im_resized_stack2): # Image resizing is performed here
    im_recolor_stack2 = []
    for img in im_resized_stack2:
        im_recolor2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        im_recolor_stack2.append(im_recolor2)
    return im_recolor_stack2

if __name__ == '__main__':
    image_recolor_stack2 = recolor_image(image_resized_stack2)

evaluation = pd.read_csv('./Evaluation/evaluation.csv')

x_eval_bw = np.array(image_recolor_stack2)
x_eval_bw = np.reshape(x_eval_bw, (x_eval_bw.shape[0], -1))
y_eval_bw = np.array(evaluation[['value']])
y_eval_bw = y_eval_bw.ravel()

# Models
# Random Forest Regression
rf_bw = RandomForestRegressor(n_estimators = 300, random_state = 0, verbose = 3)
rf_bw.fit(x_train_bw, y_train_bw)

rf_predicted_train_bw = rf_bw.predict(x_train_bw) 
rf_predicted_test_bw = rf_bw.predict(x_eval_bw) # This is the prediction

rf_train_accuracy_bw = r2_score(y_train_bw, rf_predicted_train_bw) # training accuracy

if  np.isnan(y_eval_bw).any():
    print("ERROR: NO EVALUATION VALUE")
else:
    rf_eval_accuracy_bw = r2_score(y_eval_bw, rf_predicted_test_bw) # evaluation accuracy, only if you provide the evaluation criteria

# SVR
svc_bw = SVR(kernel = 'rbf', C = 10, verbose = 3)
svc_bw.fit(x_train_bw, y_train_bw)

svc_predicted_train_bw = svc_bw.predict(x_train_bw) 
svc_predicted_test_bw = svc_bw.predict(x_eval_bw) # This is the prediction

svc_train_accuracy_bw = r2_score(y_train_bw, svc_predicted_train_bw) # training accuracy

if  np.isnan(y_eval_bw).any():
    print("ERROR: NO EVALUATION VALUE")
else:
    svc_eval_accuracy_bw = r2_score(y_eval_bw, svc_predicted_test_bw) # evaluation accuracy, only if you provide the evaluation criteria

