#exercitiul 1
def list_operations(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    a_difference_b = set(a) - set(b)
    b_difference_a = set(b) - set(a)
    
    result = [intersection, union, a_difference_b, b_difference_a]
    return result

#exercitiul 2
def count_characters(text):
    char_count = {}
    
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

#exercitiul 3
def compare_dictionaries(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return False
    
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    
    if keys1 != keys2:
        return False
    
    for key in keys1:
        value1 = dict1[key]
        value2 = dict2[key]
        
        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare_dictionaries(value1, value2):
                return False
        elif isinstance(value1, (list, set, tuple)) and isinstance(value2, (list, set, tuple)):
            if len(value1) != len(value2):
                return False
            for item1, item2 in zip(sorted(value1), sorted(value2)):
                if item1 != item2:
                    return False
        elif value1 != value2:
            return False
    
    return True

#exercitul 4
def build_xml_element(tag, content, **attributes):
    opening_tag = "<" + tag
    for key, value in attributes.items():
        opening_tag += f' {key}="{value}"'
    opening_tag += f">{content}</{tag}>"
    return opening_tag

#exercitiul 5
def validate_dict(rules, input_dict):
    for key, prefix, middle, suffix in rules:
        if key not in input_dict:
            return False
        
        value = input_dict[key]
        if not value.startswith(prefix):
            return False
        
        middle_start = value.find(middle)
        if middle_start == -1 or middle_start == 0 or middle_start + len(middle) == len(value):
            return False
        
        if not value.endswith(suffix):
            return False
    
    return True

#exercitiul 6
def count_unique_and_duplicate_elements(input_list):
    unique_elements = set()
    duplicate_elements = set()
    
    for element in input_list:
        if element in unique_elements:
            duplicate_elements.add(element)
        else:
            unique_elements.add(element)
    
    return len(unique_elements), len(duplicate_elements)

#exercitiul 7
def perform_set_operations(*sets):
    result_dict = {}
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]
            
            union_key = f"{set1} | {set2}"
            result_dict[union_key] = set1 | set2
            
            intersection_key = f"{set1} & {set2}"
            result_dict[intersection_key] = set1 & set2
            
            diff_ab_key = f"{set1} - {set2}"
            result_dict[diff_ab_key] = set1 - set2
            
            diff_ba_key = f"{set2} - {set1}"
            result_dict[diff_ba_key] = set2 - set1
            
    return result_dict


#exercitiul 8 
def loop(mapping):
    visited = set()  
    result = [] 
    
    current_key = mapping.get('start')
    
    while current_key and current_key not in visited:
        visited.add(current_key)  
        result.append(current_key) 
        current_key = mapping.get(current_key) 
    
    return result

