
# Blinky Blanket

A computer vision–based smart blanket that uses **AI detection** and **camera-based monitoring** to automatically adjust its position, reducing infants’ suffocation risk without external intervention.


##  Overview

Blinky Blanket is an intelligent safety system designed to monitor sleeping infants and **automatically reposition the blanket** to ensure safe breathing conditions.  
It combines AI, computer vision, and robotics to detect unsafe situations (like a blanket covering the baby’s face) and trigger a motorized adjustment mechanism — helping parents ensure their baby’s safety even while asleep.


##  Features

- Real-time **AI object detection** using the YOLO (You Only Look Once) model  
- **Camera-based monitoring** for infant position and blanket movement  
- **Automatic repositioning** using motor control and embedded sensors  
- **Non-invasive system** — no need for wearable devices on the infant  
- Built with **C++**, **Arduino**, **Python**, **OpenCV**, and **TensorFlow**


## Tech Stack

| Category | Technologies |
|-----------|--------------|
| **Programming Languages** | C++, Python |
| **AI / CV Libraries** | YOLO, OpenCV, TensorFlow |
| **Embedded Systems** | ESP32 |
| **Hardware Components** | Motors, Camera module, Microcontroller (ESP32), Power supply, Motor Drivers |


##  How It Works

1. **Camera Feed** → The camera captures the infant’s sleeping environment in real time.  
2. **YOLO Model** → Detects blanket position and possible obstruction of the infant’s airway.  
3. **Signal to Arduino** → If a risk is detected, a control signal is sent to adjust the blanket’s position.  
4. **Motorized Adjustment** → The system moves the blanket away automatically, restoring a safe environment.  
5. **Alert System** → A buzzer or mobile notification can alert parents.

##  Setup & Usage

### Prerequisites
- Python ≥ 3.8  
- Arduino IDE installed  
- OpenCV and TensorFlow libraries  
- YOLOv11 weights file (`yolov11s.pt` or custom trained model)


