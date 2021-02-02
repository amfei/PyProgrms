# Auto detect text files and perform LF normalization
ssn_name_pairs= {"555-1234": "Bob", 
                "555-1239":  "Bob",
                "555-2345":  "Matthew",
                "555-3456":  "Luke",
                "555-11222": "Bob",
                "003-9929":  "Luke"}



    
def find_duplicated(ssn_name_dictionary:dict)->dict:
    result={}
    names=list(ssn_name_dictionary.values())
    for(ssn,name) in ssn_name_dictionary.items():
        if names.count(name)>1:
            result[name]=result.get(name,[])
            result[name].append(ssn)
    return result


dup_names =find_duplicated(ssn_name_pairs)
print(dup_names)
for (name,ssn) in dup_names.items():
    print(f"Found Duplicated Name {name} With SSN {ssn}")

