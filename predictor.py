import pandas as pd
from prophet import Prophet

holidays = pd.concat([
    pd.DataFrame({
        'holiday': 'event',
        'ds': pd.to_datetime(['2024-12-25','2025-01-01']),
        'lower_window': 0,
        'upper_window': 1
    }),
])
def initialize_model():
    model = Prophet(holidays=holidays, holidays_prior_scale=0.05)
    model.add_seasonality(name='monthly', period=30.5, fourier_order=5)
    model.add_seasonality(name='weekly', period=7, fourier_order=3)
    model.add_country_holidays(country_name="FR")
    return model

def predict_monthly(df, nbr_of_day):
    model=initialize_model()
    model.fit(df)
    future = model.make_future_dataframe(periods=nbr_of_day)
    forecast = model.predict(future)

    return {
        "month": float(forecast['yhat'].head(nbr_of_day).sum()),
        "month_low": float(forecast['yhat_lower'].head(nbr_of_day).sum()),
        "month_up": float(forecast['yhat_upper'].head(nbr_of_day).sum())
    }

def predict_day(df):
    model = initialize_model()
    model.fit(df)
    future = model.make_future_dataframe(periods=1)
    forecast = model.predict(future)
    return {
        "day": forecast[['yhat']].iloc[-1].item(),
        "day_low": forecast[['yhat_lower']].iloc[-1].item(),
        "day_up": forecast[['yhat_upper']].iloc[-1].item()
    }