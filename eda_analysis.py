"""
Exploratory Data Analysis Script
This script performs basic EDA on sample data with performance optimizations.
"""

import pandas as pd
import numpy as np
from typing import Dict


def generate_sample_data(n_rows: int = 100000) -> pd.DataFrame:
    """Generate sample data for analysis."""
    np.random.seed(42)
    return pd.DataFrame({
        'id': range(n_rows),
        'category': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
        'value': np.random.randn(n_rows) * 100,
        'date': pd.date_range('2020-01-01', periods=n_rows, freq='min'),
        'flag': np.random.choice([True, False], n_rows)
    })


def calculate_statistics(df: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate basic statistics efficiently.
    
    Performance optimization: Use vectorized operations instead of loops.
    """
    # Efficient approach using pandas built-in methods
    stats = {
        'mean': df['value'].mean(),
        'median': df['value'].median(),
        'std': df['value'].std(),
        'min': df['value'].min(),
        'max': df['value'].max()
    }
    return stats


def group_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform grouped analysis by category.
    
    Performance optimization: Use groupby with agg for multiple operations at once.
    """
    # Efficient approach: single groupby with multiple aggregations
    result = df.groupby('category').agg({
        'value': ['mean', 'sum', 'count'],
        'flag': 'sum'
    })
    result.columns = ['_'.join(col).strip() for col in result.columns.values]
    return result


def filter_data(df: pd.DataFrame, threshold: float = 0) -> pd.DataFrame:
    """
    Filter data based on conditions.
    
    Performance optimization: Use boolean indexing instead of iterrows.
    """
    # Efficient approach using boolean indexing
    return df[df['value'] > threshold]


def create_derived_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create derived features efficiently.
    
    Performance optimization: Use vectorized operations.
    Note: Returns a copy to avoid modifying the original DataFrame.
    For very large datasets, consider using inplace operations to save memory.
    """
    df = df.copy()
    
    # Efficient vectorized operations
    df['value_squared'] = df['value'] ** 2
    df['value_normalized'] = (df['value'] - df['value'].mean()) / df['value'].std()
    df['category_encoded'] = pd.Categorical(df['category']).codes
    
    return df


def main():
    """Main execution function."""
    print("Starting EDA Analysis...")
    
    # Generate data
    print("Generating sample data...")
    df = generate_sample_data(100000)
    print(f"Data shape: {df.shape}")
    
    # Calculate statistics
    print("\nCalculating statistics...")
    stats = calculate_statistics(df)
    print("Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value:.2f}")
    
    # Group analysis
    print("\nPerforming group analysis...")
    grouped = group_analysis(df)
    print(grouped)
    
    # Filter data
    print("\nFiltering data...")
    filtered = filter_data(df, threshold=50)
    print(f"Filtered data shape: {filtered.shape}")
    
    # Create derived features
    print("\nCreating derived features...")
    df_enhanced = create_derived_features(df)
    print(f"Enhanced data columns: {df_enhanced.columns.tolist()}")
    
    print("\nEDA Analysis completed successfully!")


if __name__ == "__main__":
    main()
