from i_tag import ITag


class ParagraphTag(ITag):
    def render(self):
        return f'<p>{self.content}</p>'