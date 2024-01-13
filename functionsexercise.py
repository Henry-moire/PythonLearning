# Modify this function to return a list of strings as defined above
def list_benefits():
    strings_list = []
    strings_list.append("More organized code")
    strings_list.append("More readable code")
    strings_list.append("Easier code reuse")
    strings_list.append("Allowing programmers to share and connect code together")  
    return strings_list

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    finalSentence = benefit + " is a benefit of functions!"
    return finalSentence

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()