def find_target_indices(text_array, targets):
    result_indices = []
    result_words = []
    for word in targets:
        index = text_array.find(word)
        if index != -1:
            result_indices.append(index)
            result_words.append(word)
    
    combined = [(result_indices[i], result_words[i]) for i in range(len(result_indices))]
    combined.sort()
    sorted_indices = [item[0] for item in combined]
    sorted_words = [item[1] for item in combined]

    return sorted_indices, sorted_words