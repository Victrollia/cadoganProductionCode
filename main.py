# Student: Victoria Cadogan
from dataclasses import dataclass, field
import pandas as pd
import os


@dataclass
class Products:
    index: int
    name: str
    unit_price: float
    type: str


def __get_tax(self, state):
    if state == 'MA':
        return 0.0625
    elif state == 'ME':
        return 0.055
    else:  # if it's NH
        return 1


def __get_products():
    this_folder = os.path.dirname(os.path.abspath(__file__))
    file_to_open = os.path.join(this_folder, "products.xlsx")
    wb = pd.read_excel(file_to_open, header=0)
    df = pd.DataFrame(wb)
    all_items = df[['Item', 'Price', 'Type']]
    products = []
    for i in range(len(all_items)):
        products.append(all_items.iloc[i].values.tolist())
    return products


def checkout():
    j = 1
    print('ID\tItem\t\t\tPrice\t\t\tType\n')
    for i in __get_products():
        items = Products(index=j, name=i[0], unit_price=i[1], type=i[2])
        print(str(j), items.name, "\t||\t", items.unit_price, "||\t", items.type)
        j += 1
    sell = input("Enter the ID of the items you wish to buy followed by a comma:\n")


checkout()