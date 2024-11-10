from textnode import TextNode, TextType


def main():

  txt_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
  print(txt_node)

main()
