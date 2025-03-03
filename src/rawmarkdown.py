from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            next
        else:
            text_values = node.text.split(delimiter)
            size = len(text_values)
            if size % 2 == 0:
                raise ValueError(f"closing '{delimiter}' missing in {node}")
            for i in range(0, size):
                if i % 2 == 0:
                    new_nodes.append(TextNode(text_values[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(text_values[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def split_nodes_image(old_nodes):    
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            next
        else:
            node_text = node.text
            matches = extract_markdown_images(node_text)
            for match in matches:                
                text_values = node_text.split(f"![{match[0]}]({match[1]})", maxsplit=1)
                size = len(text_values)
                if size != 2:
                    raise ValueError(f"something not right with the image in {node}")
                node_text = text_values[1]        
                if len(text_values[0]) > 0:           
                    new_nodes.append(TextNode(text_values[0], TextType.TEXT))       
                new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            if len(node_text) > 0:          
                new_nodes.append(TextNode(node_text, TextType.TEXT))
                
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            next
        else:
            node_text = node.text
            matches = extract_markdown_links(node_text)
            for match in matches:                
                text_values = node_text.split(f"[{match[0]}]({match[1]})", maxsplit=1)
                size = len(text_values)
                if size != 2:
                    raise ValueError(f"something not right with the link in {node}")
                node_text = text_values[1]          
                if len(text_values[0]) > 0:          
                    new_nodes.append(TextNode(text_values[0], TextType.TEXT))       
                new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            if len(node_text) > 0:          
                new_nodes.append(TextNode(node_text, TextType.TEXT))
                
    return new_nodes


def text_to_textnodes(text):
        
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes