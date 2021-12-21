# scene_text_recognition
scene text detection and recognition using mutilpe methods  

To use all of them we used a conda environment, so we previuslly have miniconda installed.  

# Creating conda environment
~~~
conda env create -f requirements.yml
~~~
It will create a conda enviorment named as scene  
Run the command below to activate this environment  
~~~
conda activate scene
~~~

# Preparing to use EAST
we have to unzip the 2 files, to do so enter EAST folder and execute  
~~~
zip -s 0 east_text.zip --out compacted_east.zip  
unzip compacted_east.zip
~~~
## Running EAST 
### In EAST folder  
~~~
python text_detection.py -i images/name_image.png -east frozen_east_text_detection.pb 
~~~
# Running tesseract
## In tesseract folder  
~~~
python localize_text_tesseract.py -i images/name_image.png
~~~

# Running easyOCR
## in easyOCR folder
~~~
python easyOCR.py --image images/name_image.png --langs en
~~~

# Running MSER
## in mser folder

~~~
python3 mser.py --image images/name_image.png 
~~~

# Preparing to use ResNet model in character recognition
enter character_recog  
To be able to train the model, first we have to unzip dataset, do it with the command below  
~~~
unzip datasetAZ.zip
~~~
## Training the model
we have to indicate whcich dataset to use as A-Z character recognition, (digits is used internally) and the name of the model will result, .model extension  
~~~
python train_model.py --az A_Z_data.csv --model model_name.model
~~~
After trainning, it will create a model_name.model file  
## Predict with the model
~~~
python prediction.py -i images/name_image.png -m model_name.model
~~~
