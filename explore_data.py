try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
except ImportError as e:
    print(f"Error: Missing package - {e}")
    print("Please install required packages using:")
    print("pip install pandas matplotlib seaborn")
    exit(1)

try:
    # Load the dataset
    df = pd.read_csv("Crop_recommendation.csv")
except FileNotFoundError:
    print("Error: Cannot find 'Crop_recommendation.csv'")
    print("Make sure the file is in the same directory as this script")
    exit(1)

try:
    # Print basic information
    print("\nDataset Info:")
    print(df.info())

    print("\nBasic Statistics:")
    print(df.describe())

    # Count of crops
    print("\nCrop Distribution:")
    print(df['label'].value_counts())

    # Create visualizations
    plt.figure(figsize=(12, 6))

    # NPK Distribution for Rice
    rice_data = df[df['label'] == 'rice']
    plt.subplot(131)
    sns.boxplot(data=rice_data[['N', 'P', 'K']])
    plt.title('NPK Distribution for Rice')

    # Temperature and Humidity for Rice
    plt.subplot(132)
    sns.scatterplot(data=rice_data, x='temperature', y='humidity')
    plt.title('Temperature vs Humidity for Rice')

    # pH and Rainfall for Rice
    plt.subplot(133)
    sns.scatterplot(data=rice_data, x='ph', y='rainfall')
    plt.title('pH vs Rainfall for Rice')

    plt.tight_layout()
    plt.show()

    # Save insights
    with open('rice_insights.txt', 'w') as f:
        f.write("Rice Cultivation Insights:\n\n")
        f.write(f"Average NPK values: {rice_data[['N', 'P', 'K']].mean().to_dict()}\n")
        f.write(f"Optimal pH range: {rice_data['ph'].min():.2f} - {rice_data['ph'].max():.2f}\n")
        f.write(f"Suitable temperature range: {rice_data['temperature'].min():.2f} - {rice_data['temperature'].max():.2f}°C\n")
        f.write(f"Required rainfall range: {rice_data['rainfall'].min():.2f} - {rice_data['rainfall'].max():.2f}mm\n")

except Exception as e:
    print(f"An error occurred: {str(e)}")
    exit(1)