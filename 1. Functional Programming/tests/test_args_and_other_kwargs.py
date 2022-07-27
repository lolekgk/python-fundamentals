from args_and_other_kwargs import list_parameters


class TestArgsAndOtherKwargs:
    def test_list_parameters_with_both_arguments(self):
        result = list_parameters(
            1, 2, 3, name='Peter', surname='Sagan', age=26
        )
        assert result[0] == 1
        assert result[1] == 2
        assert result[2] == 3
        assert result['name'] == 'Peter'
        assert result['surname'] == 'Sagan'
        assert result['age'] == 26

    def test_list_parameters_without_arguments(self):
        result = list_parameters()
        assert result == {}
