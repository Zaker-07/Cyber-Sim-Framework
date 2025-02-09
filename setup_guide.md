# CyberSim Framework - Setup Guide

## Prerequisites
- Kali Linux VM (host)
- Docker installed
- Python 3.8+ installed
- Git installed

## Setup Instructions

### Step 1: Clone the Repository
bash:
git clone https://github.com/yourusername/CyberSim-Framework.git
cd CyberSim-Framework
Step 2: Install Dependencies
bash:
pip3 install -r requirements.txt
Step 3: Build Docker Environment
bash:
docker-compose up -d
Step 4: Start Monitoring
bash:
python3 monitor_snort.py
Step 5: Launch Dashboard
bash:
python3 dashboard.py
