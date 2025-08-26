import re
from datetime import datetime, timedelta
import pytz


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$'
    return re.match(pattern, email) is not None


def extract_dates(text):
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(pattern, text)


def time_until_next_birthday(birthdate_str):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

   
    next_birthday = birthdate.replace(year=today.year)

    
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    delta = next_birthday - today
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes = remainder // 60

    return days, hours, minutes


def convert_timezone(time_str, from_tz, to_tz):
    fmt = "%Y-%m-%d %H:%M:%S"
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)

    naive_dt = datetime.strptime(time_str, fmt)
    from_dt = from_timezone.localize(naive_dt)
    to_dt = from_dt.astimezone(to_timezone)

    return to_dt.strftime(fmt)

def parse_log_timestamps(log):
    pattern = r'\[(\d{2})/(\w{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) \+\d{4}\]'
    month_map = {
        'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
        'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
        'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
    }

    timestamps = []
    for match in re.findall(pattern, log):
        day, mon_abbr, year, hour, minute, second = match
        month = month_map[mon_abbr]
        date_str = f"{year}-{month}-{day} {hour}:{minute}:{second}"

        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        timestamps.append(dt.strftime("%Y-%m-%d %H:%M:%S"))

    return timestamps


if __name__ == "__main__":
    print("Exercise 1 - Email Validation:")
    print(validate_email("test.email@example.com"))  
    print(validate_email("bad-email@com"))          

    print("\nExercise 2 - Extract Dates:")
    sample_text = "We have meetings on 26-08-2025, 27/08/2025 and some other day 01-01-2023."
    print(extract_dates(sample_text))

    print("\nExercise 3 - Time Until Next Birthday:")
    birthdate_input = "1990-09-15"
    days, hours, minutes = time_until_next_birthday(birthdate_input)
    print(f"Time until next birthday from {birthdate_input}: {days} days, {hours} hours, {minutes} minutes")

    print("\nExercise 4 - Timezone Converter:")
    time_str = "2023-10-05 14:30:00"
    from_timezone = "US/Eastern"
    to_timezone = "UTC"
    converted_time = convert_timezone(time_str, from_timezone, to_timezone)
    print(f"{time_str} in {from_timezone} is {converted_time} in {to_timezone}")

    print("\nExercise 5 - Log Timestamp Extraction:")
    log_sample = "[26/Aug/2025:12:30:45 +0000] GET /index.html [25/Dec/2024:08:15:00 +0000]"
    print(parse_log_timestamps(log_sample))
