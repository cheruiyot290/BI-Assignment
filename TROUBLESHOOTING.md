# Troubleshooting Guide

## 🔧 Common Issues and Solutions

### ❌ Error: "LinearRegression is not defined"

**Problem**: You're trying to use `LinearRegression()` before importing it.

**Solution**:
1. **Find the first code cell** that contains the imports:
   ```python
   from sklearn.linear_model import LinearRegression
   ```
2. **Run this cell first** by clicking on it and pressing `Shift + Enter`
3. **Wait for completion** - you should see "All libraries imported successfully!"
4. **Then run the other cells in order**

**Quick Fix**: The notebook now includes a safety check that will automatically import `LinearRegression` if needed.

---

### ❌ Error: "No module named 'sklearn'"

**Problem**: scikit-learn is not installed.

**Solution**:
```bash
pip install scikit-learn
# or
pip install -r requirements.txt
```

---

### ❌ Error: "No module named 'pandas'"

**Problem**: Required libraries are not installed.

**Solution**:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy jupyter
# or
pip install -r requirements.txt
```

---

### ❌ Error: "FileNotFoundError: sample_house_data.csv"

**Problem**: The sample data file is missing.

**Solution**:
1. Make sure `sample_house_data.csv` is in the same directory as the notebook
2. Or download the real Kaggle dataset and update the filename
3. The notebook will create sample data automatically if the file is missing

---

### ❌ Error: "plt.style.use('seaborn-v0_8') not found"

**Problem**: Older version of matplotlib/seaborn.

**Solution**: Replace the style line with:
```python
plt.style.use('seaborn')  # For older versions
# or
import matplotlib.pyplot as plt  # Use default style
```

---

### ❌ Jupyter Notebook won't start

**Problem**: Jupyter is not installed or configured.

**Solution**:
```bash
pip install jupyter
jupyter notebook
```

**Alternative**: Use the Python script instead:
```bash
python3 house_price_prediction.py
```

---

### ❌ Plots not showing in Jupyter

**Problem**: Matplotlib backend issue.

**Solution**: Add this to the first cell:
```python
%matplotlib inline
import matplotlib.pyplot as plt
```

---

### ❌ "Kernel appears to have died"

**Problem**: Memory or dependency issues.

**Solutions**:
1. **Restart the kernel**: Kernel → Restart
2. **Clear outputs**: Cell → All Output → Clear
3. **Run cells one by one** instead of all at once
4. **Use the Python script** as alternative

---

### ❌ Wrong results or strange numbers

**Problem**: Using wrong dataset or columns.

**Solution**:
1. Check that you're using the correct CSV file
2. Verify column names match ('area' and 'price')
3. Check for missing values or data type issues

---

## 🚀 Best Practices

### ✅ Recommended Workflow:

1. **Start fresh**: Restart kernel if you encounter issues
2. **Run in order**: Execute cells from top to bottom
3. **Check outputs**: Make sure each cell completes successfully
4. **Save frequently**: Save your work regularly

### ✅ Cell Execution Order:

1. **Import libraries** (first cell)
2. **Load data** (second cell)
3. **Explore data** (visualization cells)
4. **Build model** (LinearRegression cells)
5. **Analyze results** (final cells)

### ✅ If All Else Fails:

**Use the Python script instead**:
```bash
python3 house_price_prediction.py
```

This script:
- ✅ Works without Jupyter
- ✅ Has all the same analysis
- ✅ Includes all assignment answers
- ✅ Requires no additional setup

---

## 📞 Getting Help

### Check These First:
1. ✅ All required files in same directory?
2. ✅ Python 3 installed?
3. ✅ Required packages installed?
4. ✅ Ran import cell first?
5. ✅ No typos in filenames?

### Debug Commands:
```python
# Check if libraries are available
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
print("All imports successful!")

# Check current directory
import os
print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir('.'))

# Check data file
import pandas as pd
df = pd.read_csv('sample_house_data.csv')
print("Data loaded successfully!")
print(df.head())
```

### Still Having Issues?
1. Try the **Python script version** first
2. Check the **SETUP_GUIDE.md** for installation help
3. Verify all files are in the correct directory
4. Make sure you have Python 3.7+ installed

---

**Remember**: The assignment works perfectly with either the Jupyter notebook or the Python script. If one doesn't work, try the other!
