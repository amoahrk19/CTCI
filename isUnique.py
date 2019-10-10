def isunique(str):
    str_dict = {}
    all_u = False
    for key in str:
        if key in str_dict.keys():
            all_u = False
            break
        else:
            str_dict[key] = 1
            all_u = True
    print(all_u)

isunique("aasdayhdhkag")
