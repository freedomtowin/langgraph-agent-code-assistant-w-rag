import re
def remove_duplicate_phrases_or_sentences(text):
    # Split text into phrases/sentences based on punctuation followed by space or end of line
    # and keep the delimiters as part of the split results
    phrases = re.split(r'(\s*[.!?,]\s*|\.$)', text)
    seen = set()
    result = []

    for phrase in phrases:
        # Normalize the phrase to handle case sensitivity for comparison
        normalized = phrase.strip().lower()
        if normalized and normalized not in seen:
            seen.add(normalized)
            result.append(phrase.strip())

    # Join the unique phrases back with appropriate punctuation
    return ''.join(result)


errors = []


# Test case 1
output = remove_duplicate_phrases_or_sentences("This is a sentence. This is a sentence.")
if output != "This is a sentence.":
    err = f"Error: Expected 'This is a sentence.', but got '{output}'"
    errors.append(err)

# Test case 2
output = remove_duplicate_phrases_or_sentences("This is a sentence.This is a sentence.")
if output != "This is a sentence.":
    err = f"Error: Expected 'This is a sentence.', but got '{output}'"
    errors.append(err)

# Test case 3
output = remove_duplicate_phrases_or_sentences("Hello, hello, hello")
if output != "Hello,":
    err = f"Error: Expected 'Hello,', but got '{output}'"
    errors.append(err)

# Test case 4
output = remove_duplicate_phrases_or_sentences("a hard example . A hard example")
if output != "a hard example.":
    err = f"Error: Expected 'a hard example.', but got '{output}'"
    errors.append(err)


errors = "\n".join(errors)
if errors:
    raise Exception(errors)
else:
    print("All test cases passed successfully.")