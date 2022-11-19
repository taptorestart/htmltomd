import re


# Source: https://developer.mozilla.org/en-US/docs/Web/HTML/Element
HTML_ELEMENTS_MAIN_ROOT = ["html"]
HTML_ELEMENTS_DOCUMENT_META = ["base", "head", "link", "meta", "style", "title"]
HTML_ELEMENTS_SECTIONING_ROOT = ["body"]
HTML_ELEMENTS_CONTENT_SECTIONING = [
    "address", "article", "aside", "footer", "header", "h1", "h2", "h3", "h4", "h5", "h6", "main", "nav", "section"
]
HTML_ELEMENTS_TEXT_CONTENT = [
    "blockquote", "dd", "div", "dl", "dt", "figcaption", "figure", "hr", "li", "menu", "ol", "p", "pre", "ul"
]
HTML_ELEMENTS_INLINE_TEXT_SEMANTICS = [
    "a", "abbr", "b", "bdi", "bdo", "br", "cite", "code", "data", "dfn", "em", "i", "kbd", "mark", "q", "rp", "rt",
    "ruby", "s", "samp", "small", "span", "strong", "sub", "sup", "time", "u", "var", "wbr"
]
HTML_ELEMENTS_IMAGE_MULTIMEDIA = ["area", "audio", "img", "map", "track", "video"]
HTML_ELEMENTS_EMBEDDED_CONTENT = ["embed", "iframe", "object", "picture", "portal", "source"]
HTML_ELEMENTS_SVG_MATHML = ["svg", "math"]
HTML_ELEMENTS_SCRIPTING = ["canvas", "noscript", "script"]
HTML_ELEMENTS_DEMARCATING_EDITS = ["del", "ins"]
HTML_ELEMENTS_TABLE_CONTENT = ["caption", "col", "colgroup", "table", "tbody", "td", "tfoot", "th", "thead", "tr"]
HTML_ELEMENTS_FORMS = [
    "button", "datalist", "fieldset", "form", "input", "label", "legend", "meter", "optgroup", "option", "output",
    "progress", "select", "textarea"
]
HTML_ELEMENTS_INTERACTIVE_ELEMENTS = ["detail", "dialog", "summary"]
HTML_ELEMENTS_WEB_COMPONENTS = ["slot", "template"]
HTML_ELEMENTS_OBSOLETE_DEPRECATED_ELEMENTS = [
    "acronym", "applet", "bgsound", "big", "blink", "center", "content", "dir", "font", "frame", "frameset", "image",
    "keygen", "marquee", "menuitem", "nobr", "noembed", "noframes", "param", "plaintext", "rb", "rtc", "shadow",
    "spacer", "strike", "tt", "xmp"
]
HTML_ELEMENTS_ALL = HTML_ELEMENTS_MAIN_ROOT + HTML_ELEMENTS_DOCUMENT_META + HTML_ELEMENTS_SECTIONING_ROOT + \
                    HTML_ELEMENTS_CONTENT_SECTIONING + HTML_ELEMENTS_TEXT_CONTENT + \
                    HTML_ELEMENTS_INLINE_TEXT_SEMANTICS + HTML_ELEMENTS_IMAGE_MULTIMEDIA + \
                    HTML_ELEMENTS_EMBEDDED_CONTENT + HTML_ELEMENTS_SVG_MATHML + \
                    HTML_ELEMENTS_SCRIPTING + HTML_ELEMENTS_DEMARCATING_EDITS + HTML_ELEMENTS_TABLE_CONTENT + \
                    HTML_ELEMENTS_FORMS + HTML_ELEMENTS_INTERACTIVE_ELEMENTS + HTML_ELEMENTS_WEB_COMPONENTS + \
                    HTML_ELEMENTS_OBSOLETE_DEPRECATED_ELEMENTS


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


def figure_to_md(html: str) -> str:
    result = re.search("(?s)(?<=<figure>)(.*?)(?=</figure>)", html)
    if result is not None:
        pre_result = re.sub(f"<figure>", "", html[0:result.start()], count=1)
        post_result = re.sub(f"</figure>", "", html[result.end():], count=1)
        src = re.search("(?s)(?<=<img src=\")(.*?)(?=\")", result.group(0))
        alt = re.search("(?s)(?<=alt=\")(.*?)(?=\")", result.group(0))
        figcaption = re.search("(?s)(?<=<figcaption>)(.*?)(?=</figcaption>)", result.group(0))
        caption = figcaption.group(0) if figcaption is not None else alt.group(0) if alt is not None else ""
        source = src.group(0) if src is not None else ""
        figure_content = f"\n![{caption}]({source})\n"
        html = f"{pre_result}{figure_content}{post_result}"
        html = figure_to_md(html)

    result = re.search("(?s)(?<=<figure\s)(.*?)(?=>)(.*?)(?=</figure>)", html)
    if result is not None:
        pre_result = re.sub("<figure\s", "", html[0:result.start()], count=1)
        post_result = re.sub("</figure>", "", html[result.end():], count=1)
        src = re.search("(?s)(?<=<img src=\")(.*?)(?=\")", result.group(0))
        alt = re.search("(?s)(?<=alt=\")(.*?)(?=\")", result.group(0))
        figcaption = re.search("(?s)(?<=<figcaption>)(.*?)(?=</figcaption>)", result.group(0))
        caption = figcaption.group(0) if figcaption is not None else alt.group(0) if alt is not None else ""
        source = src.group(0) if src is not None else ""
        figure_content = f"\n![{caption}]({source})\n"
        html = f"{pre_result}{figure_content}{post_result}"
        html = figure_to_md(html)
    return html


def p_to_md(html: str) -> str:
    html = element_to_md('p', html, '\n', '\n')
    return html


def br_to_linebreak(html: str) -> str:
    html = html.replace("<br>", "\n")
    html = html.replace("</br>", "\n")
    return html


def get_title(html: str) -> str:
    pattern_search = f"(?s)(?<=<title>)(.*?)(?=</title>)"
    result = re.search(pattern_search, html)
    title = result.group(0) if result is not None else ""
    return title


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
    result = re.sub(r"\n{3,}", "\n\n", html)
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
    html = br_to_linebreak(html)
    html = b_to_md(html)
    html = strong_to_md(html)
    html = i_to_md(html)
    html = a_to_md(html)
    html = figure_to_md(html)
    html = h1_to_md(html)
    html = h2_to_md(html)
    html = h3_to_md(html)
    html = h4_to_md(html)
    html = h5_to_md(html)
    html = h6_to_md(html)
    html = p_to_md(html)
    for tag in HTML_ELEMENTS_ALL:
        html = remove_tag(tag, html)
    html = newlines_to_newline(html)
    return html
