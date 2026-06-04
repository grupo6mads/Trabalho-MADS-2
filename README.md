# 🍽️ Restaurant Management System

Sistema completo de gestão de restaurantes em tempo real, desenvolvido em Python + Flask, com integração direta ao Google Sheets como base de dados.

---

## 🚀 Funcionalidades

- Dashboard com níveis de acesso
- Gestão de restaurantes, clientes, menus e pedidos
- Analytics em tempo real
- Mapa interativo com Folium
- Verificação de integridade de dados
- Integração com Google Sheets

---

## 🧠 Tecnologias

- Python 3.12+
- Flask
- gspread
- Google Sheets API
- Folium
- Render

---

## 📂 Estrutura

restaurant-management/
│
├── app.py
├── config.py
├── sheets_service.py
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── services/
│   ├── restaurant_service.py
│   ├── client_service.py
│   ├── menu_service.py
│   ├── order_service.py
│   ├── map_service.py
│   ├── analytics_service.py
│   ├── integrity.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── restaurantes.html
│   ├── clientes.html
│   ├── menus.html
│   ├── pedidos.html
│   ├── analytics.html
│   ├── mapa.html
│   ├── integrity.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── charts/
│
├── utils/
│   ├── auth.py
│   ├── rating.py
│   ├── validators.py
│   └── integrity_checks.py
└── 
---

## ⚙️ Instalação

git clone <repo_url>
cd restaurant-management
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

---

## 🔑 Acessos

- Key_Restaurantes
- Key_Clientes
- Key_Admin
- Key_Integrity

---

## ⚠️ Nota

Projeto académico com integração em tempo real com Google Sheets.
