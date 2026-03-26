def build_profile(**details):
    for key,value in details.items():
        print(f"{key} : {value}")
    return details   #didn't wanted to return None so wrote this  

print(build_profile(Username = "ishan274",Age = 20,City= "Amravati",Designation = "AI&DS undergraduate"))