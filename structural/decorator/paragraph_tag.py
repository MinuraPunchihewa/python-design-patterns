from i_tag import ITag
from bold_decorator import bold


class ParagraphTag(ITag):
    @bold
    def render(self):
        return f'<p>{self.content}</p>'