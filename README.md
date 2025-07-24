# Data-Driven Crop Advisory System

This project provides a web-based Crop Advisory System that leverages a machine learning model to recommend crops and provide essential fertilizer advice based on soil and environmental parameters. It's specifically designed with small farm holders in mind.

## Features

* **Crop Recommendation:** Predicts the most suitable crop based on input soil (N, P, K, pH) and environmental (Temperature, Humidity, Rainfall) parameters.
* **Detailed Soil Analysis Display:** Shows the input soil parameters in a clear format.
* **Simplified Fertilizer Advisory:** Offers concise and actionable advice tailored for small farm holders, including:
    * Key principles of nutrient management.
    * NPK recommendations (dynamically adjusted).
    * Soil pH guidance.
    * Application timeline for selected crops (e.g., Rice).
    * Important guidelines for application best practices.
    * Special considerations for small farm management.
* **User-Friendly Interface:** An aesthetically pleasing and responsive web form.
* **Backend:** Flask API for model inference and data structuring.

## How to Set Up and Run

### Prerequisites

* Python 3.x installed
* `pip` (Python package installer)

### Installation

1.  **Clone the Repository:**
    If you are setting this up on a new machine, first clone the repository:
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
    cd YOUR_REPO_NAME # Replace with your actual repository name
    ```
    (If you are already in your `D:\Python` project folder, you can skip this `git clone` step.)

2.  **Install Python Dependencies:**
    Navigate to your project's root directory (`D:\Python` in your case) in your terminal/Git Bash and install the required libraries:
    ```bash
    pip install Flask joblib numpy scikit-learn
    ```

3.  **Place the Trained Model:**
    Ensure your pre-trained machine learning model file, `crop_model.pkl`, is located directly in your project's root directory (`D:\Python`). This file is essential for the system to make predictions.

4.  **Verify Static Assets:**
    Ensure your images (`background.jpg`, `header.jpg`, `leaf_icon.png`) are correctly placed in the `static/images/` subfolder within your project root (`D:\Python\static\images`).

### Running the Application

1.  **Start the Flask Server:**
    From your project's root directory (`D:\Python`) in the terminal/Git Bash, run:
    ```bash
    python app.py
    ```
    You should see output indicating the Flask app is running, typically on `http://127.0.0.1:5000`.

2.  **Access the Web Interface:**
    Open your web browser and go to `http://127.0.0.1:5000/`.

## Project Structure