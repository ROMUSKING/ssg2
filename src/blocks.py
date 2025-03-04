

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = [b.strip() for b in blocks]
    blocks = [b for b in blocks if len(b) > 0]
    
    
    return blocks