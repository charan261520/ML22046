def count_vnc(in_string): 

    vowels = "aeiouAEIOU" 

    v_count = 0 

    c_count = 0

    #test comment

    for char in in_string: 

        if char.isalpha(): 

            if char in vowels: 

                v_count += 1 

            else: 

                c_count += 1 

    return v_count, c_count 

def main(): 

    my_input = input("Enter a string: ") 

    vowels, consonants = count_vnc(my_input) 

    print(f"No of Vowels are: {vowels}") 

    print(f"No of Consonants are: {consonants}") 

if __name__ == "__main__": 

    main() 