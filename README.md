# Flask EC2 Web App 🚀

A modern Flask web application deployed on **AWS EC2**, demonstrating cloud deployment, automation, and integration with AI features as part of my **Cloud Engineering + AI** learning journey.

---

## Features ✨
- **Modern responsive UI** across all pages: Home, About, Contact, AI Sentiment Analysis.
- **AI-powered sentiment analysis** using Hugging Face Transformers (`/ai` route).
- **Cloud-ready deployment**: Hosted on AWS EC2 with Nginx reverse proxy.
- **SSL-secured**: HTTPS with Cloudflare-managed domain and Let's Encrypt certificates.
- **CI/CD automation** via GitHub Actions for seamless updates.
- Fully prepared for **cloud-native applications** and scaling.

---

## Tech Stack 🛠️
- **Backend:** Python 3.9, Flask 3.x, Gunicorn  
- **Frontend:** Bootstrap 5, Jinja2 templates  
- **AI / Machine Learning:** Hugging Face Transformers (Sentiment Analysis)  
- **Server:** AWS EC2 (Amazon Linux 2023)  
- **Web Server:** Nginx (reverse proxy)  
- **DevOps:** Git, GitHub, GitHub Actions  
- **Domain & SSL:** Cloudflare, Let’s Encrypt  

---

## Live Demo 🌍
- **Home:** [https://alishehryar.com/](https://alishehryar.com/)  
- **About:** [https://alishehryar.com/about](https://alishehryar.com/about)  
- **Contact:** [https://alishehryar.com/contact](https://alishehryar.com/contact)  
- **AI Sentiment Analysis:** [https://alishehryar.com/ai](https://alishehryar.com/ai)  

---

## Project Structure 📂
flask-ec2-app/
├── app.py # Main Flask application
├── templates/ # HTML templates
│ ├── base.html
│ ├── index.html
│ ├── ai.html
│ ├── about.html
│ └── contact.html
├── static/ # CSS, JS, and images
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .github/workflows/
└── deploy.yml # GitHub Actions deployment workflow

---

## Deployment Progress 🔄
- ✅ Domain & SSL setup (Cloudflare + Let’s Encrypt)
- ✅ Nginx configured as reverse proxy
- ✅ Gunicorn + systemd service for background deployment
- ✅ GitHub Actions + EC2 deployment automated
- ✅ Tested automation by updating README.md (2025-09-12)
- ✅ Next step: continuous updates & advanced CI/CD improvements

---

Contact 📬

Ali Shehryar

GitHub: alishehryar1

Email: alishehryar11@gmail.com

LinkedIn: iamalishehryar

⭐ If you like this project, give it a star on GitHub!