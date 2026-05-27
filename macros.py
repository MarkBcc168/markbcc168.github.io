import re 
from datetime import date
from datetime import datetime
from pathlib import Path


def last_updated(path: str) -> str:
    file_path = Path(path)
    timestamp = file_path.stat().st_mtime
    modified_date = datetime.fromtimestamp(timestamp)
    return modified_date.strftime("%B %d, %Y")


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

def paper(text: str, coauthors: list[str]=[], links: dict[str, str] = {}, summary: str="",
          abstract: str="") -> str:
    link = link_from_text(text)
    result = '<details id="paper-header"><summary>'
    result += '<div style="display: flex;">'
    result += '<div style="flex-grow: 1;">'
    result += f'<a id="{link}"></a><span id=paper-header>{text}<a href="#{link}" class="hash-link"><i class="fa fa-link"></i></a></span>'
    if(len(coauthors) > 0):
        coauthors_str = ""
        for i in range(len(coauthors)-1):
            coauthors_str += coauthors[i] + ", "
        if(len(coauthors) > 1):
            coauthors_str += " and "
        coauthors_str += coauthors[-1]
        result += "<br>" + f"(with {coauthors_str})"
    result += "</div>"
    if("arXiv" in links):
        result += '<div style="width: fit-content; align-content:center;">'
        result += f'(<a href={links["arXiv"]}>arXiv</a>)'
        result += '</div>'
    elif("pdf" in links):
        result += '<div style="width: fit-content; align-content:center;">'
        result += f'(<a href={links["pdf"]}>pdf</a>)'
        result += '</div>'
    result += '</div>'
    result += '</summary>'
    result += summary
    if(abstract != ""):
        result += "<p><b>Abstract</b><br>"
        result += abstract + "</p>"
    result += "<p>" + " ".join(f'(<a href={link}>{text}</a>)' for text, link in links.items()) + "</p>"
    result += '</details>'
    return result

def notes(text: str, coauthors: list[str]=[], links: dict[str, str] = {}, summary: str="") -> str:
    link = link_from_text(text)
    result = '<details id="notes-header"><summary>'
    result += '<div style="display: flex;">'
    result += '<div style="flex-grow: 1;">'
    result += f'<a id="{link}"></a><span id=paper-header>{text}<a href="#{link}" class="hash-link"><i class="fa fa-link"></i></a></span>'
    if(len(coauthors) > 0):
        coauthors_str = ""
        for i in range(len(coauthors)-1):
            coauthors_str += coauthors[i] + ", "
        if(len(coauthors) > 1):
            coauthors_str += " and "
        coauthors_str += coauthors[-1]
        result += "<br>" + f"(with {coauthors_str})"
    result += "</div>"
    if("arXiv" in links):
        result += '<div style="width: fit-content; align-content:center;">'
        result += f'(<a href={links["arXiv"]}>arXiv</a>)'
        result += '</div>'
    elif("pdf" in links):
        result += '<div style="width: fit-content; align-content:center;">'
        result += f'(<a href={links["pdf"]}>pdf</a>)'
        result += '</div>'
    elif("slides" in links):
        result += '<div style="width: fit-content; align-content:center;">'
        result += f'(<a href={links["slides"]}>slides</a>)'
        result += '</div>'
    result += '</div>'
    result += '</summary>'
    result += summary
    result += "<p>" + " ".join(f'(<a href={link}>{text}</a>)' for text, link in links.items()) + "</p>"
    result += '</details>'
    return result