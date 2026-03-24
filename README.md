# 5G Core Network Honeypot & TCP Tarpit 🍯🕸️

## 📌 Project Overview
A specialized security tool designed for **Active Defense and Deception** in telecommunications infrastructure. This project simulates a vulnerable 5G Core Router interface to lure attackers, harvest threat intelligence, and neutralize threats using a **TCP Tarpit** mechanism.

## 🛡️ Key Features
- **Deception Engineering:** Presents a realistic, fake "Vodafone 5G Core Router" banner to attract unauthorized access attempts.
- **Threat Intelligence:** Captures and logs the specific credentials/passwords used by attackers for dictionary attack analysis.
- **TCP Tarpit (The Trap):** Instead of dropping connections, the system holds the TCP session open indefinitely, sending 1-byte packets to freeze the attacker's automated scanning tools and waste their resources.
- **Dockerized:** Fully containerized for easy deployment as a security microservice.

## 🚀 How to Run

### Using Python
1. Ensure Python 3.x is installed.
2. Run the honeypot:
   ```bash
   python3 tarpit.py
Test the connection (as an attacker):

Bash
nc localhost 2222
Using Docker
Bash
docker build -t 5g-honeypot .
docker run -p 2222:2222 5g-honeypot
🧠 Technical Concepts Applied
Socket Programming: Utilizing Python's socket API for low-level TCP communication.

Exception Handling: Robust management of connection drops and network errors.

Resource Management: Safe handling of client connections and session timeouts.

DevSecOps: Integrating security logic directly into the infrastructure layer.

📂 Project Structure
tarpit.py: The core logic for the honeypot and tarpit loop.

Dockerfile: Container configuration for isolated deployment.

README.md: Project documentation.