from itertools import product


class SudokuValidator:

    def __init__(self, data):
        self.data = data
        self.sqrt = len(self.data)**(1/2.0)
        self.subsquare_indices = [range(len(self.data))[x:x + int(self.sqrt)] for x in range(0, len(self.data),
                                                                                             int(self.sqrt))]

    def is_valid(self):
        if self.has_valid_structure():
            return all([self.has_valid_rows(),
                        self.has_valid_columns(),
                        self.has_valid_subsquares()])
        else:
            return False

    def has_valid_structure(self):
        return all([self.has_square_structure(),
                   self.sqrt > 0,
                   self.sqrt % 1 == 0,
                   self.are_not_bools()])

    def has_square_structure(self):
        return all([len(r) == len(self.data) for r in self.data])

    def are_not_bools(self):
        return all(all([not isinstance(i, bool) for i in r]) for r in self.data)

    def has_valid_rows(self):
        return all([self._valid_set(r) for r in self.data])

    def has_valid_columns(self):
        cols = [[r[n] for r in self.data] for n in range(len(self.data))]
        return all([self._valid_set(c) for c in cols])

    def has_valid_subsquares(self):
        blocks = [[self.data[r][c] for r, c in product(row_block, col_block)] for row_block, col_block in
                  product(self.subsquare_indices, self.subsquare_indices)]
        return all([self._valid_set(b) for b in blocks])

    @staticmethod
    def _valid_set(l):
        return set(l) == set(range(1, len(l) + 1))
