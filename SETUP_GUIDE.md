# House Price Prediction Assignment - Setup Guide

## Quick Start (Recommended)

### Option 1: Run the Python Script (No Dependencies Required)
The simplest way to see the assignment results:

```bash
python3 house_price_prediction.py
```

This script uses only built-in Python libraries and demonstrates:
- Simple linear regression calculations
- Manual implementation of the mathematical formulas
- Complete analysis with results for all assignment questions

### Option 2: Use Jupyter Notebook (Full Experience)
For the complete interactive experience with visualizations:

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
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

## Files Included

- **`house_price_prediction.ipynb`** - Complete Jupyter notebook with visualizations
- **`house_price_prediction.py`** - Standalone Python script (no dependencies)
- **`requirements.txt`** - Python dependencies for the notebook
- **`README.md`** - Detailed project documentation
- **`SETUP_GUIDE.md`** - This setup guide

## Assignment Questions Answered

✅ **Question 1: What is the equation of the line of best fit?**
- The script calculates and displays the slope (m) and intercept (c) values
- Shows the complete equation: Price = m × Area + c

✅ **Question 2: How well does the line fit the data?**
- Calculates R² score to evaluate model accuracy
- Provides interpretation of the fit quality

✅ **Question 3: Predict the price for 1500 sq ft house**
- Makes the specific prediction requested
- Shows the calculation process

## Key Features

### Mathematical Implementation
- Manual calculation of linear regression coefficients
- Step-by-step demonstration of the formulas:
  - Slope: m = Σ((x-x̄)(y-ȳ)) / Σ((x-x̄)²)
  - Intercept: c = ȳ - m*x̄
  - R²: 1 - (SSR/SST)

### Educational Value
- Shows both manual calculations and library implementations
- Explains each step of the process
- Provides clear interpretation of results

### Data Analysis
- Creates realistic housing dataset
- Performs correlation analysis
- Calculates residuals and error metrics

## Troubleshooting

### If you get "Module not found" errors:
1. Make sure you're using Python 3
2. For the notebook, ensure all dependencies are installed
3. Use the standalone script if you want to avoid dependency issues

### If Jupyter won't start:
1. Make sure you've activated the virtual environment
2. Try: `pip install jupyter` if it's missing
3. Use the Python script as an alternative

## Expected Output

The script will show:
- Dataset overview and statistics
- Linear regression equation
- R² score and model performance
- Prediction for 1500 sq ft house
- Sample data points with residuals
- Complete answers to all assignment questions

## Next Steps

After running the basic analysis, you can:
1. Modify the dataset size in the script
2. Experiment with different house areas for predictions
3. Add more features for multiple linear regression
4. Implement cross-validation for better evaluation

## Support

If you encounter any issues:
1. Check that Python 3 is installed
2. Try the standalone script first (no dependencies)
3. Ensure all files are in the same directory
4. Check the README.md for more detailed information
