from enum import Enum

class TextType(Enum):
  NORMAL = "normal"
  BOLD = "bold"
  ITALIC = "italic"
  CODE = "code"
  LINK = "link"
  IMAGE = "image"


class TextNode():
  def __init__(self, text, textType, url=None):
    self.text = text
    self.textType = textType
    self.url = url
  
  def __eq__(self, node):
    return (self.text == node.text and self.textType == node.textType and self.url == node.url)

  def __repr__(self):
    return f"TextNode({self.text}, {self.textType.value}, {self.url})"
  



