from enum import Enum

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = [b.strip() for b in blocks]
    blocks = [b for b in blocks if len(b) > 0]
    
    
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(block):
    if block.startswith("#"):
        for i in range(1, 7):
            if block[i] == " ":
                return BlockType.HEADING
            if block[i] == "#":
                continue
            else:
                return BlockType.PARAGRAPH
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if all(line.startswith(">") for line in block.splitlines()):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in block.splitlines()):
        return BlockType.UNORDERED_LIST
    lines = block.splitlines()
    if all(line.split(". ", 1)[0].isdigit() for line in lines):
        numbers = [int(line.split(". ", 1)[0]) for line in lines]
        if numbers == list(range(numbers[0], numbers[0] + len(numbers))):
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH