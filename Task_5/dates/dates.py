from datetime import datetime


def calc_date():

    average_living_period = 71

    day = int(input("Enter your day of birth: "))
    month = int(input("Enter the month of you birth: "))
    year = int(input("Enter the year of you birth: "))

    date_of_birth = datetime(year, month, day)
    current_date = datetime.now()
    has_lived = current_date - date_of_birth
    print("Вы прожили: {} дней,  {} часов, {} минут".format(has_lived.days, has_lived.seconds // 3600,
                                                            has_lived.seconds // 60))

    year_of_death = year + average_living_period
    date_of_death = datetime(year_of_death, month, day)
    has_left = date_of_death - current_date
    print("Вам осталось: {} дней,  {} часов, {} минут".format(has_left.days, has_left.seconds // 3600,
                                                              has_left.seconds // 60))


calc_date()
