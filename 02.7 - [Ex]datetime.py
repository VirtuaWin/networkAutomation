import datetime

x = datetime.datetime.now()
y = str(x)
print(y)
w = type(y)
print(w)
print(x.strftime('%d-%m-%Y_%X'))
print(datetime.datetime.now().strftime('%d-%m-%Y_%X'))
