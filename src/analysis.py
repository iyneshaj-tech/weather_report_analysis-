# ============================================================
# WEATHER DATA ANALYSIS PROJECT
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ============================================================
# 1. SET PROJECT PATHS
# ============================================================

# Project folder = one level above src
PROJECT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Create data and results folders inside project
DATA_DIR = os.path.join(PROJECT_DIR, "data")
RESULTS_DIR = os.path.join(PROJECT_DIR, "results")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)


# ============================================================
# 2. LOAD WEATHER DATASET
# ============================================================

df = pd.read_csv(
    r"C:\Users\Iynesha J\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\sessions\630C538269E1C546F78931AE9B57229DCD522C48\transfers\2026-40\Weather.csv"
)

print("========================================")
print("       WEATHER DATA ANALYSIS")
print("========================================")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())


# Remove spaces from column names
df.columns = df.columns.str.strip()


# ============================================================
# 3. DATASET INFORMATION
# ============================================================

print("\n========== DATASET INFORMATION ==========")

df.info()

print("\n========== STATISTICAL SUMMARY ==========")

print(df.describe())


# ============================================================
# 4. IDENTIFY WEATHER COLUMNS
# ============================================================

columns = df.columns.tolist()


def find_column(possible_names):

    for name in possible_names:

        for col in columns:

            if name.lower() in col.lower():

                return col

    return None


date_col = find_column([
    "date",
    "datetime",
    "day",
    "time"
])


temperature_col = find_column([
    "temperature",
    "temp"
])


humidity_col = find_column([
    "humidity",
    "humid"
])


wind_col = find_column([
    "wind_speed",
    "windspeed",
    "wind speed",
    "wind"
])


rainfall_col = find_column([
    "rainfall",
    "rain",
    "precipitation"
])


pressure_col = find_column([
    "pressure",
    "atmospheric pressure",
    "atm"
])


print("\n========== DETECTED COLUMNS ==========")

print("Date:", date_col)

print("Temperature:", temperature_col)

print("Humidity:", humidity_col)

print("Wind Speed:", wind_col)

print("Rainfall:", rainfall_col)

print("Pressure:", pressure_col)


# ============================================================
# 5. MISSING VALUES
# ============================================================

print("\n========== MISSING VALUES BEFORE TREATMENT ==========")

print(df.isnull().sum())


# ============================================================
# 6. DATE CONVERSION
# ============================================================

if date_col is not None:

    df[date_col] = pd.to_datetime(
        df[date_col],
        errors="coerce"
    )

    print("\nDate conversion completed.")


# ============================================================
# 7. DUPLICATE REMOVAL
# ============================================================

print("\n========== DUPLICATES ==========")

print(
    "Duplicates before removal:",
    df.duplicated().sum()
)


df = df.drop_duplicates()


print(
    "Duplicates after removal:",
    df.duplicated().sum()
)


# ============================================================
# 8. MISSING VALUE TREATMENT
# ============================================================

weather_columns = [
    temperature_col,
    humidity_col,
    wind_col,
    rainfall_col,
    pressure_col
]


for col in weather_columns:

    if col is not None:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

        df[col] = df[col].fillna(
            df[col].median()
        )


print("\n========== MISSING VALUES AFTER TREATMENT ==========")

print(df.isnull().sum())


# ============================================================
# 9. SORT DATA BY DATE
# ============================================================

if date_col is not None:

    df = df.sort_values(
        date_col
    )

    df = df.reset_index(
        drop=True
    )


# ============================================================
# 10. TEMPERATURE STATISTICS
# ============================================================

if temperature_col is not None:

    print("\n========== TEMPERATURE STATISTICS ==========")

    print(
        "Mean Temperature:",
        df[temperature_col].mean()
    )

    print(
        "Median Temperature:",
        df[temperature_col].median()
    )

    print(
        "Minimum Temperature:",
        df[temperature_col].min()
    )

    print(
        "Maximum Temperature:",
        df[temperature_col].max()
    )

    print(
        "Temperature Standard Deviation:",
        df[temperature_col].std()
    )

    print("\nTemperature Description:")

    print(
        df[temperature_col].describe()
    )

else:

    print(
        "\nTemperature column not found."
    )


# ============================================================
# 11. TEMPERATURE TREND
# ============================================================

if date_col is not None and temperature_col is not None:

    plt.figure(
        figsize=(12, 5)
    )

    plt.plot(
        df[date_col],
        df[temperature_col]
    )

    plt.title(
        "Temperature Trend"
    )

    plt.xlabel(
        "Date"
    )

    plt.ylabel(
        "Temperature"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            RESULTS_DIR,
            "temperature_trend.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ============================================================
# 12. RAINFALL TREND
# ============================================================

if date_col is not None and rainfall_col is not None:

    plt.figure(
        figsize=(12, 5)
    )

    plt.plot(
        df[date_col],
        df[rainfall_col]
    )

    plt.title(
        "Rainfall Trend"
    )

    plt.xlabel(
        "Date"
    )

    plt.ylabel(
        "Rainfall"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            RESULTS_DIR,
            "rainfall_trend.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ============================================================
# 13. HUMIDITY VS TEMPERATURE
# ============================================================

if humidity_col is not None and temperature_col is not None:

    plt.figure(
        figsize=(8, 6)
    )

    plt.scatter(
        df[temperature_col],
        df[humidity_col]
    )

    plt.title(
        "Humidity vs Temperature"
    )

    plt.xlabel(
        "Temperature"
    )

    plt.ylabel(
        "Humidity"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            RESULTS_DIR,
            "humidity_vs_temperature.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ============================================================
# 14. WIND SPEED DISTRIBUTION
# ============================================================

if wind_col is not None:

    plt.figure(
        figsize=(8, 6)
    )

    plt.hist(
        df[wind_col],
        bins=20
    )

    plt.title(
        "Wind Speed Distribution"
    )

    plt.xlabel(
        "Wind Speed"
    )

    plt.ylabel(
        "Frequency"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            RESULTS_DIR,
            "wind_speed_distribution.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ============================================================
# 15. CORRELATION ANALYSIS
# ============================================================

available_columns = []


for col in [
    temperature_col,
    humidity_col,
    wind_col,
    rainfall_col,
    pressure_col
]:

    if col is not None:

        available_columns.append(col)


if len(available_columns) >= 2:

    correlation = df[
        available_columns
    ].corr()

    print(
        "\n========== CORRELATION MATRIX =========="
    )

    print(
        correlation
    )


    plt.figure(
        figsize=(8, 6)
    )

    sns.heatmap(
        correlation,
        annot=True
    )

    plt.title(
        "Weather Variables Correlation"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            RESULTS_DIR,
            "correlation_heatmap.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ============================================================
# 16. SAVE PREPROCESSED DATA
# ============================================================

preprocessed_file = os.path.join(
    DATA_DIR,
    "weather_preprocessed.csv"
)


df.to_csv(
    preprocessed_file,
    index=False
)


print(
    "\nPreprocessed dataset saved successfully!"
)

print(
    "Saved at:",
    preprocessed_file
)


# ============================================================
# 17. FINAL CHECK
# ============================================================

print(
    "\n========== FINAL DATASET =========="
)


print(
    "Final Dataset Shape:",
    df.shape
)


print(
    "\nMissing Values:"
)


print(
    df.isnull().sum()
)


print(
    "\nDuplicate Rows:"
)


print(
    df.duplicated().sum()
)


print(
    "\nFirst 5 Rows:"
)


print(
    df.head()
)


# ============================================================
# 18. DISPLAY SAVED RESULTS
# ============================================================

print(
    "\n========== SAVED PLOTS =========="
)


print(
    "Results folder:",
    RESULTS_DIR
)


for file in os.listdir(RESULTS_DIR):

    if file.endswith(".png"):

        print(
            "✓",
            file
        )


print(
    "\n========================================"
)

print(
    "      WEATHER ANALYSIS COMPLETED"
)

print(
    "========================================"
)
