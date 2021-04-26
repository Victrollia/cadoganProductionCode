# Student: Victoria Cadogan
from dataclasses import dataclass, field


@dataclass
class Products:
    name: str
    unit_price: float
    type: str


def __get_tax(state):
    if state.upper() == 'MA':
        return 0.0625
    elif state.upper() == 'ME':
        return 0.055
    else:
        return 1


def checkout(purchase: Products, state):
    if purchase.type.lower() == 'wic eligible' or purchase.type.lower() == 'clothing':
        total = purchase.unit_price
        return total
    elif state.upper() not in ('MA', 'ME', 'NH'):
        print("Please enter MA, ME or NH")
        return ''
    else:
        total = round(purchase.unit_price + (purchase.unit_price * __get_tax(state)), 2)
        return total
