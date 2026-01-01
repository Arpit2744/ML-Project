# 🚀 Student Performance Indicator (End-to-End ML Pipeline)

A complete Machine Learning project that predicts student performance based on various parameters. This repository demonstrates the full lifecycle of an ML application, from data analysis to cloud deployment using Docker and CI/CD pipelines.

## 🛠️ Tech Stack
* **Language:** Python (3.8+)
* **Framework:** FastApi (Backend) / Scikit-Learn (ML)
* **Containerization:** Docker
* **Cloud Provider:** AWS (EC2, ECR)
* **CI/CD:** GitHub Actions (Self-Hosted Runner)

## 📂 Project Structure
```text
├── artifacts/          # Generated models (model.pkl) & datasets (train/test.csv)
├── logs/               # Application execution logs
├── notebook/           # Jupyter notebooks for EDA & model training
├── src/                # Core application source code
│   ├── components/     # Data ingestion, transformation, & training modules
│   ├── pipeline/       # Training & Prediction pipelines
│   ├── logger.py       # Custom logging setup
│   └── exception.py    # Custom exception handling
├── static/             # CSS and styling files
├── templates/          # HTML templates for the UI
├── app.py              # Application entry point (FastAPI)
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
└── setup.py            # Project packaging setup

## 📊 Features
* **Data Ingestion & Transformation:** Automated pipelines to handle data processing.
* **Model Training & Prediction pipeline:** Regression models trained to predict student scores.
* **Web Interface:** Web UI for user inputs (built with FastAPI/Jinja2).
* **Automated Deployment:** Fully automated CI/CD pipeline triggering on every push.

## ⚙️ How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/Arpit2744/ML-Project.git](https://github.com/Arpit2744/ML-Project.git)
cd ML-Project

```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run the App

```bash
python app.py

```

*Open `http://127.0.0.1:8000` in your browser.*

---

## 🐳 Docker Support

Build and run the container locally to ensure consistency.

```bash
docker build -t student-performance .
docker run -p 8000:8000 student-performance

```

---

## ☁️ Deployment Pipeline (CI/CD)

This project uses **GitHub Actions** to automate deployment to **AWS EC2**.

### Workflow Steps:

1. **Integration:** Code is linted and tested.
2. **Delivery:** Docker image is built and pushed to **AWS ECR (Elastic Container Registry)**.
3. **Deployment:** A **Self-Hosted Runner** on an AWS EC2 instance pulls the latest image and updates the running container.

### 🚧 Challenges & Learnings

Building this wasn't just about coding; it was about engineering. Here are the real-world issues I solved:

* **EC2 Disk Space:** The 1.6GB Docker image crashed the `t2.micro` instance. I learned to resize AWS EBS volumes and expand Linux partitions on the fly.
* **Git Divergence:** Solved `non-fast-forward` merge conflicts when syncing local code with remote repo changes.
* **Docker Zombie Containers:** Automated the cleanup of old containers in the CI/CD pipeline to prevent name conflicts during re-deployment.
* **Missing Artifacts:** Debugged `FileNotFoundError` caused by `.gitignore` excluding the trained model file (`model.pkl`) from the build.

---

## 📜 License

This project is open-source and available under the MIT License.