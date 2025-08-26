import re
from datetime import datetime
import pytz


def is_valid_email(email):
    """Validate email using regex."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def extract_valid_emails(email_list):
    """Extract only valid emails from a list."""
    return [email for email in email_list if is_valid_email(email)]



def display_current_times(timezones):
    """Display current time in given timezones."""
    utc_now = datetime.utcnow()
    print("\nCurrent Times in Different Timezones:")
    for zone in timezones:
        try:
            tz = pytz.timezone(zone)
            local_time = pytz.utc.localize(utc_now).astimezone(tz)
            print(f"{zone:30} -> {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
        except pytz.UnknownTimeZoneError:
            print(f"{zone:30} -> Invalid Timezone")



if __name__ == "__main__":

    emails = [
        "osama.alsaidi@hotmail.com",
        "invalid-email@",
        "oooo_123@gmail.co.",
        "ahmad@company",
        "user.name@domain.com"
    ]

    print("Validating Emails...\n")
    valid_emails = extract_valid_emails(emails)

    if valid_emails:
        print("Valid Emails Found:")
        for email in valid_emails:
            print(f"  - {email}")
    else:
        print("No valid emails found.")


    timezones_to_display = [
        "UTC",
        "US/Eastern",
        "Europe/London",
        "Asia/Kolkata",
        "Australia/Sydney",
        "Africa/Nairobi"
    ]

    display_current_times(timezones_to_display)
