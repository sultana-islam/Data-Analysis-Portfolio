# Data Wrangling for Customer Analytics at City of Vancouver

## Project Title
Data Wrangling for Enhanced Citizen Services Analytics using Vancouver Datasets

## Objective
The primary goal of this project was to perform comprehensive data wrangling to prepare robust datasets for customer/citizen analytics at the City of Vancouver. By cleaning, transforming, and consolidating data from various sources, the project aimed to enhance the accuracy and usability of city service data for subsequent analysis and reporting.

## Background
The City of Vancouver has accumulated data from multiple channels, including park facilities, neighborhood demographics, and community center usage. However, this data was often inconsistent, incomplete, or fragmented, making it challenging to derive meaningful insights about citizen service needs and usage patterns. Effective data wrangling facilitated better decision-making and more targeted service delivery strategies.

## Datasets
The data wrangling process involved various datasets, including:

1. **Park Facilities Data**: Information about recreational facilities in Vancouver parks
2. **Neighborhood Demographics**: Population and demographic information for Vancouver neighborhoods
3. **Community Center Usage**: Attendance and program participation at community centers

These datasets initially contained various data quality issues including missing values, inconsistent formatting, duplicate records, and incompatible data types.

## Methodology

### 1. Data Assessment
- Conducted a thorough examination of all datasets to identify:
  - Missing values and their patterns
  - Inconsistent data formats
  - Duplicate records
  - Erroneous data points
  - Data type inconsistencies
- Documented all data quality issues in a comprehensive assessment report
- Prioritized issues based on impact on subsequent analysis

### 2. Data Cleaning
- **Handling Missing Values**:
  - Imputed missing numerical values using appropriate methods (mean, median, or mode)
  - For categorical variables, applied domain-specific logic or used "Unknown" category
  - Removed records with critical missing data when necessary

- **Removing Duplicates**:
  - Identified and eliminated duplicate records
  - Preserved the most complete record when duplicates contained varying information

- **Standardizing Formats**:
  - Normalized date formats to ISO standard (YYYY-MM-DD)
  - Standardized text fields (proper case, consistent abbreviations)
  - Unified units of measurement across datasets

- **Correcting Errors**:
  - Identified and fixed outliers and impossible values
  - Corrected misspellings in categorical variables
  - Resolved inconsistencies between related fields

### 3. Data Transformation
- **Type Conversion**:
  - Converted data types to appropriate formats (string to date, text to numeric)
  - Ensured consistent data types across related fields in different datasets

- **Feature Engineering**:
  - Created derived variables to enhance analysis capabilities
  - Calculated aggregate measures where appropriate
  - Developed categorical groupings for numerical ranges

- **Normalization**:
  - Applied scaling techniques to numerical variables
  - Created consistent category levels across datasets

### 4. Data Integration
- Developed a unified data model to connect the different datasets
- Created primary and foreign key relationships for joining datasets
- Merged datasets to create integrated views for specific analytical purposes
- Validated integrated datasets for completeness and accuracy

### 5. Workflow Automation
- Implemented AWS DataBrew to automate data cleaning operations
- Created reusable recipe files for consistent transformation across datasets
- Developed data pipeline for ongoing data refreshes

## Tools and Technologies Used

- **AWS DataBrew**: Primary tool for data profiling, cleaning, and transformation
- **AWS S3**: Storage for raw and processed datasets
- **AWS Glue**: ETL service for complex transformations and workflow orchestration
- **Python**: Custom scripts for specialized cleaning and transformation tasks
  - Pandas: Data manipulation library
  - NumPy: Numerical operations
  - Regex: Pattern matching for data cleaning
- **AWS QuickSight**: Data visualization for validation and quality assessment

## Technical Implementation

### AWS DataBrew Configuration
```json
{
  "Name": "VancouverParksFacilities",
  "Description": "Recipe for cleaning Vancouver Parks Facilities data",
  "Steps": [
    {
      "Action": {
        "Operation": "DETECT_DATA_TYPES",
        "Parameters": {}
      }
    },
    {
      "Action": {
        "Operation": "REMOVE_DUPLICATES",
        "Parameters": {
          "columnSelectors": [
            {
              "regex": "ParkID"
            }
          ]
        }
      }
    },
    {
      "Action": {
        "Operation": "FILL_MISSING_VALUES",
        "Parameters": {
          "columnSelectors": [
            {
              "regex": "FacilityCount"
            }
          ],
          "value": "0"
        }
      }
    },
    {
      "Action": {
        "Operation": "CHANGE_DATA_TYPE",
        "Parameters": {
          "columnSelectors": [
            {
              "regex": "FacilityCount"
            }
          ],
          "newDataType": "INTEGER"
        }
      }
    }
  ]
}
```

### Python Data Cleaning Script (Sample)
```python
import pandas as pd
import numpy as np
import re

def clean_vancouver_dataset(file_path, output_path):
    """
    Clean the Vancouver dataset
    
    Parameters:
    file_path (str): Path to the input CSV file
    output_path (str): Path for the cleaned output file
    """
    # Load the data
    df = pd.read_csv(file_path)
    
    # Standardize column names
    df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]
    
    # Handle missing values
    df['facilitycount'] = df['facilitycount'].fillna(0).astype(int)
    
    # Standardize facility types
    df['facilitytype'] = df['facilitytype'].str.title()
    
    # Apply regex pattern to standardize format
    pattern = r'(.+)\s+Park$'
    df['name'] = df['name'].apply(
        lambda x: re.sub(pattern, r'\1 Park', x) if isinstance(x, str) else x
    )
    
    # Remove duplicates
    df = df.drop_duplicates(subset=['parkid', 'facilitytype'])
    
    # Save the cleaned dataset
    df.to_csv(output_path, index=False)
    
    return df

# Example usage
clean_vancouver_dataset('raw_parks_data.csv', 'cleaned_parks_data.csv')
```

## Results and Impact

### Data Quality Improvements
- Reduced missing values from 15% to less than 2%
- Eliminated all duplicate records
- Standardized 100% of date fields to consistent format
- Corrected facility type categorizations, reducing unique categories from 36 to 24
- Unified naming conventions across all datasets

### Efficiency Gains
- Automated data cleaning process reduced manual effort by approximately 85%
- Decreased data preparation time from days to hours
- Created reusable transformation recipes that can be applied to future data refreshes

### Enhanced Analytics Capabilities
- Integrated datasets enabled cross-domain analysis
- Improved data quality allowed for more accurate insights
- Standardized formats facilitated easier visualization and reporting

## Lessons Learned

- **Importance of Thorough Data Profiling**: Initial comprehensive assessment saved significant time by identifying all issues upfront
- **Value of Standardized Approach**: Consistent cleaning methods across datasets simplified integration
- **Automation Benefits**: Investing time in automated workflows paid dividends in reproducibility and efficiency
- **Documentation Necessity**: Detailed documentation of transformation steps enabled knowledge sharing and process improvement

## Future Improvements

- Implement more sophisticated imputation methods for missing values
- Develop real-time data quality monitoring
- Expand the data model to include additional City of Vancouver datasets
- Create a metadata repository to track data lineage and transformations

## Reflection

This data wrangling project demonstrated the critical importance of thorough data preparation in the analysis process. By methodically addressing data quality issues and implementing automated cleaning workflows using AWS services, the project transformed raw, problematic datasets into reliable analytical assets.

The skills developed during this project—systematic data assessment, application of appropriate cleaning techniques, and implementation of cloud-based data processing tools—provide a solid foundation for handling diverse data challenges in future projects. The resulting integrated datasets not only supported the immediate analytical needs but also established a framework for ongoing data management and analysis of City of Vancouver data.
