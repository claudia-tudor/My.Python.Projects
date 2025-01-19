minutes_tci = int(input("Please enter the number of minutes:"))
hours_tci = minutes_tci // 60 
minutesremaining_tci = minutes_tci % 60
print (f"{minutes_tci} minutes represent {hours_tci} hours and {minutesremaining_tci} minutes.")