from case_sensitive import case_check


class TestCaseSensitive:
    def test_case_check_one_argument_is_not_str(self):
        result = case_check(1, 'a')
        assert result == -1

    def test_case_check_both_arguments_are_not_str(self):
        result = case_check(1, False)
        assert result == -1

    def test_case_check_first_str_upper_second_lower(self):
        result = case_check('A', 'b')
        assert result == False

    def test_case_check_first_str_lower_second_upper(self):
        result = case_check('a', 'B')
        assert result == False

    def test_case_check_both_str_lower(self):
        result = case_check('a', 'b')
        assert result == True

    def test_case_check_both_str_upper(self):
        result = case_check('A', 'B')
        assert result == True
