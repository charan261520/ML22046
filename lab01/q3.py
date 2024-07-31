def get_list(prompt): 

    print(prompt) 

    return list(map(int, input("Enter the integers separated by spaces: ").split())) 

  

def find_com_ele(l1, l2): 

    s1 = set(l1) 

    s2 = set(l2) 

    com_ele = s1.intersection(s2) 

    return com_ele 

  

def main(): 

    l1 = get_list("Enter the first list of integers:") 

    l2 = get_list("Enter the second list of integers:") 

     

    com_ele = find_com_ele(l1, l2) 

     

    print(f"Number of common elements: {len(com_ele)}") 

    print(f"Common elements: {sorted(com_ele)}") 

  

if __name__ == "__main__": 

    main() 