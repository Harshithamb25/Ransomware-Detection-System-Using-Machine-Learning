This system leverages machine learning to identify ransomware by constantly analyzing real-time file operations and classifying activity using a Random Forest model. The project spans dataset creation, automated model training, continuous directory monitoring, alert logging, and instant email notification of suspicious events.

Main Features
Generates mock ransomware and regular activity data

Trains an ML classifier (Random Forest)

Monitors folders in real time

Detects abnormal, potentially malicious changes

Logs security alerts

Notifies admins with automated email alerts

Modular Python-based scripts for ease of adaptation

Technology Stack
Python, Pandas, NumPy, Scikit-learn, Joblib

SMTP for notifications

JavaScript for demonstration interface

Usage Steps
Clone the repository and install dependencies

Generate synthetic data and train the model

Configure the monitoring path and email settings

Launch monitoring to start detecting threats

Detection Workflow
The monitoring script collects system stats like file modification times, count of changes, CPU, and disk activity. These are used by the trained model to distinguish between normal and ransomware actions. Alerts and notification emails trigger if ransomware-like activity is detected.

Intended Purpose
Educational project using simulated ransomware behavior, meant for learning and demonstration—not production use.

Extensible Goals
Integrate OS-level resource monitoring

Add a web dashboard and real-time analytics

Introduce deep-learning detection methods

Expand notifications and platform support.
