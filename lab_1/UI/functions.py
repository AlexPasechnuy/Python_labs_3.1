def print_arr(arr):
    number = 1
    for rec in arr:
        print(number, ". ", rec.to_string())
        number+=1