import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = str(input("Would you like to see data for Chicago, New York city, or Washington?\n")).lower()
            break
        except ValueError:
            print('That\'s not a valid value!')
        except KeyboardInterrupt:
            print('\nNo Input taken')
            break
        finally:
            print('\nAttempted Input\n')

    if city not in CITY_DATA:
        print('City name you typed is not on the list above. Please try again.\n')
        return get_filters()

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        try:
            month = str(input("Which month? all, january, february, march, april, may, or june?\n")).lower()
            break
        except ValueError:
            print('That\'s not a valid value!')
        except KeyboardInterrupt:
            print('\nNo Input taken')
            break
        finally:
            print('\nAttempted Input\n')

    if month not in months:
        print('Month you typed is not on the list above. Please try again.\n')
        return get_filters()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        try:
            day = str(input("Which day? Please type your response as a string type or type all for no filter.\n")).lower()
            break
        except ValueError:
            print('That\'s not a valid value!')
        except KeyboardInterrupt:
            print('\nNo Input taken')
            break
        finally:
            print('\nAttempted Input\n')

    if day not in days:
        print('Day of week you typed is not valid day. Please try again.\n')
        return get_filters()

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':

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

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:{}'.format(common_month))

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of week :{}'.format(common_day_of_week))

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('Most common start hour :{}'.format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station =  df['Start Station'].mode()[0]
    print('Most commonly used start station :{}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station =  df['End Station'].mode()[0]
    print('Most commonly used end station :{}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    frequent_start_end_station = df.groupby('Start Station')['End Station'].value_counts().idxmax()

    print('Most frequent combination of start and end station:{}'.format(frequent_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time :{} sec'.format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time :{} sec'.format(round(mean_travel_time,1)))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city, df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count for each each user types:{}'.format(user_types))

    if city != 'washington':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print('Count gender:{}'.format(gender))
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        print('Earliest birth year:{}'.format(int(earliest)))
        most_recent = df['Birth Year'].max()
        print('Most recent birth year:{}'.format(int(most_recent)))
        most_common_year = df['Birth Year'].mode()[0]
        print('Most common birth year:{}'.format(int(most_common_year)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Your docstring here """
    i = 0
    raw = input("Would you like to view individual trip data?Type 'yes' or 'no.\n").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[0+i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Would you like to view individual trip data?Type 'yes' or 'no.\n").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city, df)
        display_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() == 'no':
            break
        else:
            while restart.lower() != 'no':
                if restart.lower() == 'yes':
                    break
                else:
                    print('This is not valid input. Please try again.\n')
                    restart = input('\nWould you like to restart? Enter yes or no.\n')
                    if restart.lower() == 'no':
                        return None



if __name__ == "__main__":
	main()
