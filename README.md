# Project Title

## Overview
This repository contains a Python application for tracking machine learning models using MLflow. The application allows users to manage model versions, retrieve metrics, and facilitate the deployment of models.

## Features
- Track multiple versions of machine learning models.
- Retrieve detailed metrics for each model version.
- Easy integration with MLflow for model management.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/wakoTheDev/Scalable-ML-Pipelines-with-Model-Registries-and-FeatureStores-MLOPs.git
   cd Scalable-ML-Pipelines-with-Model-Registries-and-FeatureStores-MLOPs
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the MLflow server:**
   ```bash
   mlflow ui
   ```
   This will start the MLflow tracking UI at `http://localhost:5000`.

2. **Run the application in the following order:**
   - First, run the `feature_services` module to prepare your features:
     ```bash
     python feature_store/feature_services.py
     ```
   - Next, execute the `training_pipeline` to train your model:
     ```bash
     python training_pipeline/training_pipeline.py
     ```
   - Finally, run the `main.py` script to start the application:
     ```bash
     python main.py
     ```

3. **Interacting with the ModelTracker class:**
   You can create an instance of the `ModelTracker` class and call its methods to retrieve model versions and metrics:
   ```python
   from model_registry.model_tracker import ModelTracker

   tracker = ModelTracker()
   model_versions = tracker.get_model_versions("your_model_name")
   print(model_versions)
   ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

