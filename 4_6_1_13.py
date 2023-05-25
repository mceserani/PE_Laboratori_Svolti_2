""" Count the occurrences of a weekday in a year """

from calendar import Calendar

class MyCalendar(Calendar):
    """ Subclass of Calendar """

    def count_weekday_in_year(self, year, weekday):
        """ Return the number of occurrences of weekday in year """
        count = 0
        for month in range(1, 13):
            for week in self.monthdays2calendar(year, month):
                for day, wday in week:
                    if wday == weekday and day != 0:
                        count += 1
        return count

# Create an instance of MyCalendar
my_calendar = MyCalendar()

# Example input
year = 2019
weekday = 0

# Call the count_weekday_in_year method to count the occurrences
result = my_calendar.count_weekday_in_year(year, weekday)

# Print the result
print(result)
