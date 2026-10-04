# Weather Data Analysis

## 1. Project Title

**Weather Data Analysis using Python and Git**

## 2. Objective

The objective of this project is to analyze weather data using Python, perform data preprocessing, calculate temperature statistics, and visualize important weather patterns. Git and GitHub are used for version control and project management.

## 3. Dataset Description

The dataset contains weather-related information such as:

* Date
* Temperature
* Humidity
* Rainfall
* Wind Speed
* Atmospheric Pressure

The dataset is cleaned and preprocessed before performing the analysis.

## 4. Tools and Libraries Used

### Tools

* Python
* Jupyter Notebook
* Git
* GitHub
* VS Code

### Python Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn

## 5. Data Preprocessing

The following preprocessing operations were performed:

* Removed unnecessary spaces from column names.
* Converted weather-related columns into numeric format.
* Treated missing values using appropriate statistical methods.
* Converted the date column into datetime format.
* Removed duplicate records.
* Calculated temperature statistics.
* Saved the processed dataset as `weather_preprocessed.csv`.

## 6. Temperature Analysis

Temperature statistics were calculated to understand the distribution of temperature values.

The following statistics were analyzed:

* Mean temperature
* Median temperature
* Minimum temperature
* Maximum temperature
* Standard deviation
* Descriptive statistics

## 7. Data Visualizations

The project includes the following visualizations:

### Temperature Trend

Shows how temperature changes over time.

### Rainfall Trend

Shows rainfall variation over time.

### Humidity vs Temperature

Shows the relationship between humidity and temperature.

### Wind Speed Distribution

Shows the distribution of wind speed values.

### Correlation Heatmap

Shows relationships between different numerical weather variables.

The generated visualizations are stored in the `results/` folder.

## 8. Project Structure

```text
weather analysis report/
│
├── data/
│   └── weather_preprocessed.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   └── analysis.py
│
├── results/
│   ├── temperature_trend.png
│   ├── rainfall_trend.png
│   ├── humidity_vs_temperature.png
│   ├── wind_speed_distribution.png
│   └── correlation_heatmap.png
│
├── docs/
│   └── project_report.pdf
│
├── screenshots/
│
├── README.md
└── .gitignore
```

## 9. Git Features Used

The following Git features were demonstrated:

* Repository initialization
* Adding files using `git add`
* Committing changes using `git commit`
* Creating branches
* Switching branches
* Modifying project files
* Merging branches
* Comparing changes
* Viewing Git history
* Connecting the local repository to GitHub
* Pushing the project to GitHub

### Branches Used

* `main`
* `weather-preprocessing`
* `weather-visualization`

## 10. Conclusion

This project demonstrates the complete workflow of weather data analysis using Python along with Git-based version control. The weather dataset was preprocessed, analyzed statistically, and visualized to identify important weather patterns. Git branches and commits were used to organize the development process, and the final project was uploaded to GitHub.
