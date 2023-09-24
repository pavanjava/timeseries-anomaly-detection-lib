import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pd.set_option('mode.chained_assignment', None)


class MovingAverage:

    def initialize(self, df: pd.DataFrame, datetime_column=None, target_column=None):
        """Load time series data & process the data frame"""
        project_data = df
        project_data['timestamp'] = pd.to_datetime(project_data[datetime_column], format='%d/%m/%Y %H:%M:%S')
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

    def plot_anomalies(self, df, anomalies, ma, threshold, data_label_name, anomalie_label_name, mvng_avg_label_name, threshold_label_name, plot_title_name, xlabel_name, ylabel_name, image_name, target_column=None):
        # Plot the temperature readings and the anomalies
        plt.subplots(figsize=(14, 10))  # MODIFICATION, inserted

        plt.plot(df['timestamp'], df[target_column], color='yellow', label=data_label_name)
        plt.scatter(anomalies['timestamp'], anomalies[target_column], color='red', label=anomalie_label_name)
        plt.plot(df['timestamp'], ma, color='green', label=mvng_avg_label_name)
        plt.fill_between(df['timestamp'], ma - threshold, ma + threshold, color='gray', alpha=0.2, label=threshold_label_name)

        plt.legend()
        plt.title(plot_title_name)
        plt.xlabel(xlabel_name)
        plt.ylabel(ylabel_name)
        plt.grid()
        plt.savefig(image_name)
        plt.show()
