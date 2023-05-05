def get_mem(password, sentence, type_password):
    learning = 1    # suppose it is constant
    if type_password == 'PAO':
        symbol_translation = 0
    else:
        symbol_translation = len(sentence)
    return learning/(len(sentence)/7)*len(password*(1+symbol_translation))
