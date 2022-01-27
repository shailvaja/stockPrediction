import data
from datetime import date
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def get_data():
    dt = date(2022, 1,6)
    d = data.Data(dt)
    print(d.get_data())



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
