from datetime import datetime, date
import time

import pandas as pd

from sender import send_whatsapp_message


def create_dataframe():
    try:
        data_df = pd.read_csv("data.csv")
        return data_df

    except Exception as e:
        print(e)
        print("Something went wrong. Birthdays dataframe not created.")
        return False


def check_for_firstday():
    try:
        data_df = create_dataframe()
        today = datetime.now()
        for i in range(data_df.shape[0]):
            today = date.today()
            first_day_of_month = date(today.year, today.month, 23)
            if today == first_day_of_month:
                title = data_df.loc[i, "title"]
                amount = data_df.loc[i, "debit per month"]
                payment_link = None
                if not pd.isna(data_df.loc[i, "payment link"]):
                    payment_link = data_df.loc[i, "payment link"]
                send_whatsapp_message(
                    title, amount, payment_link, '919031760771')
                time.sleep(3)

    except Exception as e:
        print(e)
        print("Something went wrong. Birthday check not successful.")


if __name__ == "__main__":
    check_for_firstday()
