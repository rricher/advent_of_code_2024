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


def order_pages(orders, pages):
    incorrect = []
    for page in pages:
        # print(page)
        out_of_order = False
        for i in range(len(page)):
            if out_of_order:
                break
            for j in range(i + 1, len(page)):
                if page[j] in orders:
                    if page[i] in orders[page[j]]:
                        incorrect.append(page)
                        out_of_order = True
                        break
    return incorrect


def sort_incorrect(orders, incorrect):
    correct = []
    # print(orders)
    for page in incorrect:
        # processed = []
        i = 0
        # print(page)
        while i < len(page):
            # print(i)
            j = i + 1
            while j < len(page):
                if page[j] not in orders:
                    j += 1
                    continue
                if page[i] in orders[page[j]]:
                    # print(f"moving {page[j]} before {page[i]}: {page}")
                    num = page.pop(j)
                    page.insert(i, num)
                    i -= 1
                    # print(page)
                    break
                j += 1
            i += 1
        correct.append(page)
    return correct


def get_middles(correct):
    middles = 0
    for page in correct:
        middles += int(page[int(len(page) / 2)])
    print(middles)


def main() -> None:
    rules = get_input("./input.txt")
    orders, pages = seperate_rules(rules)
    incorrect = order_pages(orders, pages)
    correct = sort_incorrect(orders, incorrect)
    get_middles(correct)


if __name__ == "__main__":
    main()
