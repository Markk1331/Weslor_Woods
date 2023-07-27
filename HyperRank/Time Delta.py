from datetime import datetime as dt

format = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(),format) - dt.strptime(input(), format)).total_seconds())))