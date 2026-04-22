# 🚀 OrderFix — WhatsApp AI Order Manager

AI agent that automates WhatsApp order processing into structured data and workflows.

---

## 💡 Problem
Small businesses receive orders via WhatsApp in messy, unstructured text.  
This leads to manual effort, errors, and delays.

---

## 🤖 Solution
OrderFix uses AI to read messages, extract order details, and convert them into structured data that can be used for operations.

---

## ⚙️ Features
- Extract items, quantity, and delivery details from messages
- Convert text into structured JSON
- Ready for integration with Google Sheets / CRM
- Can generate automated replies

---

🏗️ Tech Stack
Python
FastAPI
LLM APIs (OpenAI / Claude)

---

📦 Project Structure
orderfix-ai/
├── app/
├── docs/
├── .env.example
├── requirements.txt
└── README.md

---

💼 Use Case
Cloud kitchens
Home food businesses
Small retailers using WhatsApp orders
🚧 Note

This repository showcases the system design and capabilities.
Full production implementation is private.

---

📫 Contact

Charu@Stratschool.org

---

## 🧪 Demo

### Input
"I need 2 chicken biryani and 1 coke, deliver by 8pm"

### Output
```json
{
  "items": [
    {"name": "chicken biryani", "qty": 2},
    {"name": "coke", "qty": 1}
  ],
  "delivery_time": "8pm"
}



