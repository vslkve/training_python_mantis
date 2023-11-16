from sys import maxsize


class Project:
    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return "%s" % self.name

    def __eq__(self, other):
        return self.name is None or other.name is None or self.name == other.name

    # def id_or_max(self):
    #     if self.id:
    #         return int(self.id)
    #     else:
    #         return maxsize

    def sorted_name(self):
        if self.name:
            return self.name
