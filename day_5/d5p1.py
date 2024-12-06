import sys

sys.path.insert(0, "C:/Users/ryan/Projects/advent_of_code")

from read_file import get_input


def seperate_rules(rules: list[str]) -> tuple[dict, list]:
    switch = False
    orders = {}
    pages = []
    for rule in rules:
        if not switch:
            if not rule:
                switch = True
            else:
                first, after = rule.split("|")
                if first not in orders:
                    orders[first] = set()
                orders[first].add(after)
        else:
            pages.append(rule.split(","))
    # print(orders)
    return orders, pages


def order_pages(order, pages):
    middles = 0
    for page in pages:
        # print(page)
        out_of_order = False
        for i in range(len(page)):
            if out_of_order:
                break
            for j in range(i + 1, len(page)):
                if page[j] in order:
                    if page[i] in order[page[j]]:
                        # print(page[i], page[j], order[page[j]])
                        out_of_order = True
                        break
        if not out_of_order:
            # print(page)
            middles += int(page[int(len(page) / 2)])
    print(middles)


def main() -> None:
    rules = get_input("./input.txt")
    orders, pages = seperate_rules(rules)
    order_pages(orders, pages)


if __name__ == "__main__":
    main()
