[Watch the demo video here--->](https://drive.google.com/drive/u/0/folders/1hy0UWr-5cNdlcmiNqGrk-2P6hktUfQLM)



 Machine Downtime Prediction API

This is a RESTful API that predicts machine downtime based on the temperature and runtime of the machine. The model is built using Logistic Regression and can be used to make predictions regarding machine failure or downtime in manufacturing settings.

 Project Structure

```
.
├── app.py                     # Main Flask application
├── downtime_model.pkl          # Trained model
├── manufacturing_data.csv      # Synthetic dataset
└── README.md                   # Project documentation
```

### Setup Instructions

 1. Clone the Repository

Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/machine-downtime-api.git
cd machine-downtime-api
```

### 2. Install Dependencies

Make sure you have Python installed. Create a virtual environment and install the required dependencies:
```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required dependencies
pip install -r requirements.txt
```

### 3. Run the Flask App

To run the application locally, use the following command:
```bash
python app.py
```
The API will be accessible at `http://127.0.0.1:5000/`.

### 4. Test the API

You can test the API endpoints using **Postman** or **cURL**.

---

## API Endpoints

### 1. **Home Route**
**GET /**

Returns a welcome message.

**Example Response**:
```json
{
    "message": "Welcome to the Machine Downtime Prediction API!"
}
```

### 2. **Predict Route**
**POST /predict**

This endpoint predicts whether a machine will experience downtime based on the input features (`Temperature` and `Run_Time`).

**Request Body**:
```json
{
    "Temperature": 80,
    "Run_Time": 120
}
```

**Example Response**:
```json
{
    "Downtime": "No",
    "Confidence": 0.31
}
```

**Description**:
- `Downtime`: Indicates if the machine is predicted to have downtime ("Yes"/"No").
- `Confidence`: The confidence score of the prediction, which is a value between 0 and 1.





1. **GitHub Repository** containins:
   - The **codebase** for the API.
   - A **sample dataset** (`manufacturing_data.csv`).
   - The **trained model** (`downtime_model.pkl`).
   - This **README file**.

2. A **working API** that can be tested locally using Postman or cURL.

---



### **requirements.txt**
Make sure to create a `requirements.txt` file with the dependencies:

```
Flask==2.1.1
joblib==1.1.0
numpy==1.21.4
scikit-learn==1.0.1
```

---

### **GitHub Repository Setup**
To set up this project in a GitHub repository:

1. Create a new repository on GitHub (e.g., `machine-downtime-api`).
2. Push your local project to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/machine-downtime-api.git
   git push -u origin master
   ```




