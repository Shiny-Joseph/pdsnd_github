import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv' }
MONTH_NUMBER = { '01': 'january','02': 'february','03': 'march','04': 'april','05': 'may','06':'june' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True : 
            city = input ("CITY NAME : ").lower()
            if city in ("chicago","new york city","washington"):
                break
            else:
                print("please enter correct name of the city as chicago / new york city / washington!")
                # get user input for month (all, january, february, ... , june)
    while True : 
            month = input("Name of the Month: ").lower()
            if month in ("all","january","february","march","april","may","june","july","august","september","october","november","december"):
                break 
            else:
                print("please enter correct name of the month like january ,february..etc or all.. !")
             # get user input for day of week (all, monday, tuesday, ... sunday)
    while True : 
            day = input("Day of the Week: ").lower()
            if day in ("all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"):
                break
            else:
                print("please enter correct name of the day like monday, tuesday...etc!")   
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
        df - Pandas DataFrame containing city data filtered by month and day """
        
    df=pd.read_csv(r"\\SEGOTN15463\Self-service Reporting\Region Europe - Business Control and Operations\Shiny\Python\all-project-files/"+CITY_DATA[city])
    
    if month != "all":
        df["Name of the month"] = pd.to_datetime(df['Start Time']).dt.strftime("%B").str.lower()
        df=df[df["Name of the month"]==month]
        
    if day != "all":
        df["Day of the Week"] = pd.to_datetime(df['Start Time']).dt.strftime("%A").str.lower()
        df=df[df["Day of the Week"]==day]
        
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df["month"] = pd.to_datetime(df['Start Time']).dt.strftime("%B").str.lower()
    common_month = df['month'].mode()

    # display the most common day of week
    df["day"] = pd.to_datetime(df['Start Time']).dt.strftime("%A").str.lower()
    common_day = df['day'].mode()

    # display the most common start hour
    df["hour"] = pd.to_datetime(df['Start Time']).dt.strftime("%H").str.lower()
    common_hour = df['hour'].mode()
    print("most common month is "+ common_month.iloc[0] )
    print("most common Day is "+ common_day.iloc[0])
    print("Most common time is " + common_hour.iloc[0]+" hrs")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most common start station is :  " + df["Start Station"].mode().iloc[0])

    # display most commonly used end station
    print("Most common end station is :  " + df["End Station"].mode().iloc[0])

    # display most frequent combination of start station and end station trip
    df["full trip"]="From "+df["Start Station"]+" to "+df["End Station"]
    print("Most common trip is :  " + df["full trip"].mode().iloc[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Travel time is : "+ str(sum(df["Trip Duration"]/3600)))
    # display mean travel time
    print("Mean of Total Travel time is : "+ str(df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    df["User Type"]=df["User Type"].fillna("No User Type Found")
    ct=df[["User Type","Trip Duration"]].groupby("User Type").agg("count").reset_index().rename(columns={"Trip Duration" : "Count of User type"})
    print(ct.to_string(index=False))
    # Display counts of gender
    if city!="washington":
        
        df["Gender"]=df["Gender"].fillna("Gender not disclosed")
        gt=df[["Gender","Trip Duration"]].groupby("Gender").agg("count").reset_index().rename(columns={"Trip Duration" : "Count of Gender Types"})
        print(gt.to_string(index=False))

    # Display earliest, most recent, and most common year of birth
        print("Earliest Year of Birth is: " + str(min(df["Birth Year"])))
        print(" The Most Recent Year of Birth is: " + str(max(df["Birth Year"])))
        print(" The Most common Year of Birth is: " + str(df["Birth Year"].mode().iloc[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):

    """ Printing raw data based on customer rquirement """

    display = input("Would you like to view 5 rows of individual trip data? Enter y/n?\n")
    if display.lower() =='y':
        start_loc = 0
        while True:
            print(df.iloc[start_loc:start_loc+5].reset_index(drop=True))
            start_loc += 5
            display = input("Do you wish to continue? Enter y/n?\n").lower()
            if display != 'y':
                break   

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        view_data(df)
        restart = input('\nWould you like to restart? Enter y/n.\n')
        if restart.lower() != 'y':
           break

if __name__ == "__main__":
	main()

