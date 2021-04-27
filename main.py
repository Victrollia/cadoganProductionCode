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
    if purchase.unit_price < 0:
        print("We do not accept refunds!")
        return ''
    elif purchase.type.lower() == 'clothing':
        if purchase.unit_price > 100 and state.upper() == 'ME':
            return round(purchase.unit_price + (purchase.unit_price * __get_tax(state)), 2)
        elif purchase.unit_price > 175 and state.upper() == 'MA':
            return round(purchase.unit_price + (purchase.unit_price * __get_tax(state)), 2)
        else:
            return purchase.unit_price
    elif purchase.type.lower() == 'wic eligible':
        return purchase.unit_price
    elif state.upper() not in ('MA', 'ME', 'NH'):
        print("Please enter MA, ME or NH")
        return ''
    else:
        return round(purchase.unit_price + (purchase.unit_price * __get_tax(state)), 2)
