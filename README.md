## ESG Rating Classification - README
Project Overview
This repository contains the code and resources for a machine learning project focused on predicting Environmental, Social, and Governance (ESG) ratings for companies. ESG ratings are scores used to evaluate how well a company performs in areas related to environmental sustainability, social responsibility, and corporate governance. These ratings are increasingly important for investors, regulators, and stakeholders who are interested in responsible investing and corporate transparency.

Our primary objective is to develop and evaluate a model that can predict the ESG ratings of companies based on various features and data points related to their operations, practices, and disclosures.

## Project Objectives
Predict ESG Ratings: The main goal of this project is to predict the ESG ratings of companies using machine learning models. We aim to accurately estimate these ratings based on a set of input features that describe the company's performance across different dimensions.

Model Explainability: We conducted a detailed study to assess the explainability of our model using SHAP (SHapley Additive exPlanations) values. Understanding the factors that contribute to the model's predictions is crucial for ensuring transparency and trustworthiness in our predictions, especially in the context of ESG ratings.

## ESG Scores Explained
ESG scores are a set of metrics that evaluate a company’s performance in three key areas:

Environmental (E): This dimension assesses how a company impacts the environment. Key factors include carbon emissions, energy efficiency, waste management, and water usage.

Social (S): This dimension evaluates a company’s relationship with its employees, suppliers, customers, and communities. It includes factors such as labor practices, human rights, product safety, and community engagement.

Governance (G): This dimension examines how a company is governed, focusing on leadership, executive pay, audits, internal controls, and shareholder rights.

Each company receives a score in these three areas, which are often combined into an overall ESG rating.

Repository Structure
data/: Contains the dataset used for training and testing the model.
notebooks/: Jupyter notebooks used for data exploration, model training, and evaluation.
models/: Saved models and any relevant model artifacts.
src/: Source code for data processing, feature engineering, and model training.
shap_explainability/: Scripts and notebooks related to the SHAP analysis for model explainability.
README.md: This file, providing an overview of the project.
Getting Started
Prerequisites
Python 3.8+
Required Python packages are listed in requirements.txt.
