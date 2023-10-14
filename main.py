from datetime import datetime, timedelta

users = [
    {"name": "Milentiy", "Birthday": "08 May 1997"},
    {"name": "Alena", "Birthday": "07 September 1987"},
    {"name": "Dmytro", "Birthday": "18 August 1987"},
    {"name": "Milana", "Birthday": "16 December 1987"},
    {"name": "Petro", "Birthday": "15 October 1987"},
    {"name": "Olga", "Birthday": "18 October 1967"},
]

weekdays = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Next Monday": [],
}


def get_birthdays_per_week(users_list):
    current_date = datetime.now().date()
    end_of_week = current_date + timedelta(days=7)

    birthdays_exist = False

    for user in users_list:
        name = user["name"]
        birthday = datetime.strptime(user["Birthday"], "%d %B %Y")
        birthday_date = datetime(current_date.year, birthday.month, birthday.day).date()

        if current_date <= birthday_date <= end_of_week:
            day_of_week = birthday_date.strftime("%A")

            if day_of_week in ("Saturday", "Sunday"):
                day_of_week = "Monday"

            weekdays[day_of_week].append(name)
            birthdays_exist = True

    for day, names in weekdays.items():
        if names:
            print(f"{day}: {', '.join(names)}")

    if not birthdays_exist:
        print("No birthdays in the upcoming week. Be happy :)")


if __name__ == "__main__":
    get_birthdays_per_week(users)
