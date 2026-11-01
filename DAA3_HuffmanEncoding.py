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

#====VIVA Questions====
"""
Viva Questions and Answers
Basic Questions
Q1. What is Huffman Encoding?

Ans: Huffman Encoding is a lossless data compression technique that assigns variable-length binary codes to characters based on their frequencies.

Q2. What is lossless compression?

Ans: Lossless compression reduces data size without losing any original information.

Q3. What is the main objective of Huffman Encoding?

Ans: To reduce the total number of bits required to represent data.

Q4. Which algorithmic technique is used in Huffman Encoding?

Ans: Greedy Algorithm.

Q5. Why is Huffman Encoding called a greedy algorithm?

Ans: Because it repeatedly selects the two nodes with the lowest frequencies and combines them.

Q6. What is a Huffman Tree?

Ans: A Huffman Tree is a binary tree used to generate unique binary codes for characters.

Q7. What is the difference between fixed-length and variable-length encoding?

Ans: Fixed-length encoding uses the same number of bits for every character, whereas variable-length encoding uses different numbers of bits depending on character frequency.
Algorithm-Related Questions
Q8. How does Huffman Encoding work?

Ans:
1. Calculate the frequency of each character.
2. Create a node for each character.
3. Insert all nodes into a priority queue.
4. Remove the two nodes with the lowest frequencies.
5. Combine them into a new node.
6. Repeat until only one node remains.
7. Generate binary codes by traversing the tree.

Q9. What is a priority queue?
Ans: A priority queue is a data structure in which elements are removed according to their priority. In this program, the node with the lowest frequency is removed first.

Q10. Why do we select the two nodes with the lowest frequencies?
Ans: To generate an optimal prefix code with minimum weighted encoding cost.

Q11. What is a prefix code?
Ans: A prefix code is a code in which no character's code is the prefix of another character's code.

Q12. Why is Huffman Encoding considered efficient?

Ans: Because frequently occurring characters receive shorter codes, while less frequent characters receive longer codes.
Program-Related Questions
Q13. What is the purpose of heapq in Python?

Ans: The heapq module implements a min-heap priority queue.

Q14. What is a Node class?

Ans: A Node class represents each character or internal node in the Huffman Tree.

Q15. What does __init__() do?

Ans: It initializes the attributes of a Node object, such as character, frequency, left child, and right child.

Q16. What is the purpose of __lt__()?

Ans: It compares two nodes based on their frequencies so that heapq can maintain the min-heap order.

Q17. What does heapq.heappush() do?

Ans: It inserts an element into the priority queue.

Q18. What does heapq.heappop() do?

Ans: It removes and returns the element with the lowest frequency.

Q19. Why do we use root.left and root.right?

Ans: They represent the left and right child nodes of the Huffman Tree.

Q20. Why do we assign 0 to the left branch and 1 to the right branch?

Ans: To generate binary codes while traversing the Huffman Tree. These assignments are conventional and can be reversed.

Q21. What does frequency.get(char, 0) + 1 do?

Ans: It counts the frequency of each character in the input string.

Q22. Why do we use root.char is not None?

Ans: To identify a leaf node containing an actual character.

Q23. What happens if the input contains only one unique character?

Ans: The program assigns the code 0 to that character.

Complexity-Related Questions
Q24. What is the time complexity of Huffman Encoding?
Ans: O(n + k log k), where n is the input string length and k is the number of unique characters.

Q25. What is the space complexity of Huffman Encoding?

Ans: O(n + k), including the frequency dictionary, Huffman Tree, and generated codes.

Q26. What is the main advantage of Huffman Encoding?
Ans: It reduces storage requirements by assigning shorter codes to frequently occurring characters.

Q27. What is the main disadvantage of Huffman Encoding?

Ans: The Huffman Tree or code table must also be stored or transmitted to decode the compressed data.

Q28. Where is Huffman Encoding used?
Ans: It is used in data compression formats and algorithms such as ZIP, JPEG, and other compression systems.
                                                  """
