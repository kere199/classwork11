from collections import Counter

def most_frequent_item_count(collection):
    if collection == []:
        return 0
    
    counter = Counter(collection)   
    return counter.most_common(1)[0][1]
    
    
    

print(most_frequent_item_count([1,2,3,3,4,3,3,4]))
       
        
    


