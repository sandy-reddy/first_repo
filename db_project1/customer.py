class Customer:
    #Employee attributes

    def __init__(self, first, last, dofb, custid):
        self.first = first
        self.last = last
        self.dofb = dofb
        self.custid = custid

    @property  
    def fullname(self):
        return "{} {}".format(self.first, self.last)


