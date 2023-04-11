import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class MovingAverage:
    def load_data(self, df: pd.DataFrame, datetime_column=None, target_column=None):
        """Load time series data & process the data frame"""
        project_data = df
        project_data['timestamp'] = pd.to_datetime(project_data[datetime_column])
        project_data[target_column] = pd.to_numeric(project_data[target_column], errors='coerce')
        project_data = project_data[["timestamp", target_column]]
        project_data.fillna(value=project_data[target_column].mean(), inplace=True)
        project_data.isna().sum()
        project_data.info()
        return project_data

    def compute_anomalies(self, df, target_column=None):
        # Calculate the moving average of the temperature readings
        window_size = 200  # MODIFICATION, original was 50
        ma = df[target_column].rolling(window_size).mean()

        # Calculate the deviation from the moving average
        deviation = df[target_column] - ma

        # Calculate the standard deviation of the deviation
        std_deviation = deviation.rolling(window_size).std()

        # Calculate the threshold for anomaly detection
        threshold = 3 * std_deviation

        # Detect anomalies based on deviations from the moving average
        anomalies = df[deviation.abs() > threshold]
        return anomalies, ma, threshold

    def plot_anomalies(self, df, anomalies, ma, threshold, target_column=None):
        # Plot the temperature readings and the anomalies
        plt.subplots(figsize=(14, 10))  # MODIFICATION, inserted
        plt.plot(df['timestamp'], df[target_column], color='blue', label='Power Consumption Readings')
        plt.scatter(anomalies['timestamp'], anomalies[target_column], color='red', label='Anomalies')
        plt.plot(df['timestamp'], ma, color='green', label='Moving Average')
        plt.fill_between(df['timestamp'], ma - threshold, ma + threshold, color='gray', alpha=0.2, label='Threshold')
        plt.legend()
        plt.title('Power consumption Anomaly Detection')
        plt.xlabel('Date')
        plt.ylabel('Consumption ')
        plt.grid()
        plt.savefig("moving_avg_anomaly_plot.png")
        plt.show()
