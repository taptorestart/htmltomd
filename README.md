# htmltomd

htmltomd is a simple package for converting HTML to Markdown.

## Getting Started
```shell
pip install htmltomd
```

```Python
import htmltomd

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<div>
<h1><b>htmltomd</b></h1>
<br>
<p>
<i>htmltomd</i> is a simple package <br>for converting HTML to Markdown.
</p>
<h2>Getting Started</h2>
<p>
pip install htmltomd
</p>
<h2>Source code</h2>
<p>
<a href="https://github.com/taptorestart/htmltomd" target="_black">github.com/taptorestart/htmltomd</a>
</p>
<p>
<figure><img src="image.png"><figcaption>Image</figcaption></figure>
</p>
</div>
</body>
</html>  
"""
result = htmltomd.html_to_md(html)
print(result)
```

Result
```shell

# **htmltomd**

*htmltomd* is a simple package 
for converting HTML to Markdown.

## Getting Started

pip install htmltomd

## Source code

[github.com/taptorestart/htmltomd](https://github.com/taptorestart/htmltomd)

![Image](image.png)


```
