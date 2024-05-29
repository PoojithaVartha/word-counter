def count_words(text):
  """Counts the occurrences of words in a given text string.

  Args:
      text: The text string to analyze.

  Returns:
      A dictionary mapping each word to its count.
  """  

  # Split the text into words, handling extra spaces
  words = text.split()  

  # Create a dictionary to store word counts
  word_counts = {}
  for word in words:
    if word:  # Skip empty strings
      # Check if the word exists in the dictionary
      if word in word_counts:
        # Increment the count for the existing word
        word_counts[word] += 1
      else:
        # Add the new word with a count of 1
        word_counts[word] = 1

  # Return the dictionary containing word counts
  return word_counts

# Example usage
text = input("Enter the string:")
word_counts = count_words(text)

# Print the word counts
print(word_counts)
