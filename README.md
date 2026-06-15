# Hackathon E‑Commerce Conversion Prediction

## Overview
This repository contains the code and data for a hackathon project that predicts whether a user will convert (make a purchase) on an e‑commerce website. The goal is to build a straightforward, easy‑to‑understand model that can be trained and evaluated quickly.

## Project Structure
- `train.csv` – Training data with features and the target label `converted`.
- `public_test.csv` – Test data for public evaluation.
- `private_test.csv` – Test data for private evaluation (used for final scoring).
- `sample_submission.csv` – Example submission file format.
- `submission.csv` – Your final predictions ready for upload.
- `methodology_report.docx` – A plain‑English report describing the approach (generated separately).

## How to Run
1. **Install dependencies** (e.g., `pandas`, `scikit‑learn`):
   ```bash
   pip install -r requirements.txt
   ```
   *(If a `requirements.txt` is not present, install the packages you need manually.)*
2. **Train the model** – Open the notebook `SA2026_Starter_Notebook.ipynb` (or `notebook.ipynb`) and run the cells to train and evaluate the model.
3. **Generate predictions** – After training, the notebook will create `submission.csv` in the required format.

## License
This project is provided for educational and hackathon purposes. Feel free to adapt the code for your own experiments.
