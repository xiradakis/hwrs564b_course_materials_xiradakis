## This script contains example functions for training and running an auto-regressive model for streamflow forecasting

from statsmodels.tsa.ar_model import AutoReg


def make_5day_forecast_ar(fitted_result, data, forecast_date, n_days=5):
    """
    Recursive AR forecast starting on forecast_date.
    Each predicted log-flow is fed back as input for the next day.
    Returns DataFrame with Forecast_cfs indexed by date.
    """
    params   = fitted_result.params
    ar_order = len(params) - 1
    history  = list(data['log_flow'].values[-ar_order:])

    log_forecasts = []
    for _ in range(n_days):
        next_val = params[0] + sum(params[i + 1] * history[-(i + 1)] for i in range(ar_order))
        log_forecasts.append(next_val)
        history.append(next_val)

    dates = pd.date_range(start=forecast_date, periods=n_days, freq='D')
    return pd.DataFrame({'Forecast_cfs': np.exp(np.array(log_forecasts)) - 1}, index=dates)


def fit_ar_model(train, ar_order):
     """Fit an auto-regressive model of specified order to the training data.
        Returns the fitted model result object."""
     
     return AutoReg(train['log_flow'], lags=ar_order, old_names=False).fit()
