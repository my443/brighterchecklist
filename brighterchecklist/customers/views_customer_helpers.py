import datetime

def get_days_until_expiry(expiry_date: datetime) -> int:
    days_until_expiry = (expiry_date - datetime.date.today()).days

    return days_until_expiry
