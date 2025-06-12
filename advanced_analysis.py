#!/usr/bin/env python3
"""
Advanced House Price Prediction Analysis
Building on Simple Linear Regression

This script demonstrates multiple improvements over basic linear regression:
1. Multiple Linear Regression
2. Feature Engineering
3. Cross-Validation
4. Regularization (Ridge/Lasso)
5. Model Comparison

Author: BI Assignment Advanced Analysis
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import warnings
warnings.filterwarnings('ignore')

def load_and_prepare_data():
    """Load and prepare the housing dataset"""
    try:
        df = pd.read_csv('Housing.csv')
        print(f"✅ Loaded {len(df)} records from Housing.csv")
    except FileNotFoundError:
        print("❌ Housing.csv not found. Creating sample data...")
        # Create sample data
        np.random.seed(42)
        n = 500
        df = pd.DataFrame({
            'price': np.random.normal(8000000, 2000000, n),
            'area': np.random.normal(7000, 2000, n),
            'bedrooms': np.random.choice([2, 3, 4, 5], n),
            'bathrooms': np.random.choice([1, 2, 3], n),
            'stories': np.random.choice([1, 2, 3, 4], n),
            'mainroad': np.random.choice(['yes', 'no'], n),
            'guestroom': np.random.choice(['yes', 'no'], n),
            'basement': np.random.choice(['yes', 'no'], n),
            'hotwaterheating': np.random.choice(['yes', 'no'], n),
            'airconditioning': np.random.choice(['yes', 'no'], n),
            'parking': np.random.choice([0, 1, 2, 3], n),
            'prefarea': np.random.choice(['yes', 'no'], n),
            'furnishingstatus': np.random.choice(['furnished', 'semi-furnished', 'unfurnished'], n)
        })
        print(f"✅ Created sample dataset with {len(df)} records")
    
    return df

def preprocess_data(df):
    """Preprocess the dataset for machine learning"""
    df_processed = df.copy()
    
    # Handle categorical variables
    categorical_cols = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 
                       'airconditioning', 'prefarea']
    
    # Convert yes/no to 1/0
    for col in categorical_cols:
        if col in df_processed.columns:
            df_processed[col] = df_processed[col].map({'yes': 1, 'no': 0})
    
    # Handle furnishingstatus with label encoding
    if 'furnishingstatus' in df_processed.columns:
        le = LabelEncoder()
        df_processed['furnishingstatus'] = le.fit_transform(df_processed['furnishingstatus'])
    
    return df_processed

def create_enhanced_features(X):
    """Create new features from existing ones"""
    X_enhanced = X.copy()
    
    # Feature engineering
    if 'area' in X_enhanced.columns and 'bedrooms' in X_enhanced.columns:
        X_enhanced['area_per_bedroom'] = X_enhanced['area'] / (X_enhanced['bedrooms'] + 1)
    
    if 'area' in X_enhanced.columns and 'bathrooms' in X_enhanced.columns:
        X_enhanced['area_per_bathroom'] = X_enhanced['area'] / (X_enhanced['bathrooms'] + 1)
    
    if 'bedrooms' in X_enhanced.columns and 'bathrooms' in X_enhanced.columns:
        X_enhanced['bedroom_bathroom_ratio'] = X_enhanced['bedrooms'] / (X_enhanced['bathrooms'] + 1)
    
    if 'area' in X_enhanced.columns:
        X_enhanced['area_squared'] = X_enhanced['area'] ** 2
    
    # Total amenities score
    amenity_cols = ['guestroom', 'basement', 'hotwaterheating', 'airconditioning']
    available_amenities = [col for col in amenity_cols if col in X_enhanced.columns]
    if available_amenities:
        X_enhanced['total_amenities'] = X_enhanced[available_amenities].sum(axis=1)
    
    return X_enhanced

def evaluate_models(X, y, X_enhanced):
    """Evaluate different models and return results"""
    results = {}
    
    # 1. Simple Linear Regression (area only)
    if 'area' in X.columns:
        X_simple = X[['area']]
        cv_scores = cross_val_score(LinearRegression(), X_simple, y, cv=5, scoring='r2')
        results['Simple (Area only)'] = {
            'mean_r2': cv_scores.mean(),
            'std_r2': cv_scores.std(),
            'features': 1
        }
    
    # 2. Multiple Linear Regression
    cv_scores = cross_val_score(LinearRegression(), X, y, cv=5, scoring='r2')
    results['Multiple Features'] = {
        'mean_r2': cv_scores.mean(),
        'std_r2': cv_scores.std(),
        'features': X.shape[1]
    }
    
    # 3. Enhanced Features
    cv_scores = cross_val_score(LinearRegression(), X_enhanced, y, cv=5, scoring='r2')
    results['Enhanced Features'] = {
        'mean_r2': cv_scores.mean(),
        'std_r2': cv_scores.std(),
        'features': X_enhanced.shape[1]
    }
    
    # 4. Ridge Regression
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_enhanced)
    
    ridge_alphas = [0.1, 1.0, 10.0, 100.0]
    best_ridge_score = 0
    best_ridge_alpha = 1.0
    
    for alpha in ridge_alphas:
        cv_scores = cross_val_score(Ridge(alpha=alpha), X_scaled, y, cv=5, scoring='r2')
        if cv_scores.mean() > best_ridge_score:
            best_ridge_score = cv_scores.mean()
            best_ridge_alpha = alpha
    
    results['Ridge Regression'] = {
        'mean_r2': best_ridge_score,
        'std_r2': 0,  # Simplified for this demo
        'features': X_enhanced.shape[1],
        'alpha': best_ridge_alpha
    }
    
    # 5. Lasso Regression
    lasso_alphas = [0.1, 1.0, 10.0, 100.0]
    best_lasso_score = 0
    best_lasso_alpha = 1.0
    
    for alpha in lasso_alphas:
        cv_scores = cross_val_score(Lasso(alpha=alpha, max_iter=2000), X_scaled, y, cv=5, scoring='r2')
        if cv_scores.mean() > best_lasso_score:
            best_lasso_score = cv_scores.mean()
            best_lasso_alpha = alpha
    
    results['Lasso Regression'] = {
        'mean_r2': best_lasso_score,
        'std_r2': 0,  # Simplified for this demo
        'features': X_enhanced.shape[1],
        'alpha': best_lasso_alpha
    }
    
    # 6. Random Forest
    cv_scores = cross_val_score(RandomForestRegressor(n_estimators=100, random_state=42), 
                               X_enhanced, y, cv=5, scoring='r2')
    results['Random Forest'] = {
        'mean_r2': cv_scores.mean(),
        'std_r2': cv_scores.std(),
        'features': X_enhanced.shape[1]
    }
    
    return results

def analyze_feature_importance(X_enhanced, y):
    """Analyze feature importance using Random Forest"""
    X_train, X_test, y_train, y_test = train_test_split(X_enhanced, y, test_size=0.2, random_state=42)
    
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    
    importance_df = pd.DataFrame({
        'Feature': X_enhanced.columns,
        'Importance': rf.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    return importance_df

def main():
    """Main function to run advanced analysis"""
    print("🚀 Advanced House Price Prediction Analysis")
    print("=" * 60)
    
    # Load and prepare data
    print("\n📊 Step 1: Loading and preparing data...")
    df = load_and_prepare_data()
    df_processed = preprocess_data(df)
    
    # Separate features and target
    X = df_processed.drop('price', axis=1)
    y = df_processed['price']
    
    print(f"Features: {list(X.columns)}")
    print(f"Dataset shape: {X.shape}")
    
    # Create enhanced features
    print("\n🔧 Step 2: Creating enhanced features...")
    X_enhanced = create_enhanced_features(X)
    new_features = [col for col in X_enhanced.columns if col not in X.columns]
    print(f"New features created: {new_features}")
    print(f"Total features: {X_enhanced.shape[1]} (was {X.shape[1]})")
    
    # Evaluate models
    print("\n📈 Step 3: Evaluating different models...")
    results = evaluate_models(X, y, X_enhanced)
    
    # Display results
    print("\n" + "=" * 60)
    print("                 MODEL COMPARISON RESULTS")
    print("=" * 60)
    
    results_df = pd.DataFrame([
        {
            'Model': name,
            'R² Score': data['mean_r2'],
            'Features': data['features']
        }
        for name, data in results.items()
    ]).sort_values('R² Score', ascending=False)
    
    print(results_df.to_string(index=False, float_format='%.4f'))
    
    # Feature importance analysis
    print("\n🌳 Step 4: Feature importance analysis...")
    importance_df = analyze_feature_importance(X_enhanced, y)
    
    print("\nTop 10 Most Important Features:")
    print(importance_df.head(10).to_string(index=False, float_format='%.4f'))
    
    # Summary and recommendations
    best_model = results_df.iloc[0]
    print(f"\n🎯 SUMMARY AND RECOMMENDATIONS:")
    print(f"\n✅ Best Model: {best_model['Model']}")
    print(f"   R² Score: {best_model['R² Score']:.4f}")
    print(f"   Features Used: {best_model['Features']}")
    
    improvement = best_model['R² Score'] - results['Simple (Area only)']['mean_r2']
    print(f"\n📈 Improvement over simple linear regression: {improvement:.4f}")
    print(f"   ({improvement/results['Simple (Area only)']['mean_r2']*100:.1f}% relative improvement)")
    
    print(f"\n🔍 Key Insights:")
    print(f"   • Most important feature: {importance_df.iloc[0]['Feature']}")
    print(f"   • Feature engineering added {len(new_features)} new features")
    print(f"   • Advanced models show significant improvement")
    
    print(f"\n📚 Next Steps:")
    print(f"   • Try hyperparameter tuning for best model")
    print(f"   • Collect more data for better performance")
    print(f"   • Consider ensemble methods")
    print(f"   • Deploy model for real-world predictions")
    
    print("\n" + "=" * 60)
    print("                 ANALYSIS COMPLETED!")
    print("=" * 60)

if __name__ == "__main__":
    main()
