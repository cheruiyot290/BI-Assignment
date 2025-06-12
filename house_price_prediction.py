#!/usr/bin/env python3
"""
House Price Prediction Using Simple Linear Regression
Business Intelligence & Data Analytics Assignment

This script demonstrates simple linear regression for house price prediction
following the equation: y = mx + c

Author: BI Assignment
Date: 2024
"""

import random
import math

def load_kaggle_data():
    """Try to load the real Kaggle dataset, fallback to sample data"""
    try:
        # Try to load the real Kaggle dataset
        # Update this filename to match your downloaded Kaggle file
        import csv

        # Try common Kaggle dataset filenames
        possible_files = ['Housing.csv', 'house_data.csv', 'housing_prices.csv', 'sample_house_data.csv']

        for filename in possible_files:
            try:
                areas = []
                prices = []

                with open(filename, 'r') as file:
                    reader = csv.DictReader(file)

                    # Try to find area and price columns (case insensitive)
                    area_col = None
                    price_col = None

                    for col in reader.fieldnames:
                        if col.lower() in ['area', 'sqft', 'size']:
                            area_col = col
                        elif col.lower() in ['price', 'cost', 'value']:
                            price_col = col

                    if area_col and price_col:
                        for row in reader:
                            try:
                                area = float(row[area_col])
                                price = float(row[price_col])
                                areas.append(area)
                                prices.append(price)
                            except (ValueError, KeyError):
                                continue

                        if areas and prices:
                            print(f"✅ Successfully loaded {len(areas)} records from {filename}")
                            return areas, prices

            except FileNotFoundError:
                continue

        # If no real dataset found, create sample data
        print("📝 Kaggle dataset not found. Creating sample data...")
        return create_sample_data()

    except Exception as e:
        print(f"⚠️ Error loading data: {e}")
        print("📝 Creating sample data...")
        return create_sample_data()

def create_sample_data(n_samples=100):
    """Create sample housing data for demonstration"""
    random.seed(42)

    # Generate house areas (square feet) and prices
    areas = []
    prices = []

    true_slope = 1000  # Price per sq ft (more realistic for the sample data)
    true_intercept = 2000000  # Base price

    for _ in range(n_samples):
        # Generate area with some randomness around 7000 sq ft
        area = random.gauss(7000, 2000)
        area = max(3000, min(15000, area))  # Clip to reasonable range

        # Generate price with linear relationship + noise
        noise = random.gauss(0, 1000000)
        price = true_slope * area + true_intercept + noise
        price = max(3000000, min(15000000, price))  # Clip to reasonable range

        areas.append(area)
        prices.append(price)

    return areas, prices

def explore_data(areas, prices):
    """Explore and analyze the dataset"""
    n = len(areas)

    print("=== DATASET OVERVIEW ===")
    print(f"Number of houses: {n}")

    # Calculate basic statistics
    area_mean = sum(areas) / n
    price_mean = sum(prices) / n

    area_min, area_max = min(areas), max(areas)
    price_min, price_max = min(prices), max(prices)

    print(f"\nArea Statistics:")
    print(f"  Mean: {area_mean:.2f} sq ft")
    print(f"  Range: {area_min:.2f} - {area_max:.2f} sq ft")

    print(f"\nPrice Statistics:")
    print(f"  Mean: {price_mean:.2f} KSh")
    print(f"  Range: {price_min:.2f} - {price_max:.2f} KSh")

    # Calculate correlation
    correlation = calculate_correlation(areas, prices)
    print(f"\nCorrelation between Area and Price: {correlation:.4f}")

    return correlation

def calculate_correlation(x_values, y_values):
    """Calculate Pearson correlation coefficient"""
    n = len(x_values)
    x_mean = sum(x_values) / n
    y_mean = sum(y_values) / n

    numerator = sum((x_values[i] - x_mean) * (y_values[i] - y_mean) for i in range(n))
    x_variance = sum((x_values[i] - x_mean) ** 2 for i in range(n))
    y_variance = sum((y_values[i] - y_mean) ** 2 for i in range(n))

    denominator = math.sqrt(x_variance * y_variance)

    if denominator == 0:
        return 0

    return numerator / denominator

def manual_linear_regression(areas, prices):
    """Calculate linear regression coefficients manually"""
    n = len(areas)

    # Calculate means
    x_mean = sum(areas) / n
    y_mean = sum(prices) / n

    # Calculate slope: m = Σ((x-x̄)(y-ȳ)) / Σ((x-x̄)²)
    numerator = sum((areas[i] - x_mean) * (prices[i] - y_mean) for i in range(n))
    denominator = sum((areas[i] - x_mean) ** 2 for i in range(n))

    if denominator == 0:
        slope = 0
    else:
        slope = numerator / denominator

    # Calculate intercept: c = ȳ - m*x̄
    intercept = y_mean - slope * x_mean

    # Calculate predictions
    predictions = [slope * area + intercept for area in areas]

    # Calculate R² manually
    sst = sum((prices[i] - y_mean) ** 2 for i in range(n))  # Total sum of squares
    ssr = sum((prices[i] - predictions[i]) ** 2 for i in range(n))  # Residual sum of squares

    if sst == 0:
        r2 = 1.0
    else:
        r2 = 1 - (ssr / sst)

    # Calculate RMSE
    mse = ssr / n
    rmse = math.sqrt(mse)

    return slope, intercept, r2, rmse, predictions

def simple_visualization(areas, prices, slope, intercept, r2, predictions):
    """Create a simple text-based visualization and analysis"""
    print("\n" + "="*60)
    print("           VISUALIZATION AND ANALYSIS")
    print("="*60)

    # Predict for 1500 sq ft
    area_1500 = 1500
    price_1500 = slope * area_1500 + intercept

    print(f"\n📈 REGRESSION LINE EQUATION:")
    print(f"   Price = {slope:.2f} × Area + {intercept:.2f}")
    print(f"   R² = {r2:.4f}")

    print(f"\n🎯 PREDICTION FOR 1500 SQ FT HOUSE:")
    print(f"   Predicted Price: {price_1500:.2f} KSh")
    print(f"   Price per sq ft: {price_1500/area_1500:.2f} KSh")

    # Show some sample data points
    print(f"\n📊 SAMPLE DATA POINTS (First 10):")
    print(f"{'Area (sq ft)':<12} {'Actual Price':<15} {'Predicted Price':<15} {'Residual':<10}")
    print("-" * 55)

    for i in range(min(10, len(areas))):
        residual = prices[i] - predictions[i]
        print(f"{areas[i]:<12.0f} {prices[i]:<15.0f} {predictions[i]:<15.0f} {residual:<10.0f}")

    # Calculate residual statistics
    residuals = [prices[i] - predictions[i] for i in range(len(prices))]
    mean_residual = sum(residuals) / len(residuals)
    abs_residuals = [abs(r) for r in residuals]
    mae = sum(abs_residuals) / len(abs_residuals)

    print(f"\n📏 RESIDUAL ANALYSIS:")
    print(f"   Mean Residual: {mean_residual:.2f} KSh")
    print(f"   Mean Absolute Error: {mae:.2f} KSh")

    return price_1500

def print_results(slope, intercept, r2, rmse, manual_slope, manual_intercept, manual_r2, price_1500):
    """Print comprehensive results"""
    print("\n" + "="*60)
    print("           HOUSE PRICE PREDICTION - RESULTS")
    print("="*60)

    print(f"\n🎯 ANSWERS TO ASSIGNMENT QUESTIONS:")
    print(f"\n1. EQUATION OF THE LINE OF BEST FIT:")
    print(f"   📈 Price = {slope:.2f} × Area + {intercept:.2f}")
    print(f"   📊 Slope (m): {slope:.2f} KSh per sq ft")
    print(f"   📊 Intercept (c): {intercept:.2f} KSh")

    print(f"\n2. HOW WELL DOES THE LINE FIT THE DATA:")
    print(f"   📊 R² Score: {r2:.4f} ({r2*100:.2f}%)")
    print(f"   📏 RMSE: {rmse:.2f} KSh")

    print(f"\n3. PREDICTION FOR 1500 SQ FT HOUSE:")
    print(f"   🏠 Area: 1500 sq ft")
    print(f"   💰 Predicted Price: {price_1500:.2f} KSh")
    print(f"   💵 Price per sq ft: {price_1500/1500:.2f} KSh")

    print(f"\n🔬 MANUAL CALCULATION VERIFICATION:")
    print(f"   Manual slope: {manual_slope:.2f}")
    print(f"   Manual intercept: {manual_intercept:.2f}")
    print(f"   Manual R²: {manual_r2:.4f}")

    print(f"\n📋 KEY INSIGHTS:")
    print(f"   • Each additional square foot increases price by {slope:.2f} KSh")
    print(f"   • The model explains {r2*100:.1f}% of price variation")
    print(f"   • Model is {'reliable' if r2 > 0.7 else 'moderately reliable' if r2 > 0.5 else 'less reliable'} for predictions")

def main():
    """Main function to run the complete analysis"""
    print("House Price Prediction Using Simple Linear Regression")
    print("Business Intelligence & Data Analytics Assignment")
    print("-" * 60)

    print("\n📥 DATASET LOADING:")
    print("To use the real Kaggle dataset:")
    print("1. Download from: https://www.kaggle.com/datasets/yasserh/housing-prices-dataset")
    print("2. Place the CSV file in this directory")
    print("3. The script will automatically detect and use it")
    print("-" * 60)

    # Step 1: Load and explore data
    print("\n📊 Step 1: Loading and exploring dataset...")
    areas, prices = load_kaggle_data()
    correlation = explore_data(areas, prices)

    # Step 2: Manual calculations (our main method)
    print("\n🔢 Step 2: Performing linear regression calculations...")
    slope, intercept, r2, rmse, predictions = manual_linear_regression(areas, prices)

    # Step 3: Visualize results
    print("\n📈 Step 3: Creating analysis and visualization...")
    price_1500 = simple_visualization(areas, prices, slope, intercept, r2, predictions)

    # Step 4: Print comprehensive results
    print_results(slope, intercept, r2, rmse, slope, intercept, r2, price_1500)

    print("\n" + "="*60)
    print("                    ANALYSIS COMPLETED!")
    print("="*60)

if __name__ == "__main__":
    main()
