
class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
    
  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
    html_str =  ""
    if self.props:
      for prop in self.props:
        if len(html_str) > 0:
          html_str += f" {prop}=\"{self.props[prop]}\""
        else: 
          html_str += f"{prop}=\"{self.props[prop]}\""
        
    return html_str
  
  def __repr__(self):
    return f"HTMLNode( tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"


class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, props=None):
    self.children = None
    super().__init__(tag, value, self.children, props)
  
  def to_html(self):
    if not self.value:
      raise ValueError("All leaf nodes must have a value")
    if not self.tag:
      return self.value
    else:
      attributs = ""
      if self.props:
        for prop in self.props:
          attributs += f" {prop}=\"{self.props[prop]}\""
      return f"<{self.tag}{attributs}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
  def __init__(self, tag=None, children=None, props=None):
    self.value = None
    super().__init__(tag, self.value, children, props)

  def to_html(self):
    if not self.tag:
      raise ValueError("All parent nodes must have a tag")
    if not self.children:
      raise ValueError("All parent nodes must have children")
    else:
      parentAttr = "" 
      if self.props:
        for prop in self.props:
          parentAttr += f" {prop}=\"{self.props[prop]}\""
      children_in_html = self.children_to_html(self.children)

      return f"<{self.tag}{parentAttr}>{children_in_html}</{self.tag}>"
      
  def children_to_html(self, children):
    if len(children) == 1:
      return children[0].to_html()
    
    return children[0].to_html() + self.children_to_html(children[1:])

