import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the Park Facilities dataset
def load_and_clean_data(file_path):
    """
    Load and clean the park facilities data
    
    Parameters:
    file_path (str): Path to the CSV file
    
    Returns:
    pd.DataFrame: Cleaned DataFrame
    """
    # Load the data
    df = pd.read_csv(file_path)
    
    # Check for missing values
    print(f"Missing values before cleaning:\n{df.isnull().sum()}")
    
    # Handle missing values
    df['FacilityCount'] = df['FacilityCount'].fillna(0)
    
    # Convert data types
    df['ParkID'] = df['ParkID'].astype(int)
    df['FacilityCount'] = df['FacilityCount'].astype(int)
    
    # Check for duplicates
    duplicates = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicates}")
    
    # Remove duplicates if any
    if duplicates > 0:
        df = df.drop_duplicates()
    
    print(f"Missing values after cleaning:\n{df.isnull().sum()}")
    print(f"Data shape: {df.shape}")
    
    return df

def analyze_facility_distribution(df):
    """
    Analyze the distribution of facilities across parks
    
    Parameters:
    df (pd.DataFrame): The cleaned park facilities data
    """
    # Count of facilities by type
    facility_counts = df.groupby('FacilityType')['FacilityCount'].sum().sort_values(ascending=False)
    
    print("Top 10 Facility Types by Count:")
    print(facility_counts.head(10))
    
    # Create a bar chart
    plt.figure(figsize=(12, 6))
    facility_counts.head(10).plot(kind='bar', color='skyblue')
    plt.title('Top 10 Facility Types in Vancouver Parks')
    plt.xlabel('Facility Type')
    plt.ylabel('Total Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('facility_distribution.png')
    
    return facility_counts

def analyze_parks_by_facility_diversity(df):
    """
    Analyze parks by the diversity of facilities they offer
    
    Parameters:
    df (pd.DataFrame): The cleaned park facilities data
    """
    # Count unique facility types per park
    park_diversity = df.groupby('Name')['FacilityType'].nunique().sort_values(ascending=False)
    
    print("\nTop 10 Parks by Facility Diversity:")
    print(park_diversity.head(10))
    
    # Create a horizontal bar chart
    plt.figure(figsize=(12, 8))
    park_diversity.head(15).plot(kind='barh', color='lightgreen')
    plt.title('Top 15 Vancouver Parks by Facility Diversity')
    plt.xlabel('Number of Different Facility Types')
    plt.ylabel('Park Name')
    plt.tight_layout()
    plt.savefig('park_diversity.png')
    
    return park_diversity

def analyze_facility_correlation(df):
    """
    Analyze if there's any correlation between different facility types
    
    Parameters:
    df (pd.DataFrame): The cleaned park facilities data
    """
    # Create a pivot table: parks vs facility types
    pivot_df = df.pivot_table(
        index='Name', 
        columns='FacilityType', 
        values='FacilityCount', 
        aggfunc='sum',
        fill_value=0
    )
    
    # Calculate correlation between facility types
    correlation = pivot_df.corr()
    
    # Create a heatmap
    plt.figure(figsize=(14, 12))
    sns.heatmap(correlation, annot=False, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Between Facility Types')
    plt.tight_layout()
    plt.savefig('facility_correlation.png')
    
    return correlation

def create_facility_map(df):
    """
    Note: This function requires geospatial data which isn't in the original dataset.
    This is a placeholder to show how you might approach creating a map of facilities.
    
    Parameters:
    df (pd.DataFrame): The park facilities data with geospatial information
    """
    print("\nNote: To create an actual map visualization, we would need latitude and longitude data for each park.")
    print("In a real analysis, we could use libraries like Folium or GeoPlotLib to map facility distribution.")

def main():
    """
    Main function to run the analysis
    """
    # File path would need to be updated to your actual file location
    file_path = 'Park_Facilities_Cleaned.csv'
    
    # Load and clean the data
    df = load_and_clean_data(file_path)
    
    # Basic data exploration
    print("\nData Overview:")
    print(df.head())
    print("\nData Summary:")
    print(df.describe())
    
    # Summary statistics
    print("\nSummary Statistics by Facility Type:")
    print(df.groupby('FacilityType')['FacilityCount'].agg(['count', 'sum', 'mean', 'median', 'max']))
    
    # Analyze facility distribution
    facility_counts = analyze_facility_distribution(df)
    
    # Analyze parks by facility diversity
    park_diversity = analyze_parks_by_facility_diversity(df)
    
    # Analyze correlation between facility types
    correlation = analyze_facility_correlation(df)
    
    # Create a map of facilities (would require geospatial data)
    create_facility_map(df)
    
    print("\nAnalysis complete! Visualizations saved to the current directory.")

if __name__ == "__main__":
    main()
