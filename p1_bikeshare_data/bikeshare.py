import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

months = ['January', 'February', 'March', 'April', 'May', 'June']


def whitespace():
    print(' ')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    whitespace()
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('What city would you like info for? We have data for Chicago, New York, and Washington:').title()
    while city not in list(CITY_DATA.keys()):
        print('At this time we only have data for Chicago, New York, and Washington... Please try one of those cities')
        city = input('Try again!: ').title()
    whitespace()

    # get user input for month (all, january, february, ... , june)
    month = input('Would you like to filter for a certain month? We only have data from January till June!\n We will default to all months if not in range or left blank!: ').title()
    if month != 'all' and month not in months:
        month = 'all'
    whitespace()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('You also have the opportunity to filter by day of the week..\n Leaving blank will default to all: ').title()
    days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day not in days_of_the_week and day != 'all':
        day = 'all'

    print('-'*40)
    return city, month, day

city, month, day = get_filters()



def display_filters():
    print(f'Selected filters are: \n City -----> {city} \n Month -----> {month.title()} \n Day -----> {day.title()}')
    whitespace()

display_filters()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

     # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common day month... only run if not filtering by month
    if month == 'all':
        popular_month = df['month'].mode()[0]
        print(f'The most common month for travel is {months[popular_month-1]}')

    # display the most common day of week... only run if not filtering by day
    if day == 'all':
        popular_week = df['day_of_week'].mode()[0]
        print(f'The most common day of the week for travel is {popular_week}')

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    time_zone = {0:'AM', 1: 'PM'}
    if popular_hour > 12:
        popular_hour -=12
        print(f'The most common start hour for the selected filters is {popular_hour}:00{time_zone[1]}')
    else:
        print(f'The most common start hour for the selected filters is {popular_hour}:00{time_zone[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    df['Trip'] = 'From ' + df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].mode()[0]

    print(f'The most common start location is {common_start}, the most common end location is {common_end}, and the most common trip is {common_trip}\n')

    more_info = input('Are you interested in the counts for these common stations? Enter yes or no. Blank or anything else, we will assume no!').lower()

    whitespace()

    if more_info == 'yes':
        count_start = df[df['Start Station']== common_start].count()[0]
        count_end = df[df['End Station']== common_end].count()[0]
        count_trip = df[df['Trip']== common_trip].count()[0]
        print(f'Users started their trip at {common_start} {count_start} times; {common_end}, the most common end station was reached {count_end} times; {common_trip}, the most frequent trip was made {count_trip} times')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # display total travel time in seconds
    total_time_seconds = df['Trip Duration'].sum()

    #convert seconds to days, hours, minutes and seconds
    time_days = total_time_seconds // (24*3600)
    remaining_time_seconds = total_time_seconds % (24*3600)
    time_hours = remaining_time_seconds // 3600
    remaining_time_seconds %= 3600
    time_minutes = remaining_time_seconds // 60
    remaining_time_seconds %=60

    # display mean travel time and convert it to minutes and seconds
    average_travel_time = df['Trip Duration'].mean()
    average_travel_time_minutes = average_travel_time // 60
    average_travel_time %= 60

    print(f' For this dataset, the average travel time is {average_travel_time_minutes} minutes and {average_travel_time} seconds.\n \n Additionally, users spent {time_days} days, {time_hours} hours, {time_minutes} minutes and {remaining_time_seconds} seconds traveling')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df.groupby('User Type')['User Type'].count()

    print(f'Here are the counts and types for the users in {city}\n')

    for user in user_types.index:
        print(f'{user}s {user_types[user]}')

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df.groupby('Gender')['Gender'].count()

    # Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        
        print(f'\n Here are the counts by gender: {gender_types}')
        print(f'\n The youngest user was born in {recent_year} while the oldest user was born in {earliest_year}. The most common birth year is {common_year} ')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """" Displays raw data if the user requests it """
    print('\nAre you interested in seeing the raw data for your dataset?\n')
    response = input('Enter yes or no. If your input is not yes, we will assume it is a no!: ').lower()

    whitespace()
    if response == 'yes':
        number = int(input('How many rows are you looking to see?: '))
        while number < 0 or number > len(df):
            number = input(f'Please only enter a number between 0 and {len(df)}: ')
        display_data = df.head(number)
        print(display_data)
        stat1 = df[['Trip Duration', 'hour']].describe()
        print(f'\n Check out these interesting statistics: \n{stat1}\n')


def main():
    while True:
        # city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
