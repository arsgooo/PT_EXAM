def add_good(goods, name, price):
    if isinstance(name, str) and isinstance(price, (int, float)):
        goods[name] = price
        return True
    else:
        raise TypeError("Invalid data type")

def remove_good(goods, name):
    if name in goods:
        removed_good = goods.pop(name)
        return goods, removed_good
    else:
        raise ValueError(f"The good '{name}' is not found")

def get_good(goods, name):
    if name in goods:
        return (name, goods[name])
    else:
        raise ValueError(f"The good '{name}' is not found")

def get_goods_amount(goods):
    return len(goods)

def get_total_cost(goods):
    total_cost = sum(goods.values())
    return total_cost
