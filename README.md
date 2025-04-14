

# docsum

This `docsum.py` script summarizes the content of files you provide. It works with `.html`, `.txt`, `.pdf`, and `.jpg` formats, from both local paths and URLs.

## Supported File Types
- Text files (`.txt`)
- HTML files (`.html`)
- PDF documents (`.pdf`)
- Images (`.jpg`) via Groq Vision

## Example Commands

```bash
$ python3 docsum.py docs/news-mx.html
The US Supreme Court has lifted a lower court's suspension of a law from 1798, allowing President Donald Trump's administration to deport Venezuelan migrants accused of being part of a criminal gang. The court did not rule on the legality of the deportations, but instead allowed the administration to continue using the law. The decision has been met with criticism from progressive justices, who argue that the law is being misused to arbitrarily deport immigrants.

$ python3 docsum.py docs/constitution-mx.txt

$ python3 docsum.py docs/research_paper.pdf

$ python3 docsum.py https://elpais.com/us/

$ python3 docsum.py https://www.cmc.edu/sites/default/files/about/images/20170213-cube.jpg
```