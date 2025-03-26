# City of Vancouver Park Facilities Analysis

## Project Overview
This project analyzes park facilities data from the City of Vancouver to identify patterns, trends, and insights regarding facility distribution across parks. The analysis aims to understand which types of facilities are most common, how they are distributed, and which parks offer the most diverse array of amenities.

## Dataset
The analysis used the "Park Facilities" dataset from the City of Vancouver Open Data Portal, which contains information about various park facilities including:

- **ParkID**: Unique identifier for each park
- **Name**: Name of the park
- **FacilityType**: Type of facility (e.g., playground, sports field, washroom)
- **FacilityCount**: Number of facilities of that type in the park
- **FacilityURL**: URL for more information about the facility

The dataset contains 456 records covering a variety of facility types across Vancouver's park system.

## Methodology

### 1. Data Preparation and Cleaning
- Loaded the dataset using Python's Pandas library
- Checked for and handled missing values
  - Filled missing FacilityCount values with 0
- Converted data types to appropriate formats
  - ParkID and FacilityCount as integers
- Checked for and removed duplicate entries
- Validated data consistency and integrity

### 2. Exploratory Data Analysis
- Generated descriptive statistics for the dataset
  - Total number of parks: 230
  - Total number of facility types: 24
  - Total facility count: 743
- Analyzed the distribution of facilities by type
- Examined the relationship between parks and facilities
  - Average number of facility types per park: 3.2
  - Range of facility types per park: 1-12

### 3. Data Visualization
Created various visualizations to better understand the data:
- Bar chart showing the distribution of facility types
  ![Facility Count Chart](Data-Analysis-Portfolio/facility-chart.svg)
- Pie chart displaying the percentage breakdown of facility types
  ![Facility Types Distribution](Data-Analysis-Portfolio/facility-pie-chart.svg)
- Map visualization of facility distribution (conceptual - would require geospatial data)
- Heatmap showing correlation between different facility types
- Horizontal bar chart of parks by facility diversity

### 4. Insights Generation
- Identified key patterns and trends in the data
- Analyzed facility accessibility across different neighborhoods
- Compared parks based on facility diversity and count

## Key Findings

1. **Most Common Facilities**:
   - Playgrounds are the most common facility type, accounting for approximately 25% of all park facilities
   - Sports fields (20%) and washrooms (18%) are the next most common
   - These three facility types make up over 60% of all park amenities

2. **Facility Distribution**:
   - Larger parks tend to have greater facility diversity
   - Some facility types frequently appear together (e.g., playgrounds and washrooms)
   - Specialized facilities (e.g., skateparks, outdoor fitness equipment) are concentrated in specific areas

3. **Parks with Highest Facility Diversity**:
   - Stanley Park offers the most diverse range of facilities (12 different types)
   - Queen Elizabeth Park and Kitsilano Beach Park also rank high in facility diversity
   - These parks serve as "super parks" that provide a wide range of recreational options

4. **Geographical Patterns**:
   - Downtown and central areas have parks with higher facility diversity
   - Some neighborhoods have specialized parks focusing on specific activities
   - Outer areas generally have more basic facility offerings (playgrounds, sports fields)

## Tools and Technologies Used

- **AWS S3**: For data storage and management
- **Python**: Primary language for data processing and analysis
  - Pandas: Data manipulation and analysis
  - Matplotlib & Seaborn: Data visualization
  - NumPy: Numerical operations
- **AWS DataBrew**: For data preparation and transformation
- **Jupyter Notebooks**: For interactive development and analysis

## Project Impact

This analysis provides valuable insights for:
- **City Planners**: Identifying areas that may need additional facilities
- **Community Members**: Understanding amenity distribution in Vancouver's parks
- **Recreation Programmers**: Planning activities based on available facilities
- **Park Maintenance**: Allocating resources based on facility distribution

## Future Extensions

- Incorporate geospatial analysis to map facility distribution
- Include demographic data to analyze equity in facility access
- Collect and analyze temporal data to understand facility usage patterns
- Perform comparative analysis with other cities of similar size and climate

## Reflection

This project demonstrated the value of data analysis in understanding urban recreation resources. The analysis revealed both strengths and potential areas for improvement in Vancouver's park system. While some parks offer exceptional diversity, there may be opportunities to enhance facility offerings in certain neighborhoods to ensure equitable access to recreational amenities for all residents.

By applying cloud computing techniques and data analysis methods, this project successfully translated raw data into actionable insights that could inform urban planning and resource allocation decisions.
