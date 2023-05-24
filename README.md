# Data Science Small Projects
Using ML algorithms for small applications and reports. Each project refers to its corresponding notebook file.

## :pushpin: General notes :pushpin:
---
- The data folder is empty due to sizing issues (if it doesn't exist create one), so please go ahead and add the neccesary files for each project.

- For the *movies related* projects, al the data is taken from the IMDB dataset: https://www.imdb.com/interfaces/, and then properly prepared for modelling. 

**However, each project provides the *polished dataset* such that there is no need to download datasets if you only want to run the final application.** 

- :warning: For a better viewing experience copy and paste the notebook https address to [Nbviewer](https://nbviewer.org/)

## :movie_camera: *Movies* Project :movie_camera:

### **The brief**
A recommandation system where based on a chosen id, the output consists of similar movies recommendation.
- *Model*: unsupervised KNN 
- *Libs*: sklearn, pandas, numpy
- *Notebook file*: movies.ipynb

### **Links and Notes**
Polished dataset:
- From Google drive (mandatory for the Application section): https://drive.google.com/file/d/1BasDf5kGMpARja5sO2tkgxqW_yalquPk/view?usp=sharing 

Note: 
**Section 0**: every such section consists of functions and libraries mandatory for the folowing sections, so please run these sections first;


## :chart_with_downwards_trend: *Movie Trends* Project :chart_with_downwards_trend:


### **The brief**
An application that uses polynomial regression to analyse and display past movie genre trends, based on IMDB dataset. The app also gives insigts on the most representative periods for each genre.

- *Model*: polynomial regression
- *Libs*: sklearn, pandas, matplotlib, numpy
- *Notebook file*: movie_trends.ipynb
### **Links and Notes**
Polished dataset:
- From Google drive (mandatory for the Application section): https://drive.google.com/file/d/1FeYNXyVxjiIxYYkywCJ_jk6Lt7sefpnX/view?usp=sharing;

## :computer: *Object Detection* Project :computer:


### **The brief**
The development of a model which recognizes and counts specific objects (laptop, keys, smartphone, keyboard, router, usb stick, server rack).  

- *Model*: YOLO
- *Libs*: ultralytics, roboflow
- *Notebook file*:object_detection.ipynb
### **Links and Notes**
Roboflow dataset (useful only if you want to retrain or use the dataset):
https://universe.roboflow.com/iulia-bunescu-vldcs/specific-electronics-challenge-v2/dataset/7


### **Some results**
<img src="\results_images\confusion_matrix_normalized.png" alt="Model Testing results" >

