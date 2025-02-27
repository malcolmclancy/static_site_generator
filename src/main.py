from textnode import TextNode, TextType

def main():
    node = TextNode("textnode", TextType.BOLD, "https://boot.dev/")
    print(node)

main()