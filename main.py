from datetime import datetime, timezone

expectedformat = '%Y-%m-%d %H:%M:%S'

print("Format date and time as YYYY-MM-DD HH:MM:SS\n")


dt = input("Enter a Date and time:\n").strip()

try:
    dt = datetime.strptime(dt, expectedformat)

except ValueError:
    print('')
    print("Invalid Datetime")
    print('')

if dt.year is not None:

    if dt.year < 1900:
        print('')
        print("Year must be greater than 1900")
        print('')
        
    elif dt.year > 2020:
        print('')
        print("Year must be less than 2020")
        print('')
        
    else:
        print('')
        print("Date and time are valid")
        print('')

else:
    print(dt+ " is valid")

print("Converting to UTC...")
print('')
dtu  = dt.replace(tzinfo=timezone.utc).timestamp()

print("UCT: "+str(dtu) + " seconds")
print('')
    
