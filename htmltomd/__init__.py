import re


def element_to_md(element: str, html: str, prefix: str = "", suffix: str = "") -> str:
    pattern_search = f"(?s)(?<=<{element}>)(.*?)(?=</{element}>)"
    result = re.search(pattern_search, html)
    if result is not None:
        pre_result = re.sub(f"<{element}>", "", html[0:result.start()], count=1)
        post_result = re.sub(f"</{element}>", "", html[result.end():], count=1)
        html = f"{pre_result}{prefix}{result.group(0)}{suffix}{post_result}"
        html = element_to_md(element, html, prefix, suffix)

    pattern_search = f"(?s)(?<=<{element}\s)(.*?)(?=>)(.+?)(?=</{element}>)"
    result = re.search(pattern_search, html)
    if result is not None:
        pre_result = re.sub(f"<{element}\s", "", html[0:result.start()], count=1)
        post_result = re.sub(f"</{element}>", "", html[result.end():], count=1)
        content = re.search(f"(?s)(?<=>)(.*?)(?=</{element}>)", html[result.start():])
        html = f"{pre_result}{prefix}{content.group(0)}{suffix}{post_result}"
        html = element_to_md(element, html, prefix, suffix)
    return html


def h1_to_md(html: str) -> str:
    html = element_to_md('h1', html, '\n# ', '\n')
    return html


def h2_to_md(html: str) -> str:
    html = element_to_md('h2', html, '\n## ', '\n')
    return html


def h3_to_md(html: str) -> str:
    html = element_to_md('h3', html, '\n### ', '\n')
    return html


def h4_to_md(html: str) -> str:
    html = element_to_md('h4', html, '\n#### ', '\n')
    return html


def h5_to_md(html: str) -> str:
    html = element_to_md('h5', html, '\n##### ', '\n')
    return html


def h6_to_md(html: str) -> str:
    html = element_to_md('h6', html, '\n###### ', '\n')
    return html


def b_to_md(html: str) -> str:
    html = element_to_md('b', html, '**', '**')
    return html


def strong_to_md(html: str) -> str:
    html = element_to_md('strong', html, '**', '**')
    return html


def i_to_md(html: str) -> str:
    html = element_to_md('i', html, '*', '*')
    return html


def a_to_md(html: str) -> str:
    result = re.search("(?s)(?<=<[a|A]\s)(.*?)(?=>)(.*?)(?=</[a|A]>)", html)
    if result is not None:
        pre_result = re.sub("<[a|A]\s", "", html[0:result.start()], count=1)
        post_result = re.sub("</[a|A]>", "", html[result.end():], count=1)
        href = re.search("(?s)(?<=[href=|HREF=]\")(.*?)(?=\")", result.group(0))
        content = re.search("(?s)(?<=>)(.*?)(?=</[a|A]>)", html[result.start():])
        html = f"{pre_result}[{content.group(0)}]({href.group(0)}){post_result}"
        html = a_to_md(html)
    return html


def p_to_md(html: str) -> str:
    html = element_to_md('p', html, '\n', '\n')
    return html


def get_body(html: str) -> str:
    pattern_search = f"(?s)(?<=<body>)(.*?)(?=</body>)"
    result = re.search(pattern_search, html)
    if result is not None:
        html = result.group(0)

    pattern_search = f"(?s)(?<=<body\s)(.*?)(?=>)(.+?)(?=</body>)"
    result = re.search(pattern_search, html)
    if result is not None:
        content = re.search(f"(?s)(?<=>)(.*?)(?=</body>)", html[result.start():])
        html = content.group(0)
    return html


def remove_scripts(html: str) -> str:
    result = re.sub("<script.*?>\n*?.*?\n*?</script>", "", html)
    return result


def remove_styles(html: str) -> str:
    result = re.sub("<style.*?>\n*?.*?\n*?</style>", "", html)
    return result


def remove_comments(html: str) -> str:
    result = re.sub("<!--\n*?.*?\n*?-->", "", html)
    return result


def remove_links(html: str) -> str:
    result = re.sub("<link\n*?.*?\n*?/>", "", html)
    return result


def remove_tabs(html: str) -> str:
    result = re.sub(r"\s+", " ", html)
    return result


def remove_newlines(html: str) -> str:
    result = re.sub(r"\n+", "", html)
    return result


def newlines_to_newline(html: str) -> str:
    result = re.sub(r"\n+", "\n", html)
    return result


def remove_tag(tag: str, html: str) -> str:
    result = re.sub(f"<{tag}\n*?.*?\n*?>", "", html)
    result = re.sub(f"</{tag}>", "", result)
    return result


def html_to_md(html: str) -> str:
    html = get_body(html)
    html = remove_newlines(html)
    html = remove_tabs(html)
    html = remove_scripts(html)
    html = remove_styles(html)
    html = remove_links(html)
    html = remove_comments(html)
    html = remove_tag("div", html)
    html = remove_tag("iframe", html)
    html = remove_tag("footer", html)
    html = remove_tag("ins", html)
    html = remove_tag("span", html)
    html = b_to_md(html)
    html = strong_to_md(html)
    html = i_to_md(html)
    html = a_to_md(html)
    html = h1_to_md(html)
    html = h2_to_md(html)
    html = h3_to_md(html)
    html = h4_to_md(html)
    html = h5_to_md(html)
    html = h6_to_md(html)
    html = p_to_md(html)
    html = newlines_to_newline(html)
    return html
