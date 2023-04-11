from src.core.utils import LoadDataSet
from src.core.AverageMethod import MovingAverage


def compute():
    moving_avg = MovingAverage()
    df = LoadDataSet().load(file='/Users/pavanmantha/Pavans/MTech/Sem-4/dissertation-code/power_consumption.txt', delimiter=';')

    df["DateTime"] = df['Date']+" "+df["Time"]

    df = moving_avg.load_data(df=df, datetime_column="DateTime", target_column="Global_active_power")

    print("Target Data Frame processing complete")

    anomalies, ma, threshold = moving_avg.compute_anomalies(df=df, target_column="Global_active_power")

    print("anomalies, ma, threshold computed")

    moving_avg.plot_anomalies(df=df,target_column="Global_active_power", anomalies=anomalies, ma=ma, threshold=threshold)

    print("anomauly detection complete")

compute()