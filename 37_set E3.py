def passed_atleast_one(science_passed,maths_passed):
    return science_passed | maths_passed

def passed_both(science_passed,maths_passed):
    return science_passed & maths_passed

def passed_maths_only(science_passed,maths_passed):
    return maths_passed - science_passed

def passed_only_one_subject(science_passed,maths_passed):
    return science_passed ^ maths_passed

def main():
    science_passed = {"Ian","Bell","Alice","Bob","Candace"}
    maths_passed = {"Alice","Shaun","Ash","Ian","Mimi"}
    print(f"Students who passed atleast one subject are : {", ".join(passed_atleast_one(science_passed,maths_passed))}")
    print(f"Students who passed both subject are : {", ".join(passed_both(science_passed,maths_passed))}")
    print(f"Students who passed only maths subject are : {", ".join(passed_maths_only(science_passed,maths_passed))}")
    print(f"Students who passed only one subject are : {", ".join(passed_only_one_subject(science_passed,maths_passed))}")


if __name__ == "__main__":
    main()