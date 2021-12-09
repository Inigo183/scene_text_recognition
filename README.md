# scene_text_recognition
scene text recogition using different 

# Creating conda enviroment
conda create -f requirements.yml
It will create a conda enviorment named as tf
conda activate tf

# To use EAST, we have to unzip the 2 files, to do so enter EAST folder and execute
zip -s 0 east_text.zip --out compacted_east.zip
unzip compacted_east.zip

# To run EAST 
python text_detection.py -i images/(name) -east frozen_east_text_detection.pb 

# To run tesseract
python localize_text_recongition.py -i images/(path)
