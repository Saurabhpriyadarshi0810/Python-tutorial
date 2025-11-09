def print_list(list,idx = 0):
    if idx == len(list):
        return
    else:
        print(list[idx])
        print_list(list,idx+1)
        




cities = ["hajipur","ara","bhagalpur","nayagao","patna"]
print_list(cities)
