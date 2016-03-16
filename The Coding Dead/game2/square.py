class Square(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.entity = ""

    def put_on_square(self, entity):
        self.entity = entity

    def get_from_square(self):
        return self.entity
