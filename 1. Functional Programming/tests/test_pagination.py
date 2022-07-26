from pagination import paginate


class TestPagination:
    def test_paginate_first_page_with_many_elements_on_page(self):
        items = list(range(101))
        result = paginate(items, 10, 1)
        assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_paginate_middle_page_with_many_elements_on_page(self):
        items = list(range(101))
        result = paginate(items, 10, 5)
        assert len(result) == 10
        assert result[0] == 40
        assert result[5] == 45

    def test_paginate_first_page_with_not_many_elements_on_page(self):
        items = list(range(101))
        result = paginate(items, 2, 1)
        assert result == [0, 1]

    def test_paginate_middle_page_with_not_many_elements_on_page(self):
        items = list(range(101))
        result = paginate(items, 2, 5)
        assert result == [8, 9]

    def test_paginate_last_not_full_page(self):
        items = list(range(101))
        result = paginate(items, 10, 11)
        assert len(result) == 1
