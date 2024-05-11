def count_word_freq(word_list):

    final_dict = {}
    for item in word_list:
        if item in final_dict.keys():
            final_dict[item] += 1
        else:
            final_dict[item] = 1
    
    return final_dict

print(count_word_freq(['apple', 'orange', 'banana', 'apple', 'orange', 'apple']))
        