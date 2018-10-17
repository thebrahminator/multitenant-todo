class TodoQueryString():
    def __init__(self):
        self.query = ""

    def __call__(self, *args, **kwargs):
        self.query_string = ""

    def create_table(self, *args, **kwargs):
        pass