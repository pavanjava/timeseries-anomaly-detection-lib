from src.core.utils import LoadDataSet
from src.core.AverageMethod import MovingAverage


def compute():
    moving_avg = MovingAverage()
    df = LoadDataSet().load(file='/Users/pavanmantha/Pavans/MTech/Sem-4/dissertation-code/power_consumption.txt', delimiter=';')

    df["DateTime"] = df['Date']+" "+df["Time"]

    df = moving_avg.initialize(df=df, datetime_column="DateTime", target_column="Global_active_power")

    print("Target Data Frame processing complete")

    anomalies, ma, threshold = moving_avg.compute_anomalies(df=df, target_column="Global_active_power")

    print("anomalies, ma, threshold computed")

    moving_avg.plot_anomalies(df=df,target_column="Global_active_power", anomalies=anomalies, ma=ma, threshold=threshold,
                              anomalie_label_name="Anomalies", mvng_avg_label_name="Moving Average",
                              data_label_name="Power consumption data", threshold_label_name="Threshold", image_name="anomaly",
                              xlabel_name="Date", ylabel_name="power consumption",plot_title_name="Anomaly Detection")

    print("anomauly detection complete")


compute()