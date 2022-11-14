import model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    Task01.init(value_a, value_b)
    result = Task01.sum()
    view.view_data(result)

def button_click1():
    value_a = view.get_value()
    value_b = view.get_value()
    Task01_mult.init(value_a, value_b)
    result = Task01_mult.mult()
    view.view_data(result)


from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};temperature;{}\n'
                        .format(time, data))

def preassure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};preassure;{}\n'
                        .format(time, data))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n'
                        .format(time, data))