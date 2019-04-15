import time
import pandas as pd
#import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
print('Specify a city, month and day separated by commas')
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! \n Specify a city, month and day separated by commas')

    cities = ['chicago', 'new york city', 'washington']
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Specify a city: ').lower()
    while city not in cities:
        city = input('city is not in our database. You can select between {chicago, new york city or washington.\n Specify a city: ').lower()


    # get user input for month (all, january, february, ... , june)
    month = input('Specify a month. Use all to apply no filter: ').lower()
    while month not in months:
        print('month is not in our database. You can choose from january to june')
        month = input('Specify a month. Use all to apply no filter: ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Specify a day of week. Use ''all'' to apply no filter: ').lower()
    while day not in days:
        print('You have to write the complete name, lowercase. Please retry')
        day = input('Specify a day of week. Use ''all'' to apply no filter: ').lower()

    print('/n Your filter selection was: ', city, ', month: ', month, ', day: ', day)
    print('-'*40)
    return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    if city == 'washington':
        df['Gender'] = 'NaN'
        df['Birth Year'] = 'NaN'

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # display the most common day of week
    df['weekday'] = df['Start Time'].dt.weekday_name
    popular_day = df['weekday'].mode()[0]
    print('Most Frequent Day:', popular_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', popular_start)

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', popular_end)

    # display most frequent combination of start station and end station trip
    popular_station = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('Most Commonly Used Star End Station:', popular_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    total_time = (df['End Time'] - df['Start Time']).sum()

    print('Total Travel Time:', total_time)

    # display mean travel time

    mean_time = (df['End Time'] - df['Start Time']).mean()

    print('Mean Travel Time:', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = pd.value_counts(df['User Type'])
    print(user_types)

    # Display counts of gender

    gender = pd.value_counts(df['Gender'])
    print(gender)

    # Display earliest, most recent, and most common year of birth

        # extract month and day of week from Start Time to create new columns
    df['month'] = df['Birth Year']

    common_year = df['month'].mode()
    print('\nMost Frequent User Birth Year:', common_year)

    latest_year = df['month'].max()
    print('\nMost Recent User Birth Year:', latest_year)

    earliest_year = df['month'].min()
    print('\nMost Earlier User Birth Year:', earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_data = input('\nWould you like to see the first 5 lines of data? Enter yes or no:').lower()
        if see_data != 'yes':
           restart = input('\nWould you like to restart? Enter yes or no.\n')
           if restart.lower() != 'yes':
               break
        while True:
            i = 0
            print(df.iloc[i:i+5])
            i += 5
            more_data = input('Would you like to see the next 5 lines? Enter yes or no: ').lower()
            if more_data != 'yes':
                break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
