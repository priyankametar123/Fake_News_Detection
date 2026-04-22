# 📰 Fake News Detection

A Machine Learning–powered web application that classifies news articles as **Real** or **Fake** using Natural Language Processing (NLP) and a Logistic Regression model, served via a Flask web interface.

---

## 🚀 Live Demo

Run locally and navigate to `http://127.0.0.1:5000/` after following the setup instructions below.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Model](#model)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 Overview

Misinformation and fake news have become a growing concern in the digital age. This project provides a simple yet effective tool to detect whether a given news article is **real or fake** using a trained Machine Learning model.

The model is trained on the **WELFake Dataset**, a large benchmark dataset combining multiple fake-news corpora. The final application exposes the model through a clean Flask web interface where users can paste any news text and instantly receive a prediction.

---

## ✨ Features

- 🔍 Paste any news article and get an instant Real/Fake prediction
- 🧠 Trained Logistic Regression model with TF-IDF vectorization
- 🌐 Simple and responsive Flask web interface
- ⚡ Fast inference using a pre-trained `.pkl` model
- 📓 Jupyter Notebooks included for full model training pipeline

---

## 🛠️ Tech Stack

| Layer        | Technology                        |
|--------------|-----------------------------------|
| Language     | Python 3.x                        |
| ML Framework | Scikit-learn                      |
| NLP          | TF-IDF Vectorizer (Scikit-learn)  |
| Web Framework| Flask                             |
| Model Format | Joblib (`.pkl`)                   |
| Dataset      | WELFake Dataset (CSV)             |
| Notebooks    | Jupyter Notebook                  |

---

## 📁 Project Structure

```
sem4-project/
│
├── app.py                        # Flask web application (entry point)
├── logistic_model.pkl            # Pre-trained Logistic Regression model (pipeline)
├── WELFake_Dataset.csv           # Dataset used for training
│
├── templates/
│   └── index.html                # Frontend HTML template
│
├── Fake News Detector.ipynb      # Main Jupyter Notebook for model training & evaluation
├── Untitled.ipynb                # Experimental/scratch notebook
│
└── Fake-News-Detection-Machine-Learning-Scam-Detection-NLP/
    ├── Face News Prediction Model.ipynb   # Alternative deep learning model
    ├── Scam Detection.ipynb               # Scam detection experiments
    └── fake_news_model.keras              # Keras-based deep learning model
```

---

## 📊 Dataset

**WELFake Dataset**  
- **Size**: ~72,000 news articles  
- **Labels**: `0` = Fake News, `1` = Real News  
- **Source**: Combines Kaggle, McIntire, Reuters, and BuzzFeed Political datasets  
- **Features used**: Article text (title + body)

> ⚠️ The dataset file (`WELFake_Dataset.csv`) is large (~234 MB). It is included in the repository but may be excluded via `.gitignore` in large deployments.

---

## 🤖 Model

The production model is a **Scikit-learn Pipeline** consisting of:

1. **TF-IDF Vectorizer** — Converts raw text into numerical feature vectors
2. **Logistic Regression Classifier** — Binary classifier (`Real` / `Fake`)

The model is saved as `logistic_model.pkl` using `joblib` and loaded at runtime by the Flask app.

### Performance (on WELFake dataset)
| Metric    | Score  |
|-----------|--------|
| Accuracy  | ~96%+  |
| Precision | ~96%   |
| Recall    | ~96%   |
| F1-Score  | ~96%   |

> See `Fake News Detector.ipynb` for full training code, evaluation metrics, and confusion matrix.

---

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/priyankametar123/Fake_News_Detection.git
   cd Fake_News_Detection
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask scikit-learn joblib pandas numpy
   ```

4. **Run the Flask app**
   ```bash
   python app.py
   ```

5. Open your browser and visit: `http://127.0.0.1:5000/`

---

## 📋 Usage

1. Open the web app in your browser.
2. Paste any news article text into the text area.
3. Click the **"Predict"** button.
4. The result will display whether the article is **Real News** ✅ or **Fake News** ❌.

---

## 🔄 Retraining the Model

To retrain the model from scratch:

1. Open `Fake News Detector.ipynb` in Jupyter Notebook or JupyterLab.
2. Ensure `WELFake_Dataset.csv` is present in the project root.
3. Run all cells — the notebook will preprocess the data, train the model, evaluate it, and save `logistic_model.pkl`.

```bash
jupyter notebook "Fake News Detector.ipynb"
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 👥 Team

Developed as part of **Semester 4 Major Project**.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [WELFake Dataset](https://zenodo.org/record/4561253) by Verma et al.
- [Scikit-learn](https://scikit-learn.org/) for the ML pipeline
- [Flask](https://flask.palletsprojects.com/) for the web framework
