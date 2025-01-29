import pytest

from project2_building_your_own_custom_chatbot.helpers import remove_everything_after_references, split_into_chunks


def test_remove_references_section():
    text_with_references = 'This is some content.\n=== References ===\n[1] Some reference link'
    expected_output = "This is some content.\n"
    assert remove_everything_after_references(text_with_references) == expected_output

def test_no_references_section():
    text_without_references = "This is some content without references."
    expected_output = "This is some content without references."
    assert remove_everything_after_references(text_without_references) == expected_output

def test_references_at_start():
    text_with_references_at_start = """=== References ===
    [1] Some reference link
    """
    expected_output = ""
    assert remove_everything_after_references(text_with_references_at_start) == expected_output

# Tests for split_into_chunks
def test_split_into_chunks_all_sentences_less_than_limit():
    text = "This is sentence one. This is sentence two. This is sentence three."
    expected = ["This is sentence one.", "This is sentence two.", "This is sentence three."]
    assert split_into_chunks(text, max_chunk_size=5) == expected

def test_split_into_chunks_one_sentence_more_than_limit():
    text = "This is sentence one and has more words than 5. This is sentence two. This is sentence three."
    expected = ["This is sentence one and has more words than 5.", "This is sentence two.", "This is sentence three."]
    assert split_into_chunks(text, max_chunk_size=5) == expected

def test_split_into_chunks_one_sentence_only_and_it_is_more_than_limit():
    text = "This is sentence 1 and has more words than 5."
    expected = ["This is sentence 1 and has more words than 5."]
    assert split_into_chunks(text, max_chunk_size=5) == expected

if __name__ == "__main__":
    pytest.main()