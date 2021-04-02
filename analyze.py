
def asc_order(data):
    sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))
    return sorted_dict

def desc_order(data):
    sorted_dict = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

def print_vals(data):
    for key, val in data.items():
        print(f'{key} has a PageRank value of {val}')
