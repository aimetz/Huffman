from ordered_list import OrderedList


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right
        
    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        return self.freq == other.freq and self.char == other.char

    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        return self.freq < other.freq or (self.freq == other.freq and self.char < other.char)

    def __repr__(self):
        return "Node(%d, %d, %s, %s)"%(self.char, self.freq, self.left, self.right)


def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file'''
    infile = open(filename, "r")
    char_freq = [0] * 255
    for line in infile:
        for ch in line:
            char_freq[ord(ch)] += 1
    return char_freq


def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''
    ol = OrderedList()
    for i in range(255):
        if char_freq[i] != 0:
            ol.add(HuffmanNode(i, char_freq[i]))
    while ol.size() > 1:
        a = ol.pop(0)
        b = ol.pop(0)
        if a.char < b.char:
            char = a.char
        else:
            char = b.char
        new = HuffmanNode(char, a.freq + b.freq)
        new.left = a
        new.right = b
        ol.add(new)
    return ol.pop(0)


def create_code(node, code=""):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    if node.left is None and node.right is None:
        return code, node.char
    return create_code(node.left, code + "0"), create_code(node.right, code + "1")


def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    header = ""
    for i in range(255):
        if freqs[i] != 0:
            header += "%d %d " % (i, freqs[i])
    header = header[:len(header) - 1] + "\n"
    return header


def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''
    freqs = cnt_freq(in_file)
    huff = create_huff_tree(freqs)
    header = create_header(freqs)
    code = create_code(huff)
    infile = open(in_file, "r")
    outfile = open(out_file, "w")
    infile.close()
    outfile.close()


freq = cnt_freq("file2.txt")
code = create_code(create_huff_tree(freq))
print(code)
print(create_header(freq))
