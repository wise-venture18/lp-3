#•	DAA-3: Write a program to implement Huffman Encoding using a greedy strategy. 

import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Generate Huffman Codes
def generate_codes(root, code, huffman_codes):

    if root is None:
        return

    # Leaf node
    if root.char is not None:
        huffman_codes[root.char] = code if code else "0"
        return

    generate_codes(root.left, code + "0", huffman_codes)
    generate_codes(root.right, code + "1", huffman_codes)


# Huffman Encoding
def huffman_encoding(text):

    if not text:
        print("Input text cannot be empty.")
        return

    # Calculate character frequencies
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    # Create priority queue
    heap = []

    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    # Build Huffman Tree
    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    # Generate Huffman Codes
    root = heapq.heappop(heap)
    huffman_codes = {}

    generate_codes(root, "", huffman_codes)

    # Display results
    print("\nCharacter Frequencies and Huffman Codes:")

    for char, freq in frequency.items():
        display_char = "Space" if char == " " else char
        print(f"{display_char} : Frequency = {freq}, Code = {huffman_codes[char]}")

    # Encode input text
    encoded_text = ""

    for char in text:
        encoded_text += huffman_codes[char]

    print("\nOriginal Text:", text)
    print("Encoded Text:", encoded_text)


# Main Program
print("===== Huffman Encoding =====")

text = input("Enter a string: ")

huffman_encoding(text)

#---- END ----

#===SAMPLE INPUT=======
"""
===== Huffman Encoding =====
Enter a string: AAAABBCD

Character Frequencies and Huffman Codes:
A : Frequency = 4, Code = 0
B : Frequency = 2, Code = 10
C : Frequency = 1, Code = 110
D : Frequency = 1, Code = 111

Original Text: AAAABBCD
Encoded Text: 00001010110111
"""
