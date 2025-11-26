import re 

def hook_preconvert_header():
    for p in pages:
        p.source = re.sub(r"(#{1,6}) (.*)\n", r"\1 {{hl('\2')}}\n", p.source)

def hook_preconvert_equations():
    for p in pages:
        p.source = re.sub(r"\$\$([^\$]*)\$\$", r"\\[\1\\]", p.source)
        p.source = re.sub(r"\$([^\$]*)\$", r"\\(\1\\)", p.source)

def link_from_text(text: str) -> str:
    return text.lower().replace(" ", "_").replace("/","-").replace("\\", "")

def hl(text: str) -> str:
    link = link_from_text(text)
    return f'<a id="{link}"></a>{text}<a href="#{link}" class="hash-link"><i class="fa fa-link"></i></a>'

def paper(text: str, authors: str="") -> str:
    link = link_from_text(text)
    result = f'<a id="{link}"></a><span id=paper-header>{text}<a href="#{link}" class="hash-link"><i class="fa fa-link"></i></a></span>'
    if(authors != ""):
        result += "<br>" + f"(with {authors})"
    return result

def notes(text: str) -> str:
    link = link_from_text(text)
    result = f'<a id="{link}"></a><span id=notes-header>{text}<a href="#{link}" class="hash-link"><i class="fa fa-link"></i></a></span>&nbsp;&nbsp;'
    return result