##### Group Class Continued #####

# Add an additional method to the Group class from the previous question called merge(...).
# The merge method should accept as a parameter an instance of another Group object.  This
# method should merge the two groups together and return a new group that contains all of the 
# members from both groups.  The newly created group may have any name.

# See below for the expected output of a program that uses the Group class.

# >>> g1 = Group("A-Team", ["Tim", "Clement"])
# >>> g2 = Group("B-Team", ["Antoine"])
# >>> g3 = g1.merge(g2)
# >>> print(g3.get_members())
# ["Antoine", "Clement", "Tim"]  

class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group.")

    def get_members(self):
        return sorted(self.members)

    def merge(self, group):
        combined_members = self.members + group.members
        new_group = Group("Any Name", combined_members)
        return new_group