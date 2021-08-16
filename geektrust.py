from person import Person
from family import Family


class FamilyTree:
    """
    construct a family tree with members
    """
    @staticmethod
    def construct():
        # setting leading man and his wife into top of the tree
        king_shan = Person("King Shan", "M", None, None)
        king_shan.generation = 0
        queen_anga = Person("Queen Anga", "F", None, None)
        family = Family(king_shan)
        family.marriage_of_a_family_member(king_shan, queen_anga)
        # list of family members that needs to be added into family tree
        new_members_list = [
            # First generation
            {"from_family": True, "name": "Ish", "sex": "M", "parent": "King Shan"},
            {"from_family": True, "name": "Chit", "sex": "M", "parent": "King Shan"},
            {"from_family": True, "name": "Vich", "sex": "M", "parent": "King Shan"},
            {"from_family": True, "name": "Satya", "sex": "F", "parent": "King Shan"},
            {"from_family": True, "name": "Aras", "sex": "M", "parent": "King Shan"},
            # Spouses of first generation
            {"from_family": False, "name": "Amba", "sex": "F", "partner_name": "Chit"},
            {"from_family": False, "name": "Lika", "sex": "F", "partner_name": "Vich"},
            {"from_family": False, "name": "Vyan", "sex": "M", "partner_name": "Satya"},
            {"from_family": False, "name": "Chitra", "sex": "F", "partner_name": "Aras"},
            # second Generation
            {"from_family": True, "name": "Drita", "sex": "F", "parent": "Chit"},
            {"from_family": True, "name": "Tritha", "sex": "F", "parent": "Chit"},
            {"from_family": True, "name": "Vritha", "sex": "M", "parent": "Chit"},
            {"from_family": True, "name": "Vila", "sex": "F", "parent": "Vich"},
            {"from_family": True, "name": "Chika", "sex": "F", "parent": "Vich"},
            {"from_family": True, "name": "Jnki", "sex": "F", "parent": "Aras"},
            {"from_family": True, "name": "Ahit", "sex": "M", "parent": "Aras"},
            {"from_family": True, "name": "Asva", "sex": "M", "parent": "Satya"},
            {"from_family": True, "name": "Vyas", "sex": "M", "parent": "Satya"},
            {"from_family": True, "name": "Atya", "sex": "F", "parent": "Satya"},
            # Spouses of second Generation
            {"from_family": False, "name": "Jaya", "sex": "M", "partner_name": "Drita"},
            {"from_family": False, "name": "Arit", "sex": "M", "partner_name": "Jnki"},
            {"from_family": False, "name": "Satvy", "sex": "F", "partner_name": "Asva"},
            {"from_family": False, "name": "Krpi", "sex": "F", "partner_name": "Vyas"},
            # Third Generation
            {"from_family": True, "name": "Yodhan", "sex": "M", "parent": "Drita"},
            {"from_family": True, "name": "Laki", "sex": "M", "parent": "Arit"},
            {"from_family": True, "name": "Lavnya", "sex": "F", "parent": "Arit"},
            {"from_family": True, "name": "Vasa", "sex": "M", "parent": "Asva"},
            {"from_family": True, "name": "Kriya", "sex": "M", "parent": "Vyas"},
            {"from_family": True, "name": "Krithi", "sex": "F", "parent": "Vyas"}
        ]

        # let's add all the new members into family
        for new_person in new_members_list:
            if new_person["from_family"]:
                # add person/child to family
                FamilyTree.add_person_to_family(family, new_person)
            else:
                # add's a spouse of family member to the family tree
                FamilyTree.add_spouse_to_family_member(family, new_person)
        return family

    @staticmethod
    def add_person_to_family(family, person):
        """
        Adds a person/child to the family
        :param family: Instance of Family class
        :param person: a new person in family, which is instance of Person class
        """
        family.add_new_born(person["parent"], person["name"], person["sex"])

    @staticmethod
    def add_spouse_to_family_member(family, spouse):
        """
        Adding a outside person into family as a member's spouse
        :param family: instance of family
        :param spouse: spouse an instance of Person class, the new person family as a member's spouse
        """
        member = family.find_member_by_name(spouse["partner_name"])
        spouse = Person(spouse['name'], spouse['sex'])
        family.marriage_of_a_family_member(member, spouse)

