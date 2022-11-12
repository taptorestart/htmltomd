import re


class HtmlToMd:
    @staticmethod
    def element_to_md(element: str, html: str, prefix: str, suffix: str) -> str:
        pattern_search = f"(?s)(?<=<{element}>)(.+?)(?=</{element}>)"
        result = re.search(pattern_search, html)
        if result is not None:
            pre_result = re.sub(f"<{element}>", "", html[0:result.start()], count=1)
            post_result = re.sub(f"</{element}>", "", html[result.end():], count=1)
            html = f"{pre_result}{prefix}{result.group(0)}{suffix}{post_result}"
            html = HtmlToMd.element_to_md(element, html, prefix, suffix)

        pattern_search = f"(?s)(?<=<{element}\s)(.+?)(?=>)(.+?)(?=</{element}>)"
        result = re.search(pattern_search, html)
        if result is not None:
            pre_result = re.sub(f"<{element}\s", "", html[0:result.start()], count=1)
            post_result = re.sub(f"</{element}>", "", html[result.end():], count=1)
            content = re.search(f"(?s)(?<=>)(.+?)(?=</{element}>)", html[result.start():])
            html = f"{pre_result}{prefix}{content.group(0)}{suffix}{post_result}"
            html = HtmlToMd.element_to_md(element, html, prefix, suffix)
        return html

    @staticmethod
    def h1_to_md(html: str) -> str:
        html = HtmlToMd.element_to_md('h1', html, '# ', '\n')
        return html

    @staticmethod
    def h2_to_md(html: str) -> str:
        html = HtmlToMd.element_to_md('h2', html, '## ', '\n')
        return html

    @staticmethod
    def h3_to_md(html: str) -> str:
        html = HtmlToMd.element_to_md('h3', html, '### ', '\n')
        return html

    @staticmethod
    def h4_to_md(html: str) -> str:
        html = HtmlToMd.element_to_md('h4', html, '#### ', '\n')
        return html

    @staticmethod
    def h5_to_md(html: str) -> str:
        html = HtmlToMd.element_to_md('h5', html, '##### ', '\n')
        return html

    @staticmethod
    def h6_to_md(html: str) -> str:
        html = HtmlToMd.element_to_md('h6', html, '###### ', '\n')
        return html

    @staticmethod
    def b_to_md(html: str) -> str:
        html = HtmlToMd.element_to_md('b', html, '**', '**')
        return html

    @staticmethod
    def i_to_md(html: str) -> str:
        html = HtmlToMd.element_to_md('i', html, '*', '*')
        return html

    @staticmethod
    def a_to_md(html: str) -> str:
        result = re.search("(?s)(?<=<[a|A]\s)(.+?)(?=>)(.+?)(?=</[a|A]>)", html)
        if result is not None:
            pre_result = re.sub("<[a|A]\s", "", html[0:result.start()], count=1)
            post_result = re.sub("</[a|A]>", "", html[result.end():], count=1)
            href = re.search("(?s)(?<=[href=|HREF=]\")(.+?)(?=\")", result.group(0))
            content = re.search("(?s)(?<=>)(.+?)(?=</[a|A]>)", html[result.start():])
            html = f"{pre_result}[{content.group(0)}]({href.group(0)}){post_result}"
            html = HtmlToMd.a_to_md(html)
        return html

    @staticmethod
    def p_to_md(html: str) -> str:
        html = HtmlToMd.element_to_md('p', html, '\n', '\n')
        return html

    @staticmethod
    def get_body(html: str) -> str:
        html = html.replace("\n", "")
        result = re.search("(?s)(?<=<body>)(.+?)(?=</body>)", html)
        if result is None:
            return html
        return f"{result.group(0)}"

    @staticmethod
    def html_to_md(html: str) -> str:
        html = html.replace("\n", "")
        html = HtmlToMd.get_body(html)
        html = HtmlToMd.b_to_md(html)
        html = HtmlToMd.i_to_md(html)
        html = HtmlToMd.a_to_md(html)
        html = HtmlToMd.h1_to_md(html)
        html = HtmlToMd.h2_to_md(html)
        html = HtmlToMd.h3_to_md(html)
        html = HtmlToMd.h4_to_md(html)
        html = HtmlToMd.h5_to_md(html)
        html = HtmlToMd.h6_to_md(html)
        html = HtmlToMd.p_to_md(html)
        html = html.replace("\n\n", "\n")
        return html
