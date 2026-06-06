# PaveLink_CV
AI-Based Real-Time Road Damage Detection System using CV and DL

# PaveLink – AI-Powered Road Damage Detection System

## Overview

**PaveLink** is a **Computer Vision (CV) and Deep Learning-based road infrastructure monitoring system** designed to automatically detect potholes and road surface defects in real time. The project leverages a custom-trained **YOLOv8 object detection model** to identify road damages from images, videos, and live webcam feeds.

This project falls under the domain of **Computer Vision (CV)**, specifically **Object Detection**, where deep learning models analyze visual data to locate and classify road defects.

Download the model:

https://drive.google.com/file/d/1w5gO2Gqu-JsWD3LA_4hS7KmjKgLO2dgO/view?usp=sharing

Download the dataset:

https://drive.google.com/file/d/1j7AjQVe1sXiLO-BNuaTuUd2t-bBKn6AL/view?usp=sharing

---

## Domain

**Primary Domain:** Computer Vision (CV)

**Sub-Domains:**

* Deep Learning
* Object Detection
* Intelligent Transportation Systems
* Infrastructure Monitoring
* Road Safety Analytics

---

## Problem Statement

Road damages such as potholes and cracks are major contributors to vehicle damage, traffic congestion, and road accidents. Traditional road inspection methods are manual, time-consuming, and costly.

PaveLink addresses this challenge by providing an automated Computer Vision solution capable of detecting road defects accurately and efficiently.

---

## Features

* Real-time pothole detection using webcam feed
* Video-based road damage analysis
* Image-based defect detection
* Custom-trained YOLOv8 model
* Bounding box visualization
* Confidence score prediction
* Fast inference for deployment scenarios
* Scalable for smart city applications

---

## Technology Stack

### Machine Learning & Computer Vision

* YOLOv8
* PyTorch
* OpenCV
* NumPy

### Programming Language

* Python

### Development Environment

* VS Code
* Google Colab

---

## System Architecture

1. Input Source

   * Webcam
   * Image
   * Video

2. Preprocessing

   * Frame acquisition
   * Image resizing

3. Computer Vision Model

   * YOLOv8 Custom Object Detector

4. Detection Engine

   * Pothole localization
   * Confidence estimation

5. Output

   * Bounding boxes
   * Labels
   * Detection confidence scores

---

## Project Structure

```text
PaveLink/
│
├── test.py
├── train.py
├── val.py
├── predict.py
├── requirements.txt
├── README.md
└── y8best.pt
```

---

## Model Information

The project uses a custom-trained YOLOv8 model:

```text
Model Name: y8best.pt
Task: Road Damage Detection
Framework: Ultralytics YOLOv8
Domain: Computer Vision (CV)
```

---

## Installation

Clone the repository:

```bash
git clone <repository-link>
cd PaveLink
```

Install dependencies:

```bash
pip install -r requirements.txt
```

or

```bash
pip install ultralytics opencv-python
```

---

## Model Download

Due to GitHub file size limitations, the trained model weights are hosted on Google Drive.

Download the model:

https://drive.google.com/file/d/1w5gO2Gqu-JsWD3LA_4hS7KmjKgLO2dgO/view?usp=sharing

After downloading:

1. Place `y8best.pt` inside the project root directory.
2. Ensure the file is in the same folder as `test.py`.

Directory example:

```text
PaveLink/
│
├── test.py
├── y8best.pt
```

---

## Running Real-Time Detection

Execute:

```bash
python test.py
```

The system will:

* Open the webcam
* Capture live video frames
* Perform Computer Vision-based pothole detection
* Display bounding boxes and confidence scores

Press:

```text
q
```

to quit the application.

---

## Applications

* Smart Cities
* Road Infrastructure Monitoring
* Municipal Maintenance
* Transportation Analytics
* Automated Road Surveys
* Public Safety Systems

---

## Future Enhancements

* GPS-integrated pothole mapping
* Severity estimation
* Mobile deployment
* Cloud dashboard integration
* Real-time reporting system
* Smart city analytics platform

---

## Key Learning Outcomes

* Computer Vision (CV)
* Deep Learning
* Object Detection
* YOLOv8 Training
* Model Deployment
* OpenCV Integration
* Real-Time Video Analytics

---

## Author

Priyavarshini V
CSE (Artificial Intelligence and Machine Learning)

## Note

**PaveLink is a Computer Vision (CV) project that uses Deep Learning and YOLOv8 Object Detection techniques to identify potholes and road damages from visual data. The project demonstrates practical applications of Computer Vision in transportation safety and infrastructure monitoring.**
