class Model:
    def __init__(self, parameters, init):
        # parameter controller
        self.parameters = parameters
        self.pram_a = 1 if init else parameters["pram_a"]
        self.pram_b = 2 if init else parameters["pram_b"]
        self.pram_c = 2 if init else parameters["pram_c"]

    def get_log(self):
        log = f'{self.pram_a} {self.pram_b} {self.pram_b}'
        return log

    def get_parameters(self):
        return self.parameters


class Model_2(Model):
    def __init__(self, *args):
        super(Model_2, self).__init__(*args)
