#!/usr/bin/python3
def best_score(a_dictionary):
    dict_tuple = sorted(a_dictionary.items(), 
                        key=lambda item: item[1], reverse=True)
    return dict_tuple[0][0]
