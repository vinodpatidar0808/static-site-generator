from textnode import TextNode, TextType

def main():
  textNode = TextNode('This is a text node', TextType.BOLD,"https://www.boot.dev")
  print(textNode)

main()