from htmltomd import element_to_md, h1_to_md, h2_to_md, h3_to_md, h4_to_md, h5_to_md, h6_to_md, b_to_md, \
    i_to_md, a_to_md, p_to_md, get_body, html_to_md, remove_comments, strong_to_md, newlines_to_newline, \
    remove_newlines, figure_to_md, get_title


def test_element_to_md():
    result = element_to_md("h1", "<div><h1>Heading level 1</h1></div>", "\n# ", "\n")
    assert result == "<div>\n# Heading level 1\n</div>"
    result = element_to_md("h1", "<div><h1>Heading level 1</h1> <h1>Heading level 1</h1></div>", "\n# ", "\n")
    assert result == "<div>\n# Heading level 1\n \n# Heading level 1\n</div>"
    result = element_to_md("h1", "<div>\n<h1>Heading level 1</h1>\n\n</div>", "\n# ", "\n")
    assert result == "<div>\n\n# Heading level 1\n\n\n</div>"


def test_h1_to_md():
    result = h1_to_md("<div><h1>Heading level 1</h1> <h1>Heading level 1</h1></div>")
    assert result == "<div>\n# Heading level 1\n \n# Heading level 1\n</div>"
    result = h1_to_md("<div><h1 class='head'>Heading level 1</h1> <h1>Heading level 1</h1></div>")
    assert result == "<div>\n# Heading level 1\n \n# Heading level 1\n</div>"
    result = h1_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_h2_to_md():
    result = h2_to_md("<div><h2>Heading level 2</h2> <h2>Heading level 2</h2></div>")
    assert result == "<div>\n## Heading level 2\n \n## Heading level 2\n</div>"
    result = h2_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_h3_to_md():
    result = h3_to_md("<div><h3>Heading level 3</h3> <h3>Heading level 3</h3></div>")
    assert result == "<div>\n### Heading level 3\n \n### Heading level 3\n</div>"
    result = h3_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_h4_to_md():
    result = h4_to_md("<div><h4>Heading level 4</h4> <h4>Heading level 4</h4></div>")
    assert result == "<div>\n#### Heading level 4\n \n#### Heading level 4\n</div>"
    result = h4_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_h5_to_md():
    result = h5_to_md("<div><h5>Heading level 5</h5> <h5>Heading level 5</h5></div>")
    assert result == "<div>\n##### Heading level 5\n \n##### Heading level 5\n</div>"
    result = h5_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_h6_to_md():
    result = h6_to_md("<div><h6>Heading level 6</h6> <h6>Heading level 6</h6></div>")
    assert result == "<div>\n###### Heading level 6\n \n###### Heading level 6\n</div>"
    result = h6_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_b_to_md():
    result = b_to_md("<div><b>Bold</b> <b>Bold</b></div>")
    assert result == "<div>**Bold** **Bold**</div>"
    result = b_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_strong_to_md():
    result = strong_to_md("<div><strong>Bold</strong> <strong>Bold</strong></div>")
    assert result == "<div>**Bold** **Bold**</div>"
    result = strong_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_i_to_md():
    result = i_to_md("<div><i>Italic</i> <i>Italic</i></div>")
    assert result == "<div>*Italic* *Italic*</div>"
    result = i_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_a_to_md():
    result = a_to_md(
        "<div><a href=\"https://taptorestart.com\" target=\"_black\">taptorestart.com</a> "
        "<a href=\"https://taptorestart.com\" target=\"_black\">taptorestart.com</a></div>"
    )
    assert result == "<div>[taptorestart.com](https://taptorestart.com) " \
                     "[taptorestart.com](https://taptorestart.com)</div>"
    result = a_to_md(
        "<div><A HREF=\"https://taptorestart.com\" target=\"_black\">taptorestart.com</A></div>"
    )
    assert result == "<div>[taptorestart.com](https://taptorestart.com)</div>"


def test_figure_to_md():
    html = "<div><figure class=\"image\"><img src=\"https://taptorestart.com/cat.png\"><figcaption>Cat</figcaption></figure></div>"
    result = figure_to_md(html)
    assert result == "<div>\n![Cat](https://taptorestart.com/cat.png)\n</div>"
    html = """
<div><figure class=\"image\"><img src=\"https://taptorestart.com/cat.png\"><figcaption>Cat</figcaption></figure></div>
<div><figure class=\"image\"><img src=\"https://taptorestart.com/dog.png\"><figcaption>Dog</figcaption></figure></div>
"""
    result = figure_to_md(html)
    assert result == "\n<div>\n![Cat](https://taptorestart.com/cat.png)\n</div>\n" \
                     "<div>\n![Dog](https://taptorestart.com/dog.png)\n</div>\n"
    html = "<figure><figcaption>Cat</figcaption></figure><figure><figcaption>Dog</figcaption></figure>"
    result = figure_to_md(html)
    assert result == "\n![Cat]()\n\n![Dog]()\n"


def test_p_to_md():
    result = p_to_md("<div><p class=\"article\">Paragraph</p> <p class=\"article\">Paragraph</p></div>")
    assert result == "<div>\nParagraph\n \nParagraph\n</div>"


def test_get_title():
    html = """
<head>
    <title>Title</title>
</head>    
"""
    result = get_title(html)
    assert result == "Title"


def test_get_body():
    html = """
<head>
    <body id="body-page">
        Body
    </body>
</html>    
"""
    result = get_body(html)
    assert result == "\n        Body\n    "
    result = get_body("<body>\n\nBody\n</body>")
    assert result == "\n\nBody\n"


def test_remove_comments():
    html = "<body><!-- comment -->hello!<!-- comment --></body>"
    result = remove_comments(html)
    assert result == "<body>hello!</body>"
    html = """
<body>
<!-- comment -->
hello!
<!-- comment -->
</body>
"""
    result = remove_comments(html)
    assert result == "\n<body>\n\nhello!\n\n</body>\n"


def test_remove_newlines():
    html = "\n\n\n\n<div></div>\n\n\n\n"
    result = remove_newlines(html)
    assert result == "<div></div>"


def test_newlines_to_newline():
    html = "\n\n\n\n<div></div>\n\n\n\n"
    result = newlines_to_newline(html)
    assert result == "\n<div></div>\n"


def test_html_to_md():
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<div>
<p>
This is paragraph.
</p>
</div>
</body>
</html>        
"""
    result = html_to_md(html)
    assert result == "\nThis is paragraph.\n"
    html = """
<div>
<h1>Title 1</h1>
<p>
This is first paragraph.
</p>
<h2>Subtitle 1</h2>
<p>
This is second paragraph.
</p>
<h2>Subtitle 2</h2>
<p>
This is third paragraph.
</p>
"""
    result = html_to_md(html)
    assert result == "\n# Title 1\nThis is first paragraph.\n## Subtitle 1\nThis is second paragraph." \
                     "\n## Subtitle 2\nThis is third paragraph.\n"
