import random

from power_of_colors import random_hex_colors, random_rgb_colors


class TestPowerOfColors:
    def test_random_hex_colors(self):
        result = random_hex_colors()
        assert len(result) == 7
        assert result[0] == '#'

    def test_random_hex_colors_range(self):
        result = random_hex_colors()
        for i in range(1, len(result)):
            assert (str(i) >= '0' and str(i) <= '9') or (
                str(i) >= 'a' and str(i) <= 'f'
            )

    def test_random_rgb_colors(self):
        result = random_rgb_colors()
        for item in result:
            assert item in range(0, 256)
