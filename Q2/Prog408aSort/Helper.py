class className:
    def __init__(self, id, score):
        self.id = id
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __str__(self):
        return f"{{ID: {self.id}, Score: {self.score}}}"