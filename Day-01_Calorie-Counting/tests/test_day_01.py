import puzzle_1
import puzzle_2


class TestPuzzle1:
    """Tests for puzzle 1."""

    def test_puzzle_1(self, input_1):

        assert puzzle_1.find_max_calories_held(input_1) == 24000


class TestPuzzle2:
    """Tests for puzzle 2."""

    def test_puzzle_2(self, input_1):

        assert puzzle_2.find_sum_top_3_calories_held(input_1) == 45000
