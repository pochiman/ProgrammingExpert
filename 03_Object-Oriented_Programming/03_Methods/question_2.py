##### Group Class #####

# Add the following methods to the Group class:

##### add(...): accepts the name of a person as a parameter and adds them to the group.

##### delete (...): accepts the name of a person as a parameter and deletes them from the group.
##### If the name passed is not in the group, this method should raise an Exception.

##### get_members(...): returns a sorted list with the names of students in the group.
##### The list should be sorted in ascending order (i.e. A-Z).

# You do not need to make any instances of the class once you have added the methods.
# See below for the expected output of a program that uses the Group class.

# >>> g1 = Group("A-Team", ["Tim", "Joe"])
# >>> g1.add("Sally")
# >>> g1.add("Billy")
# >>> members = g1.get_members()
# >>> print(members)
# ["Billy", "Joe", "Sally", "Tim"]
# >>> g1.delete("Joe")
# >>> members = g1.get_members()
# >>> print(members)
# ["Billy", "Sally", "Tim"]
# >>> g1.delete("Joe")
# Exception: Member not in group

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