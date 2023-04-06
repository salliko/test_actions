

def recursive_summ(items: list) -> int:
    if not items:
        return 0
    return items.pop(0) + recursive_summ(items)
