class Validation:
    @staticmethod
    def is_blank(*args):
        return not all(list(args))

    @staticmethod
    def duplicate_rank_number(rank_list):
        """This is function check for duplicate rank numbers"""
        # Compare length for unique elements
        return not len(set(rank_list)) == len(rank_list)
