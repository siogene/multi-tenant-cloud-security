# 🔐 Multi-Tenant Cloud Security Framework

This project is a modular, layered security framework designed to secure multi-tenant cloud environments. It integrates advanced access control, encryption, intrusion detection (signature + ML), and real-time visualization using open-source tools.

---

## 🌐 Project Goals

- ✅ Strong tenant isolation (VLAN + VM segmentation)
- ✅ Fine-grained access control (RBAC, ABAC, XACML)
- ✅ Tokenization & TLS encryption for sensitive data
- ✅ Hybrid Intrusion Detection System (Snort + Isolation Forest)
- ✅ Centralized, real-time dashboard using ELK + Grafana
- ✅ Evaluation framework for performance and compliance (ISO/NIST)

---

## 📁 Project Structure

```
multi-tenant-cloud-security/
├── access_control/     # RBAC, ABAC, XACML logic
├── dashboard/          # Dockerized ELK + Grafana
├── docs/               # Architecture diagrams, instructions
├── encryption/         # Tokenization scripts, TLS setup
├── evaluation/         # Performance metrics, attack logs
├── ids/                # Snort rules + ML (Isolation Forest)
├── segregation/        # KVM + VLAN provisioning
├── scripts/            # Auto-setup, IDS trainer, deployment
```

---

## ⚙️ Key Technologies

- **Python** (Flask, Scikit-learn)
- **Snort 3** (signature-based IDS)
- **Isolation Forest** (ML-based anomaly detection)
- **WSO2 Balana** (XACML PDP)
- **Open vSwitch + KVM** (network isolation)
- **ELK Stack** (Elasticsearch, Logstash, Kibana)
- **Grafana** (visual dashboards)

---

## 🚀 Getting Started

### 🔧 Prerequisites
- Docker & Docker Compose
- Python 3.x + pip
- Git
- Git Bash (for Windows users)
- KVM + Open vSwitch (for tenant simulation)

### 🔨 Setup Steps

1. Clone the repo:
   ```bash
   git clone https://github.com/siogene/multi-tenant-cloud-security.git
   cd multi-tenant-cloud-security
   ```

2. Start the dashboard:
   ```bash
   cd dashboard
   docker-compose up -d
   ```

3. Run the ABAC engine:
   ```bash
   python access_control/abac_engine.py
   ```

4. Train the ML-IDS:
   ```bash
   python ids/train_model.py
   ```

---

## 📊 Dashboard

Kibana: [http://localhost:5601](http://localhost:5601)  
Grafana (if configured): [http://localhost:3000](http://localhost:3000)

Includes:

- IDS Alert heatmaps
- Access decision logs
- Resource usage by tenant
- Tokenization/decryption audit logs

---

## 🧪 Evaluation Metrics

| Feature       | Precision | Recall | F1-Score |
|---------------|-----------|--------|----------|
| Snort         | 91%       | 84%    | 87.3%    |
| IsolationForest | 88%     | 89%    | 88.5%    |
| Hybrid IDS    | 95%       | 93%    | 94.1%    |

---

## 📜 License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

## ✍️ Author

Saugat — as part of a research dissertation on securing multi-tenant cloud environments.

---

## 🌐 Contributions

Pull requests are welcome! Please open an issue first to discuss major changes.

---

## ✅ Project Status: **Complete & Ready for Extension**
