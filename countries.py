import os
import json 
import pathlib
import matplotlib.pyplot as plt
import tabulate

BASE_DIR = pathlib.Path(__file__).parent
data_path = "total.json"

save_folder = BASE_DIR.joinpath("datas")

def read_file(path : str) -> dict:
    """
        this function read a json file and convert it to a python dict
        params: path:str
        return: data:dict
    """
    if not(os.path.exists(path)):
        return {}

    with open(file=path) as f:
        data = json.load(f)

        return data


def sort_data(x:list, y:list) -> list:
    """
        this function take x and y axis and sorted by number of usage
    """
    zipped = zip(x,y)
    zipped = sorted(zipped, key= lambda each: each[1], reverse=True)
    zipped = zip(range(1, len(x)+1), zipped)
    return zipped

def convert_data_2xy(data:list):
    """
        this function take data and convert it to
        two seprate list
    """
    x = []
    y = []
    for each in data:
        
        name = ""
        # remove emojie from names
        for c in each["name"]:
            if c.isalpha() and c != "Â":
                name += c

        # truncate countries name 
        if len(name) > 6:
            name = name[:6] + "..."
        x.append(name)
        y.append(int(each["internet"].replace(",","")))

    return x ,y


def show_plot(x:list, y:list, title:str, x_label:str, y_label:str,name):
    """
        this function take x and y axis and show a plot from that data
    """
    plt.plot(x, y)

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(title)

    # plt.show()
    plt.savefig(name)

    # clear plot
    plt.clf()


data = read_file(str(BASE_DIR.joinpath(data_path)))
x,y = convert_data_2xy(data)
sorted_data = sort_data(y=y, x=x)


lenght = int(len(x)/8)
for i in range(lenght):
    show_plot(x=x[0:8], y=y[0:8] , x_label="countries ", y_label="internet users", title="internet usage based on population => by alisharify", name=save_folder.joinpath(str(i)+ ".jpg"))
    x = x[8::]
    y = y[8::]

show_plot(x=x, y=y , x_label="countries ", y_label="internet users", title="internet usage based on population => by alisharify", name=save_folder.joinpath(str(i)+ ".jpg"))




# for print rating result
# print(tabulate.tabulate(sorted_data, tablefmt="grid"))

# data sources: https://restcountries.com/v3.1/all and wiki pedia :)
