from textnode import TextType, TextNode

def main():
    test_text = TextNode("wow textnode", TextType.BOLD, "https://local")
    print(test_text)

if __name__ == "__main__":
    main()
