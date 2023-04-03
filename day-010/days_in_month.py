def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # JAN..DEC

  days = month_days[month - 1] # Count from 0

  if month == 2:
    if is_leap(year):
      days += 1 # Add an extra day
      return days
    else:
      return days    
  else:
    return days
  
  
  
# Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)