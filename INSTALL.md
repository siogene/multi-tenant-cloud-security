# 📦 Installation Guide

This document explains how to set up and run the Multi-Tenant Cloud Security Framework locally.

## 🛠️ Prerequisites
- Git
- Docker & Docker Compose
- Python 3.x with pip
- Git Bash or Unix Shell
- (Optional) KVM + Open vSwitch for tenant simulation

## 🚀 Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/multi-tenant-cloud-security.git
cd multi-tenant-cloud-security
```

2. **Start the Dashboard**
```bash
cd dashboard
docker-compose up -d
```

3. **Run Access Control Engine**
```bash
python access_control/abac_engine.py
```

4. **Train the IDS ML Model**
```bash
python ids/train_model.py
```

5. **View Dashboard**
- Open: http://localhost:5601 (Kibana)
- Optional: http://localhost:3000 (Grafana)
