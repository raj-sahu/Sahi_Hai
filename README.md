# Sahi Hai - A Chrome Extension to detect Malicious Websites
 
![](./images/working.gif)

# Introduction

**Sahi Hai** was made by keeping in the mind the regular internet user who has to go through many websites during his time on the internet and may fall under a trap of a malicious website who might want the user's information or want to introduce malware in their system. Our chrome extension helps the user to check a particular website whether it is safe for browsing or not we have used a pretrained ml model to do so.


- [Sahi Hai - A Chrome Extension to detect Malicious Websites](#sahi-hai---a-chrome-extension-to-detect-malicious-websites)
- [Introduction](#introduction)
- [How it Works ?](#how-it-works-)
  - [What Problem it Solves ?](#what-problem-it-solves-)
- [Tech Stack](#tech-stack)
- [Usage](#usage)
  - [Directory Structure](#directory-structure)
  - [Backend - Ml Model](#backend---ml-model)
  - [Extension](#extension)
- [Acknowledgments](#acknowledgments)

# How it Works ?

![](./images/flow.jpeg)



The ML model extracts the following features from a url :


  
| Feattures     Used                  |                                   |                            |                     |
| ----------------------------------- | --------------------------------- | -------------------------- | ------------------- |
| Having IP address                   | URL Length                        | URL Shortening service     | Having @ symbol     |
| Having double slash                 | Having dash symbol(Prefix Suffix) | Having multiple subdomains | SSL Final State     |  | Domain Registration Length | Favicon | HTTP or HTTPS token in domain name | Request URL |
| URL of Anchor                       | Links in tags                     | SFH - Server from Handler. | Submitting to email |
| Abnormal URL                        | IFrame                            | Age of Domain              | DNS Record          |
| Web Traffic -  using data.alexa.com | Google Index                      |                            | Statistical Reports |
 
 
 
  We have iterated multiple times during training phase :
  
  <!-- 1. Random Forest Model ( 93.14% Accuracy )
  1. MLP Model ( 94.17% Accuracy ) -->
  ![](./images/results.png)

<br/>

## What Problem it Solves ?

 Every other website in today's day and age on the internet wants to collect data of its users by tricking them into giving away their credentials for fraud or many such vindictive acts. Naive users using a browser have no idea about the backend of the page. The users might be tricked into giving away their credentials or downloading malicious data.

We have created an extension for Chrome that will act as middleware between the users and the malicious websites and relieve users of giving away to such websites.
Our project was made by keeping in the mind the regular internet user who has to go through many websites during his time on the internet and may fall under a trap of a malicious website who might want the user's information or want to introduce malware in their system. Our chrome extension helps the user to check a particular website whether it is safe for browsing or not

# Tech Stack

- [HTML](https://www.w3schools.com/html/) - The front-end development language used for creating extension.

- [CSS](https://www.w3schools.com/css/) - The  front-end development language used for creating extension.

- [Python](https://www.python.org/) - The Programing Language used to parse features from a website and for training/testing of the ML model.
- [JavaScript](https://www.javascript.com/) - The scripting language used for creating the extension and sending  requests to the served Ml model.
- [Php](https://www.php.net/) - The scripting language used for serving the Ml model .

- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) - The library used to scrape websites from a url.
- [Googlesearch](https://pypi.org/project/googlesearch-python/) - The library for  performing google search's during feature extraction.

- [whois](https://pypi.org/project/whois/) - The package for retrieving WHOIS information of domains during feature extraction.
- [scikit-learn](https://scikit-learn.org/stable/) -
  The library used for training ML models.
<br/>

# Usage

## Directory Structure

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

1. Go to chrome Settings using three dots on the top right corner

2. select Extensions.
3. Enable developer mode
4. click on Load Unpacked and select the extensions folder.
</br>

# Acknowledgments

A very heartful thanks to the authors and owners of the following articles which propelled us to make Sahi Hai.

- [Malicious URL Detection based on Machine Learning](https://thesai.org/Downloads/Volume11No1/Paper_19-Malicious_URL_Detection_based_on_Machine_Learning.pdf)
- [Detecting malicious URLs using machine learning techniques](https://ieeexplore.ieee.org/document/7850079)
- [Malicious URL Detection using Machine Learning: A Survey](https://arxiv.org/pdf/1701.07179.pdf)
  
And also lots of gratitude for the whole team of "HackNITR 2021" for providing us the perfect platform to showcase our idea.
