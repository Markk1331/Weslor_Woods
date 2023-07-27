import calendar
mm,dd,yy = map(int,input().split())
x = calendar.weekday(yy,mm,dd)
print((calendar.day_name[x]).upper())