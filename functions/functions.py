from utils import sum_numbers


def customer_count(n_customers: int | str = 10_000) -> dict:
    n_customers = int(n_customers)
    some_dict = {}
    for id_ in range(n_customers):
        current_sum = sum_numbers(id_)
        if current_sum in some_dict.keys():
            some_dict[current_sum] += 1
        else:
            some_dict[current_sum] = 1

    return some_dict


def customer_count_extended(n_customers: int | str = 10_000, n_first_id: int | str = 0) -> dict:

    n_customers = int(n_customers)
    assert n_first_id <= n_customers, 'Starting id supposed to be less then number of customers'
    some_dict = {}
    for id_ in range(n_first_id, n_customers):
        current_sum = sum_numbers(id_)
        if current_sum in some_dict.keys():
            some_dict[current_sum] += 1
        else:
            some_dict[current_sum] = 1

    return some_dict
