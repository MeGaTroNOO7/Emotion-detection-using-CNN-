# Emotion Detection Using CNN

## Overview

This project implements a Convolutional Neural Network (CNN) model for emotion recognition using the FER2013 dataset. The CNN model classifies facial expressions into seven emotions: angry, disgusted, fearful, happy, neutral, sad, and surprised. The project offers two main functionalities: training the model and performing real-time emotion detection through a webcam feed.

## Prerequisites

- Python 3.x
- Required libraries:
  - `numpy` version 1.22.0
  - `opencv-python` version 4.2.0.32
  - `tensorflow` version 2.9.3

## Installation

1. **Clone the Repository**:
   ~~~
   git clone https://github.com/your/repository.git
   ~~~

2. **Install Dependencies**:
   ~~~
   pip install numpy==1.22.0 opencv-python==4.2.0.32 tensorflow==2.9.3
   ~~~

   OR
   ~~~
   pip install -r requirements.txt
   ~~~

## Usage

### Running the Script

1. **Train the Model**:
   ~~~
   python script.py --mode train
   ~~~
   This command trains the CNN model using the FER2013 dataset.

2. **Perform Real-time Emotion Detection**:
   ~~~
   python script.py --mode display
   ~~~
   This command loads the trained model and performs real-time emotion detection on faces captured through a webcam feed.

### Script Arguments

- `--mode`: Specifies the mode of operation (`train` for training the model, `display` for real-time emotion detection).

## Folder Structure

Upon running the script, the following folder structure is created:

```
data/
│
├── train/
│   ├── angry/
│   ├── disgusted/
│   ├── fearful/
│   ├── happy/
│   ├── sad/
│   ├── surprised/
│   └── neutral/
│
└── test/
    ├── angry/
    ├── disgusted/
    ├── fearful/
    ├── happy/
    ├── sad/
    ├── surprised/
    └── neutral/
```

## Model Architecture

The CNN model architecture consists of several convolutional and pooling layers, followed by fully connected layers with dropout for regularization.

## Authors

- [Bernard George Charles](https://github.com/MeGaTroNOO7)


