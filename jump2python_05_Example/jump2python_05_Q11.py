import time
year = time.strftime('%Y')
monthday = time.strftime('%x')[:5]
now = time.strftime('%X')                      
print(year + '/' + monthday + ' ' + now)