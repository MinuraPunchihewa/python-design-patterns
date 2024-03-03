from paragraph_tag import ParagraphTag
from bold_decorator import BoldDecorator


paragraph = ParagraphTag('This is a paragraph')
bold_paragraph = BoldDecorator(paragraph)
print(bold_paragraph.render())