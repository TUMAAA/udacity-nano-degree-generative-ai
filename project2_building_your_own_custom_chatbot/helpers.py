import re
from openai.embeddings_utils import get_embedding, distances_from_embeddings

def remove_everything_after_references(text):
    # removes all text from reference section and below

    # Find the position of References section
    pattern = r'=+\s*References\s*=+'
    match = re.search(pattern, text, re.MULTILINE)

    if match:
        # Return only the text before References section
        return text[:match.start()]
    return text


def convert_wiki_headers(text):
    # Gets rid of the weird markup for headers '=== <header> ===' that can have different numbers of = depending on the header
    # Replace === header === with ### header
    text = re.sub(r'===\s*(.*?)\s*===', r'### \1', text+":")
    # Replace == header == with ## header
    text = re.sub(r'==\s*(.*?)\s*==', r'## \1', text+":")
    # Replace = header = with # header
    text = re.sub(r'=\s*(.*?)\s*=', r'# \1', text+":")
    return text


def split_into_chunks(text, max_chunk_size=200):
    # Splits a text string based on sentences such that the length of all included
    # **full** sentences in a chunk has no more than max_chunk_size words
    sentences = re.split(r'(?<=\.)\s+', text)
    chunks = []
    current_chunk = []

    for sentence in sentences:
        if len(' '.join(current_chunk + [sentence]).split()) <= max_chunk_size:
            current_chunk.append(sentence)
        else:
            if current_chunk:
                chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks


# From the exercise notebook "case study"
def get_rows_sorted_by_relevance(question, df, embedding_model_name):
    """
    Function that takes in a question string and a dataframe containing
    rows of text and associated embeddings, and returns that dataframe
    sorted from least to most relevant for that question
    """

    # Get embeddings for the question text
    question_embeddings = get_embedding(question, engine=embedding_model_name)

    # Make a copy of the dataframe and add a "distances" column containing
    # the cosine distances between each row's embeddings and the
    # embeddings of the question
    df_copy = df.copy()
    df_copy["distances"] = distances_from_embeddings(
        question_embeddings,
        df_copy["embeddings"].values,
        distance_metric="cosine"
    )

    # Sort the copied dataframe by the distances and return it
    # (shorter distance = more relevant so we sort in ascending order)
    df_copy.sort_values("distances", ascending=True, inplace=True)
    return df_copy