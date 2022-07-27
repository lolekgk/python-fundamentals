import random

from normalize import normalize_data, random_number


class TestNormalize:

    data = [random.randint(0, 100000) for x in range(5)]

    def test_random_number_min_max(self):
        result = random_number(self.data)
        assert min(result) == 0
        assert max(result) == 1

    def test_random_number_list_range(self):
        result = random_number(self.data)
        for num in result:
            assert num >= 0 and num <= 1

    def test_normalize_data_min_max(self):
        result = normalize_data(self.data)
        assert min(result) == 0
        assert max(result) != 1

    def test_normalize_data_list_range(self):
        result = normalize_data(self.data)
        for num in result:
            assert num >= 0 and num < 1
