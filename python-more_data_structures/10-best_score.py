#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None

    dict_tuple = sorted(a_dictionary.items(),
                        key=lambda item: item[1], reverse=True)
    return dict_tuple[0][0]
