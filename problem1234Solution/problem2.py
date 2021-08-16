import sys
sys.path.insert(0, "../")
from familyTree import FamilyTree
from problem1234Solution.problem1 import Problem1


class Problem2:
    
    
    @staticmethod
    def get_mothers(family):
        women_list = []
        for member in family.members:
            if member.sex == "F" and member.spouse:
                daughter_count = len(member.daughters)
                if daughter_count > 0:
                    women_list.append((daughter_count, member.name))
        women_list.sort(reverse=True)
        return women_list

    @staticmethod
    def add_child(family):
        parent_name = input("Enter Parent Name: ")
        options = ["Daughter", "Son"]
        for index, name in enumerate(options):
            print("Enter " + str(index) + " If you want to  " + name + ".")
        option_number = int(input("Your option : "))
        child_name = input("Enter "+options[option_number] + " name :")
        sex = "F" if option_number == 0 else "M"
        family.add_new_born(parent_name, child_name, sex)
        print("child Added successfully")


if __name__ == "__main__":
    family = FamilyTree().construct()
    most_daughter_women_list = Problem2.get_mothers(family)
    print(", ".join([x[1] for x in most_daughter_women_list]))
    Problem2.add_child(family)
    most_daughter_women_list = Problem2.get_mothers(family)
    print(most_daughter_women_list[0][1])
    # using problem1 here to get a person's relatives based on a relationship
    print("Press Ctrl-C to break the loop")
    try:
        while True:
            Problem1.print_relatives_of_member(family)
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass

