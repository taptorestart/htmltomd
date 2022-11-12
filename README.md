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
<h1>htmltomd</h1>
<p>
htmltomd is a simple package for converting HTML to Markdown.
</p>
<h2>Getting Started</h2>
<p>
pip install htmltomd
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
<div># htmltomd
htmltomd is a simple package for converting HTML to Markdown.
## Getting Started
pip install htmltomd
</div>
```
