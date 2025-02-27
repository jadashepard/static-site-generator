from textnode import TextNode, TextType
from htmlnode import LeafNode

def main():
    test_text = TextNode("wow textnode", TextType.BOLD, "https://local")
    print(test_text.text_type)

if __name__ == "__main__":
    main()
