

# Pathway Program Repository for Chisholm HigherEd  
This repository provides the code and tools necessary for students and teachers participating in the pathway program. It includes step-by-step instructions to set up your computer and ensure all code runs smoothly.  

## Getting Started  
Clone this repository to get started. Use the following command to clone the repository:  
```
git clone https://github.com/caseytechschool-cts/pathway-highered.git
```
Alternatively, visit [https://github.com/caseytechschool-cts/pathway-highered.git](https://github.com/caseytechschool-cts/pathway-highered.git), click on the green **Code** button, and select **Download ZIP**. After downloading, unzip the folder to your desired location, such as your desktop.

---

## Prerequisites  

### 1. Download and Install Python 3.8  
- Download Python 3.8 from the [official Python website](https://www.python.org/downloads/).  
- During installation, **check the box "Add Python 3.8 to PATH"**.  
- Note: Some packages used in this program require Python 3.7 or 3.8, which is why this version is specified.  
- If you already have a different version of Python, you can still install Python 3.8 alongside it.  

### 2. Install Virtualenv  
Install `virtualenv` by running the following command in your terminal:  
```
pip install virtualenv
```  
This package allows you to create a virtual environment with a specific Python version.

---

## Setup Instructions  

### Step 1: Create a Virtual Environment  
1. Open your code editor (e.g., VS Code).  
2. From the `File` menu choose `Open Folder` and navigate to the unzip folder from the getting started section.  
3. Open a terminal (`Terminal -> New Terminal`) in your editor and run:  
   ```
   virtualenv -p "C:\Path\to\python.exe" myenv
   ```  
   - Replace `C:\Path\to\python.exe` with the path to your Python 3.8 executable.  
   - Replace `myenv` with your desired virtual environment name.  
   - To find the Python 3.8 path, type the following in your terminal:  
     ```
     where python
     ```  
     Copy the path containing `python38` and replace the placeholder path above.  

### Step 2: Activate the Virtual Environment  
- On Windows:  Type the following in the terminal
  ```
  myenv\Scripts\activate
  ```  
- On macOS/Linux:  
  ```
  source myenv/bin/activate
  ```  

### Step 3: Install Dependencies  
Install all required packages by running:  
```
pip install -r requirements.txt
```  

### Step 4: Install the Dobot Driver  
To communicate with the Dobot Magician, download and install the USB-to-UART bridge driver:  
[Silicon Labs Driver Download](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads)  
- Download the universal Windows driver and follow the installation steps.  

---

## Testing the Setup  

### 1. Connect the Dobot Magician  
- Connect your Dobot Magician to your computer and power it on.  

### 2. Test with Basic Code  
Run the `basic.py` script to verify the arm's functionality. The arm should move if everything is set up correctly.  

### 3. Utility Tool  
To check the arm's position, use the utility tool:  
```
dobot_get_position.exe
```  
> Note: Only one program can connect to the Dobot at a time. Ensure other applications are closed when using this tool.

---

You are now ready to explore and tinker with the Dobot Magician. Happy coding!  

