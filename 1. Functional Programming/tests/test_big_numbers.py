from chunks import to_chunks


class TestToChunks:
    def test_to_chunks_length_from_4_to_7(self):
        alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]
        result = to_chunks(alphabet, 4, 7)
        for chunk in result:
            assert len(chunk) >= 4 and len(chunk) <= 7

    def test_to_chunks_with_small_chunk_size_range(self):
        alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]
        result = to_chunks(alphabet, 2, 4)
        for chunk in result:
            assert len(chunk) >= 2 and len(chunk) <= 4

    def test_to_chunks_with_big_chunk_size_range(self):
        alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]
        result = to_chunks(alphabet, 1, 21)
        for chunk in result:
            assert len(chunk) >= 1 and len(chunk) <= 21

    def test_to_chunks_with_chunks_bigger_than_data_length(self):
        alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]
        result = to_chunks(alphabet, 25, 27)
        assert len(result) == 1

    def test_to_chunks_with_equal_min_and_max(self):
        alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]
        result = to_chunks(alphabet, 2, 2)
        for chunk in result:
            assert len(chunk) == 2
