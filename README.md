# Pathway Program Repository for Chisholm HigherEd

## Overview
This repository contains the necessary code and tools for students and teachers participating in the Pathway program, focusing on Dobot Magician robotics integration. The guide provides comprehensive setup instructions and troubleshooting steps.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup Instructions](#setup-instructions)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

## Prerequisites

### Required Hardware
- Dobot Magician robotic arm kit
- Conveyor belt
- Different sensors (e.g., distance and colour sensor)

### Required Software
- Python 3.8 (Required for package compatibility)
- Git (optional)
- [Visual Studio Code](https://code.visualstudio.com/) (recommended) or [Windsurf by Codeium](https://codeium.com/windsurf) (optional)

## Installation

### Getting the Code
Clone this repository using Git:
```bash
git clone https://github.com/caseytechschool-cts/pathway-highered.git
```
Or download as ZIP:
1. Visit the repository: https://github.com/caseytechschool-cts/pathway-highered
2. Click the green **Code** button above
3. Select **Download ZIP**
4. Extract to your preferred location

### Python Setup
1. Download Python 3.8 from the [official Python website](https://www.python.org/downloads/release/python-380/)
2. During installation:
   - Check **"Add Python 3.8 to PATH"**

Open the cloned or the downloaded folder in your prefered IDE to complete the installation process.
### Virtual Environment Setup
1. Install virtualenv:
```bash
pip install virtualenv
```

2. Create a virtual environment:
```bash
# Windows
virtualenv -p "C:\Users\{Username}\AppData\Local\Programs\Python\Python38\python.exe" venv

Replace {Username} with your Windows username if you have installed at the default location
```
3. If you do not know where is your Python 3.8 installation, run the following command on the command line 
```bash
where python
```

3. Activate the environment:
```bash
# Windows
venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Dobot Setup

### Driver Installation
1. Download and install the [Silicon Labs CP210x USB-to-UART Bridge Driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads)
2. Install the appropriate version for your OS
3. Restart your computer after installation

### Hardware Connection
1. Connect the Dobot Magician to power
2. Connect the USB cable to your computer
3. Wait for Windows to recognize the device (~30 seconds)
4. Verify connection in Device Manager under "Ports (COM & LPT)"

## Testing

### Basic Functionality Test
1. Ensure the virtual environment is activated
2. Run the basic test script:
```bash
python basic.py
```
Expected behavior: The Dobot arm should perform a simple movement sequence

### Position Utility
Check the arm's current position:
```bash
dobot_get_position.exe
```
> Important: Only one program can connect to the Dobot at a time

## Troubleshooting

### Common Issues
1. **COM Port Not Found**
   - Check USB connection
   - Verify driver installation in Device Manager
   - Try a different USB port

2. **Python Import Errors**
   - Confirm virtual environment is activated
   - Reinstall requirements: `pip install -r requirements.txt`

3. **Dobot Connection Error**
   - Close all other programs using the Dobot
   - Reset the Dobot power
   - Check if correct COM port is selected

### Getting Help
- Create an issue on GitHub
- Contact technical support: support@chisholm.edu.au
- Check the [Dobot Documentation](https://www.dobot.cc/downloadcenter.html)

## Additional Resources
- [Dobot Magician User Manual](https://www.dobot.cc/downloadcenter/dobot-magician.html)
- [Python Documentation](https://docs.python.org/3.8/)
- [Video Tutorials](https://www.youtube.com/c/DobotRobot)

---

## Version Information
- Last Updated: December 2024
- Python Version: 3.8
- Tested on Windows 11
