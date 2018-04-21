from misaka import HtmlRenderer, Markdown
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound
from rest_framework.renderers import BaseRenderer


class HighlighterRenderer(HtmlRenderer):
    def blockcode(self, text, lang):
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            lexer = None

        if lexer:
            formatter = HtmlFormatter()
            return highlight(text, lexer, formatter)
        return '\n<pre><code>{}</code></pre>\n'.format(text.strip())


class MarkdownRenderer(BaseRenderer):
    media_type = 'text/html'
    format = 'html'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        renderer = HighlighterRenderer()
        md = Markdown(renderer, extensions=('fenced-code',))
        return md(data)
