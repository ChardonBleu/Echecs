class Round:
    """[summary]
    """

    def __init__(self):
        """[summary]
        """

        self.round_name = ""
        self.match = []  # list of 4 instances of match
        self.horodatage_begin = ""
        self.horodatage_end = ""

    def __str__(self):
        """[summary]
        """
        return("{}".format(self.match))
