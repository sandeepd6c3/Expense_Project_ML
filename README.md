# Expense_Project_ML

# 🧾 Monthly Expense Prediction System (Machine Learning)

## 📌 Overview

This project is a **Machine Learning-based Expense Prediction System** that predicts future monthly expenses based on historical data.
It uses **Linear Regression** to identify trends and forecast upcoming expenses.

---

## 🚀 Features

* 📊 Predicts next month's expense using past data
* 📈 Visualizes data with a regression line
* 🟢 Highlights future prediction on graph
* 🔁 Uses synthetic large dataset with random variation
* 📉 Calculates model error (MSE)

---

## 🧠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

---

## 📂 Project Structure

```
Expense_Project/
│
├── data.csv              # Dataset
├── generate_data.py      # Script to generate large dataset
├── model.py              # ML model (Linear Regression)
├── main.py               # Main execution file
├── plot.py               # Graph visualization
├── requirements.txt      # Dependencies
```

---

## ⚙️ How It Works

1. **Data Generation**

   * Synthetic data is generated with a trend + random variation
   * Simulates real-world expense behavior

2. **Model Training**

   * Linear Regression learns the relationship between:

     * Month (input)
     * Expense (output)

3. **Prediction**

   * Model predicts future expense using learned trend

4. **Visualization**

   * Blue dots → Actual data
   * Red line → Regression trend
   * Green dot → Future prediction

---

## ▶️ How to Run

### Step 1: Clone the repository

```
git clone https://github.com/your-username/Expense_Prediction_Project.git
cd Expense_Prediction_Project
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Generate dataset

```
python generate_data.py
```

### Step 4: Run the project

```
python main.py
```

---

## 📊 Sample Output

* Predicted Expense for Next Month
* Graph showing trend and prediction

---

## 📉 Model Evaluation

* Mean Squared Error (MSE) is used to measure model performance

---

## 💡 Use Cases

* Personal finance planning
* Budget forecasting
* Expense trend analysis

---

## 🔥 Future Improvements

* Add multiple features (income, savings, etc.)
* Use advanced models (Polynomial Regression)
* Build web interface (Streamlit)
* Real-time data integration

---

## 👨‍💻 Author

**Sandeep Choudhary**
B.Tech AI & Data Science
Arya College of Engineering & IT, Jaipur

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
