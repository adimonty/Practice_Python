import json
from collections import defaultdict
from bokeh.plotting import figure, show
from bokeh.io import output_file

def load_birthday_dict_from_file(file_name):
    with open(file_name, "r") as file:
        birthday_dict = json.load(file)
    return birthday_dict

def extract_month(birthday):
    return birthday.split()[0]

def count_birthdays_by_month(birthday_dict):
    months_count = defaultdict(int)
    for birthday in birthday_dict.values():
        month = extract_month(birthday)
        months_count[month] += 1
    return months_count

def plot_histogram(months_count):
    output_file("birthday_histogram.html")
    
    months = list(months_count.keys())
    counts = list(months_count.values())
    
    p = figure(x_range=months, title="Scientists' Birthdays by Month")
    p.vbar(x=months, top=counts, width=0.5, color="blue")
    
    p.xaxis.axis_label = "Months"
    p.yaxis.axis_label = "Number of Scientists"
    
    show(p)

def main():
    file_name = "scientists_birthdays.json"
    birthday_dict = load_birthday_dict_from_file(file_name)
    months_count = count_birthdays_by_month(birthday_dict)
    
    plot_histogram(months_count)

if __name__ == "__main__":
    main()
