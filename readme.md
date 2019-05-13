## Predicting Song Hotness

![alt text](http://www.fumcwl.org/files/69/Pictures/music.jpg)
## Introduction

### Motivation and Background

The recorded music industry has been flourishing over the past ten years. It has generated a revenue of 9.8 billion U.S. dollars in 2018 alone, and experts anticipate that this trend will continue [1]. Predicting a song’s popularity has been drawing a broad range of interest not only from singers and record producers, but also from investors and machine learning researchers.

### Project Goal
In this project, we will try to look into a range of song attributes from the Million Song Dataset [2], and extract key characteristics that determine a song’s hotness. Based on these key characteristics, we will build several machine learning models to predict a new song’s hotness. Finally, we will evaluate these models and benchmark them with regards to the baseline model.

Overall, our goal is to propose an end-to-end data pipeline, which includes data preprocessing, machine learning modeling, to accurately predict the hotness of a song.

### Project Question
In order to achieve the project goal above, we need to answer this question: what are the key characteristics of a song and how do they determine the song’s hotness? To be more specific, we need to know:

● What is the definition of the hotness of a song? Can we replace the song’s hotness attribute with other data given that this attribute is missing in near half of the songs?

● What are the most important attributes in determining a song’s hotness?

● Are there any new features that we can add to the existing dataset to improve the prediction accuracy?

For the **rest of this report, we will address these questions individually**. To facilitate reading, we have provided a roadmap that we are going to follow for the rest of the report.

![alt text](https://github.com/Yuting-Kou/AC209B_MillionSong/blob/master/src/Zheyu%20Wu/WechatIMG244.png?raw=true)


The folder version is as follows:

    
    ├── AC209B_MillionSong 
        ├── data           <- the folder contains all the data
        │   ├── music.csv
        ├── src           <- the folder contains all the script
