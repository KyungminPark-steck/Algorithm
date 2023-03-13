def solution(new_id):
    new_id = new_id.lower()

    available_list = ['-', '_', '.']
    new_id_1 = []
    for s in new_id:
        if s.isalpha() or s.isdigit()or s in available_list: new_id_1.append(s)
    new_id = ''.join(new_id_1)
    #.
    #.... > .. > .
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    

    if len(new_id) >= 1:
        if new_id[0] =='.': new_id = new_id[1::] 
    if len(new_id) >= 1:    
        if new_id[-1] == '.': new_id = new_id[:-1:]
    
    if new_id == '': new_id = 'a' 
    
    if len(new_id) >= 16: 
        new_id = new_id[:15] 
        if new_id[-1] == '.': new_id = new_id[:-1:]
    
    if len(new_id) <= 2:
        while len(new_id) !=3:
            k = new_id[-1]
            new_id = new_id + k
    
    return new_id
