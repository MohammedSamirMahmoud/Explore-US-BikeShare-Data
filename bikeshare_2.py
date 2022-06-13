import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('#'*50)
    print('Welcome to US Bikeshare data analsys - let\'s explore moe about this data\n')
    print('#'*50)
    #print('Hello! Let\'s explore some US bikeshare data!')

    # Initializing empty variables for city,month , day
    city = ''
    month = ''
    day = ''
    #print('\n')
    print('\nWe are analyzing data from 3 cities in US please choose from them\n')
    print('List of Citis --> [chicago , new york city , washington]\n')
    print('#'*50)
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        'Checking Correctness for City Input'
        try:
            print('\nPlease type the city name that you want to analyze\n')
            print('Available Citites to analyze --> [chicago , new york city , washington]\n')
            city = input().lower().strip() # handling capitalization & spaces
        except:
            print('\nSorry, Your input isn\'t correct, please make sure it matches our list\n')
            continue
        if city not in CITY_DATA.keys():
            print('*'*50)
            print('Sorry, Your input isn\'t correct, please make sure it matches our list\n')
            print('*'*50)
            # No Break because input isn't correct!
        else:
            print("\nYou are now investigating data from US Bikeshare - {} city , to change your choice please restart the program.\n".format(city.title()))
            print('#'*50)
            # Correct input then we can break the loop
            break

    # get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    while True:
        'Checking Correctness for Month Input'
        print('\nAvailable months to analyze [january,february,march,april,may,june, or all]\n')
        print('Please Choose the month name you want to analyze from the list , type all to analyze data from all months\n')
        month = input().lower()
        if month in MONTH_DATA.keys():
            print('\nWelcome you are now analyzing month {} - for US BikeShare {} city.\n'.format(month.title(),(city.title())))
            print('#'*50)
            break
        else:
            print('*'*50)
            print('Invalid choice, please choose a month from the list or type the month name correctly\n')
            print('*'*50)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS_DATA = {'saturday': 1, 'sunday': 2, 'monday': 3, 'tuesday': 4, 'wednesday': 5, 'thursday': 6, 'friday': 7, 'all':8}
    while True:
        'Checking Correctness for Day Input'
        print('\nAvailable days to analyze [saturday,sunday,monday,tuesday,wednesday,thursday,friday, or all]\n')
        print('Please Choose the day name you want to analyze from the list , type all to analyze data from all days\n')
        day = input().lower()
        if day in DAYS_DATA.keys():
            print('#'*100)
            print('\nWelcome you are now analyzing Day {} - Mnth {} -  for US BikeShare {} City.\n'.format(day.title(),month.title(),city.title()))
            print('#'*100)
            break
        else:
            print('*'*50)
            print('Invalid choice, please choose a day from the list or type the day name correctly\n')
            print('*'*50)

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

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

    return df,city,month,day

def check_data_head(df):
    while True:
        'Checking if user wants to see Sample of Data'
        print('Do you want to check sample data before proceeding? please answer by yes or no\n')
        answer = input().lower()
        if answer == 'yes':
            print('-*-' * 30)
            print(df.head(5))
            print('-*-' * 30)
            start_loc = 0 
            view_more = 'yes'
            while view_more.lower().strip() == 'yes':
                print('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
                view_more = input().lower()
                start_loc = start_loc + 5
                print('-*-' * 30)
                print(df[start_loc:start_loc +5])
                print('-*-' * 30)
            break


def time_stats(df,city,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = {'1':'January', '2':'February', '3':'March', '4':'April', '5':'May', '6':'June'}

    # display the most common month
    if month == 'all':
        most_common_month = df['month'].mode()[0]
        month_name = months[str(most_common_month)]
        print('The most common month in city --> {} is : {} '.format(city,most_common_month)) 
    else:
        most_common_month = month
        month_name = months[str(most_common_month)]
        print('You are actually filtering by month, hence the most common one is the one you filtered which is : {} , Month number {}'.format(month_name,most_common_month))
    # display the most common day of week
    if day == 'all':
        most_common_day = df['day_of_week'].mode()[0]
        print('The most common day in month number {} which is month --> {} is : {}'.format(most_common_month,month_name,most_common_day)) 
    else:
        most_common_day = day
        print('You are actually filtering by day, hence the most common one is the one you filtered which is : ', most_common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour during month: {} which is month {} - day: {} - is hour number: {} \n'.format(most_common_month,month_name,most_common_day,most_common_hour))

    print('#'*40)
    print('NEXT Results will be analyzed based on Selected filters which are: \n')
    print('City: ',city)
    print('\nMonth Name: ',month)
    print('\nDay Name: ',day)
    print('#'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most Common Start station During the selected time is:  {}'.format(most_common_start_station))

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most Common End station During the selected time is:  {}'.format(most_common_end_station))

    # display most frequent combination of start station and end station trip
    df['start to end stations'] = df['Start Station'] + " to " + df['End Station']
    most_common_start_end_station = df['start to end stations'].mode()[0]
    print('The most Common Start To End Station During the selected time is:  {}'.format(most_common_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    # Getting time in hours, minutes, seconds
    minutes, seconds = divmod(total_travel_time, 60)
    hours,minutes = divmod(minutes, 60)
    days,hours = divmod(hours, 24)
    print('#'*40)
    print("The Total Trip Duration is : {} days -  {} hours - {} minutes - and {} seconds".format(days,hours,minutes,seconds))
    # display mean travel time
    
    average_travel_time = df['Trip Duration'].mean()
    minutes, seconds = divmod(average_travel_time, 60)
    hours,minutes = divmod(minutes, 60)
    print('#'*40)
    print("The Average Trip Duration is : {} hours {} minutes and {} seconds".format(hours,minutes,seconds))
    print('#'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_types = df['User Type'].value_counts()
    print('Users Types are:\n',users_types)

    # Display counts of gender
    if city in ['chicago','new york city']:
        users_gender_count = df['Gender'].value_counts()
        print('#'*30)
        print('\nUsers Gender Statistics is: \n',users_gender_count)
        print('#'*30)

    # Display earliest, most recent, and most common year of birth
        earliest_b_year = int(df['Birth Year'].min())
        most_recent_b_year =int(df['Birth Year'].max())
        most_common_b_year = int(df['Birth Year'].mode()[0])

        print('\nEarliest Birth Year is : ',earliest_b_year)
        print('\nMost Recent Birth Year is : ',most_recent_b_year)
        print('\nMost Common Birth Year is : ',most_common_b_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    




def main():
    while True:
        city, month, day = get_filters()
        df,city,month,day = load_data(city, month, day)
        check_data_head(df)
        time_stats(df,city,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
