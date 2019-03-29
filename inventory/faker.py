import random
from .fake_list import (
    HEALTH_ITEM_LIST,
    FINANCE_ITEM_LIST,
)


def get_items(resource_type):
    if resource_type == 'health':
        item_list = HEALTH_ITEM_LIST
    else:
        item_list = FINANCE_ITEM_LIST

    count = random.randint(3, len(item_list))
    items = random.sample(item_list, count)

    inventories = []
    for item in items:
        inventories.append({
            'item': item,
            'quantity': random.randint(1, 100)
        })
    return inventories
