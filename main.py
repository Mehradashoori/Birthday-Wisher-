import datetime
import pandas
import random
import smtplib

MY_EMAIL = "rc919295@gmail.com"
PASSWORD = "1234567891013821382"

now = datetime.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today in birthdays_dict:
    letter_number = random.randint(1, 3)
    birthdays_person = birthdays_dict[today]
    with open(f"letter_templates/letter_{letter_number}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )
