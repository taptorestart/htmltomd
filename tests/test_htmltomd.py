from htmltomd import element_to_md, h1_to_md, h2_to_md, h3_to_md, h4_to_md, h5_to_md, h6_to_md, b_to_md, \
    i_to_md, a_to_md, p_to_md, _get_body, html_to_md


def test_element_to_md():
    result = element_to_md("h1", "<div><h1>Heading level 1</h1></div>", "# ", "\n")
    assert result == "<div># Heading level 1\n</div>"
    result = element_to_md("h1", "<div><h1>Heading level 1</h1> <h1>Heading level 1</h1></div>", "# ", "\n")
    assert result == "<div># Heading level 1\n # Heading level 1\n</div>"


def test_h1_to_md():
    result = h1_to_md("<div><h1>Heading level 1</h1> <h1>Heading level 1</h1></div>")
    assert result == "<div># Heading level 1\n # Heading level 1\n</div>"
    result = h1_to_md("<div><h1 class='head'>Heading level 1</h1> <h1>Heading level 1</h1></div>")
    assert result == "<div># Heading level 1\n # Heading level 1\n</div>"
    result = h1_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_h2_to_md():
    result = h2_to_md("<div><h2>Heading level 2</h2> <h2>Heading level 2</h2></div>")
    assert result == "<div>## Heading level 2\n ## Heading level 2\n</div>"
    result = h2_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_h3_to_md():
    result = h3_to_md("<div><h3>Heading level 3</h3> <h3>Heading level 3</h3></div>")
    assert result == "<div>### Heading level 3\n ### Heading level 3\n</div>"
    result = h3_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_h4_to_md():
    result = h4_to_md("<div><h4>Heading level 4</h4> <h4>Heading level 4</h4></div>")
    assert result == "<div>#### Heading level 4\n #### Heading level 4\n</div>"
    result = h4_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_h5_to_md():
    result = h5_to_md("<div><h5>Heading level 5</h5> <h5>Heading level 5</h5></div>")
    assert result == "<div>##### Heading level 5\n ##### Heading level 5\n</div>"
    result = h5_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"


def test_h6_to_md():
    result = h6_to_md("<div><h6>Heading level 6</h6> <h6>Heading level 6</h6></div>")
    assert result == "<div>###### Heading level 6\n ###### Heading level 6\n</div>"
    result = h6_to_md("<div>Content</div>")
    assert result == "<div>Content</div>"

def test_b_to_md():
    result = b_to_md("<div><b>Bold</b> <b>Bold</b></div>")
    assert result == "<div>**Bold** **Bold**</div>"
    result = b_to_md("<div>Content</div>")
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


def test_p_to_md():
    result = p_to_md("<div><p class=\"article\">Paragraph</p> <p class=\"article\">Paragraph</p></div>")
    assert result == "<div>\nParagraph\n \nParagraph\n</div>"


def test_get_body():
    result = _get_body("<body>Body</body>")
    assert result == "Body"


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
    assert result == "<div>\nThis is paragraph.\n</div>"
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
    assert result == "<div># Title 1\nThis is first paragraph.\n## Subtitle 1\nThis is second paragraph." \
                     "\n## Subtitle 2\nThis is third paragraph.\n"
