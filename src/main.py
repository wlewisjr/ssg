from textnode import TextNode, TextType


def main():
    t_node = TextNode("Anchor Text", TextType.LINK, "http://something.com")
    print(t_node)


if __name__ == "__main__":
    main()
