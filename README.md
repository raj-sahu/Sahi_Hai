# Sahi Hai - A Chrome Extension to detect Malicious Websites

![](./images/working.gif)

# Introduction

- [Sahi Hai - A Chrome Extension to detect Malicious Websites](#sahi-hai---a-chrome-extension-to-detect-malicious-websites)
- [Introduction](#introduction)
- [Built With](#built-with)
  - [Advantages](#advantages)
- [Tech Stack](#tech-stack)
- [Usage](#usage)
  - [Directory Stucture](#directory-stucture)
  - [Backend - Ml Model](#backend---ml-model)
  - [Extension](#extension)
- [Acknowledgments](#acknowledgments)

# Built With
## Advantages
# Tech Stack

# Usage

## Directory Stucture

```
.
|-- LICENSE
|-- README.md
|-- extension
|   |-- icon.png
|   |-- manifest.json
|   |-- popup.html
|   |-- popup.js
|   `-- style.css
|-- images
|   `-- working.gif
|-- models
|   |-- mlp_model.pkl
|   `-- random_forest.pkl
|-- requirements.txt
|-- run.sh
|-- test
|   |-- __pycache__
|   |   |-- features_extraction.cpython-39.pyc
|   |   `-- patterns.cpython-39.pyc
|   |-- features_extraction.py
|   |-- features_extraction.pyc
|   |-- index.php
|   |-- markup.txt
|   |-- patterns.py
|   |-- patterns.pyc
|   `-- test.py
`-- train
    |-- data
    |   `-- web_data.arff
    |-- train_mlp.py
    `-- train_rf.py
```

## Backend - Ml Model

1. Clone The Repo
2. Fire Up Terminal and Hit

   ```
   pip install -r requirements.txt 
   ./run.sh
   ```

## Extension

1. Go to chrome Setings using three dots on the top right corner

2. select Extensions.
3. Enable developer mode
4. click on Load Unpacked and select the extensions folder.

# Acknowledgments

A very heartful thanks to the authors and owners of the following articles which propelled us to make Sahi Hai.

- [Malicious URL Detection based on Machine Learning](https://thesai.org/Downloads/Volume11No1/Paper_19-Malicious_URL_Detection_based_on_Machine_Learning.pdf)
- [Detecting malicious URLs using machine learning techniques](https://ieeexplore.ieee.org/document/7850079)
- [Malicious URL Detection using Machine Learning: A Survey](https://arxiv.org/pdf/1701.07179.pdf)
  
And also lots of gratitude for the whole team of "HackNITR 2021" for providing us the perfect platform to showcase our idea.