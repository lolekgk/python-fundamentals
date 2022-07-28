import random

from infinite_randoms import history, random_number


class TestInfiniteRandom:
    def test_random_number(self):
        random.seed(900)
        result = random_number()
        assert next(result) == 0.9366763727671368
        assert len(history) == 1
