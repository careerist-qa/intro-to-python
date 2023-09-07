def greeting(name):
    print(f"Hello, {name}!")


def name_starts_with_t(name):
    if name[0:1] in 'Tt':
        return True
    else:
        return False


def process_names(name_list):
    for name in name_list:
        if name_starts_with_t(name):
            greeting(name)


names = ["Joseph", "Tom", "Kelly"]
process_names(names)

# This will only greet Tom