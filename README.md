# House Price Prediction Using Simple Linear Regression

## Business Intelligence & Data Analytics Assignment

This project demonstrates house price prediction using simple linear regression, implementing the equation **y = mx + c** where:
- **y** = house price (dependent variable)
- **x** = house area (independent variable)
- **m** = slope (rate of price increase per unit area)
- **c** = intercept (base price when area = 0)

## 📋 Assignment Objectives

1. **Find the equation of the line of best fit** (values of m and c)
2. **Evaluate model performance** using R² score
3. **Make predictions** for specific house areas (e.g., 1500 sq ft)

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Jupyter Notebook

### Installation

1. **Clone or download this repository**
2. **Install required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

4. **Open the notebook:**
   - Navigate to `house_price_prediction.ipynb`
   - Run all cells to see the complete analysis

## 📊 What's Included

### Main Notebook: `house_price_prediction.ipynb`

**Step 1: Data Loading & Exploration**
- Instructions for downloading real Kaggle dataset
- Automatic detection of dataset structure
- Load and explore the housing dataset
- Check for missing values and basic statistics

**Step 2: Data Visualization**
- Scatter plots of area vs price
- Distribution analysis
- Correlation analysis

**Step 3: Linear Regression Model**
- Build model using scikit-learn
- Extract slope and intercept values
- Calculate R² score for model evaluation

**Step 4: Visualization with Regression Line**
- Plot actual data points (blue)
- Plot regression line (red)
- Highlight specific predictions (green)

**Step 5: Manual Calculations**
- Implement linear regression formulas by hand
- Verify results match scikit-learn
- Calculate R² manually

**Step 6: Model Analysis**
- Multiple predictions for different areas
- Residual analysis
- Model assumptions checking

## 📈 Key Results

The notebook will provide:
- **Equation**: Price = m × Area + c
- **R² Score**: Model accuracy percentage
- **Predictions**: Price estimates for any given area
- **Visualizations**: Clear plots showing the relationship

## 🔧 Libraries Used

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib & seaborn**: Data visualization
- **scikit-learn**: Machine learning algorithms
- **scipy**: Statistical functions

## 📚 Educational Value

This project demonstrates:
- Simple linear regression implementation
- Manual vs automated calculations
- Model evaluation techniques
- Data visualization best practices
- Statistical interpretation

## 🎯 Assignment Questions Answered

1. **What is the equation of the line of best fit?**
   - Extracts and interprets slope and intercept values

2. **How well does the line fit the data?**
   - Calculates and reports R² score for model accuracy

3. **Predict house price for 1500 sq ft**
   - Uses the model to predict and visualize the result

## 📖 References

- [How To Perform Simple Linear Regression by Hand](https://www.youtube.com/watch?v=GhrxgbQnEEU)
- [Housing Prices Dataset - Kaggle](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

## 🔄 Next Steps

For advanced analysis, consider:
- Multiple linear regression with more features
- Cross-validation for better evaluation
- Feature engineering and selection
- Polynomial regression for non-linear relationships

## 📥 Using Real Kaggle Data

### Quick Setup:
1. **Download**: Go to https://www.kaggle.com/datasets/yasserh/housing-prices-dataset
2. **Extract**: Place the CSV file in your project directory
3. **Run**: The code automatically detects and uses the real dataset

### Automatic Features:
- ✅ **Auto-detection** of Kaggle dataset files
- ✅ **Column mapping** for different naming conventions
- ✅ **Fallback** to sample data if Kaggle data unavailable
- ✅ **Error handling** for data format issues

See `KAGGLE_DATASET_GUIDE.md` for detailed instructions.

---
