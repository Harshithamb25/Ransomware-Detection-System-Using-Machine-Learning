import os
import time
import joblib
import pandas as pd
import numpy as np
import smtplib
from email.mime.text import MIMEText

# Load the trained model
model = joblib.load("ransomware_model.pkl")
folder_to_monitor = "C:/Users/Harshitha/OneDrive/Desktop/MBH/ransomware/ransomware detection/test_folder"



# Email setup
EMAIL_SENDER = "thrisharadharishnan@gmail.com"
EMAIL_PASSWORD = "Thrisha07@#$"
EMAIL_RECEIVER = "thidhikshar@gmail.com"

# Function to send email alert
def send_email_alert(file_path):
    subject = "⚠️ Ransomware Detected!"
    body = f"ALERT! Ransomware activity detected on: {file_path}"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print(f"📧 Email alert sent to {EMAIL_RECEIVER}")
    except Exception as e:
        print(f"❌ Email alert failed: {e}")

# Function to log ransomware activity
def log_alert(file_path):
    with open("alerts.log", "a") as log_file:
        log_file.write(f"ALERT! Ransomware detected in {file_path}\n")

# Function to predict if activity is ransomware or normal
def predict_activity(time_to_modify, num_files_modified, cpu_usage, disk_usage):
    feature_names = ["time_to_modify", "num_files_modified", "cpu_usage", "disk_usage"]
    features = pd.DataFrame([[time_to_modify, num_files_modified, cpu_usage, disk_usage]], columns=feature_names)
    
    prediction = model.predict(features)
    return "Ransomware" if prediction[0] == 1 else "Normal"

# Function to monitor the folder
def monitor_folder():
    print(f"Monitoring folder: {folder_to_monitor}")
    previous_files = set(os.listdir(folder_to_monitor))

    while True:
        time.sleep(5)
        current_files = set(os.listdir(folder_to_monitor))
        new_files = current_files - previous_files  # Detect newly added files

        for filename in new_files:
            if filename.endswith(".txt"):  
                file_path = os.path.join(folder_to_monitor, filename)
                print(f"New file detected: {file_path}")

                # Simulate metadata
                time_to_modify = np.random.normal(10, 2)
                num_files_modified = np.random.randint(1, 10)
                cpu_usage = np.random.randint(40, 95)
                disk_usage = np.random.randint(30, 90)

                # Predict ransomware activity
                result = predict_activity(time_to_modify, num_files_modified, cpu_usage, disk_usage)
                
                if result == "Ransomware":
                    print(f"🚨 ALERT: Ransomware activity detected for {filename}!")
                    log_alert(file_path)  # Log alert
                    send_email_alert(file_path)  # Send email alert

        previous_files = current_files  

# Start monitoring
monitor_folder()
