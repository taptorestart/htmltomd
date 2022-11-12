import re


def element_to_md(element: str, html: str, prefix: str, suffix: str) -> str:
    pattern_search = f"(?s)(?<=<{element}>)(.+?)(?=</{element}>)"
    result = re.search(pattern_search, html)
    if result is not None:
        pre_result = re.sub(f"<{element}>", "", html[0:result.start()], count=1)
        post_result = re.sub(f"</{element}>", "", html[result.end():], count=1)
        html = f"{pre_result}{prefix}{result.group(0)}{suffix}{post_result}"
        html = element_to_md(element, html, prefix, suffix)

    pattern_search = f"(?s)(?<=<{element}\s)(.+?)(?=>)(.+?)(?=</{element}>)"
    result = re.search(pattern_search, html)
    if result is not None:
        pre_result = re.sub(f"<{element}\s", "", html[0:result.start()], count=1)
        post_result = re.sub(f"</{element}>", "", html[result.end():], count=1)
        content = re.search(f"(?s)(?<=>)(.+?)(?=</{element}>)", html[result.start():])
        html = f"{pre_result}{prefix}{content.group(0)}{suffix}{post_result}"
        html = element_to_md(element, html, prefix, suffix)
    return html


def h1_to_md(html: str) -> str:
    html = element_to_md('h1', html, '# ', '\n')
    return html


def h2_to_md(html: str) -> str:
    html = element_to_md('h2', html, '## ', '\n')
    return html


def h3_to_md(html: str) -> str:
    html = element_to_md('h3', html, '### ', '\n')
    return html


def h4_to_md(html: str) -> str:
    html = element_to_md('h4', html, '#### ', '\n')
    return html


def h5_to_md(html: str) -> str:
    html = element_to_md('h5', html, '##### ', '\n')
    return html


def h6_to_md(html: str) -> str:
    html = element_to_md('h6', html, '###### ', '\n')
    return html


def b_to_md(html: str) -> str:
    html = element_to_md('b', html, '**', '**')
    return html


def i_to_md(html: str) -> str:
    html = element_to_md('i', html, '*', '*')
    return html


def a_to_md(html: str) -> str:
    result = re.search("(?s)(?<=<[a|A]\s)(.+?)(?=>)(.+?)(?=</[a|A]>)", html)
    if result is not None:
        pre_result = re.sub("<[a|A]\s", "", html[0:result.start()], count=1)
        post_result = re.sub("</[a|A]>", "", html[result.end():], count=1)
        href = re.search("(?s)(?<=[href=|HREF=]\")(.+?)(?=\")", result.group(0))
        content = re.search("(?s)(?<=>)(.+?)(?=</[a|A]>)", html[result.start():])
        html = f"{pre_result}[{content.group(0)}]({href.group(0)}){post_result}"
        html = a_to_md(html)
    return html


def p_to_md(html: str) -> str:
    html = element_to_md('p', html, '\n', '\n')
    return html


def _get_body(html: str) -> str:
    html = html.replace("\n", "")
    result = re.search("(?s)(?<=<body>)(.+?)(?=</body>)", html)
    if result is None:
        return html
    return f"{result.group(0)}"


def html_to_md(html: str) -> str:
    html = html.replace("\n", "")
    html = _get_body(html)
    html = b_to_md(html)
    html = i_to_md(html)
    html = a_to_md(html)
    html = h1_to_md(html)
    html = h2_to_md(html)
    html = h3_to_md(html)
    html = h4_to_md(html)
    html = h5_to_md(html)
    html = h6_to_md(html)
    html = p_to_md(html)
    html = html.replace("\n\n", "\n")
    return html
