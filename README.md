

# docsum

This `docsum.py` script summarizes the content of files you provide. It works with `.html`, `.txt`, `.pdf`, and `.jpg` formats, from both local paths and URLs.

## Supported File Types
- Text files (`.txt`)
- HTML files (`.html`)
- PDF documents (`.pdf`)
- Images (`.jpg`) via Groq Vision

## Example Commands

```
$ python3 docsum.py docs/news-mx.html
The US Supreme Court, in a divided 5-4 decision, has allowed the Trump administration to continue using a 1798 wartime law to deport Venezuelan immigrants accused of belonging to a criminal gang. The US Supreme Court has ruled that the government has the authority to deport non-citizens under the Foreign Enemy Act, a law dating back to 1792, sparking concerns about executive power and civil liberties. Here is a summary of the text in 1 sentence in English:  The US government has vowed to track down and expel any remaining members of the Tren de Aragua gang, while the Supreme Court has allowed the use of the Enemy Alien law, amid controversy over the detention and deportation of immigrants, including a Salvadoran man who was mistakenly deported.
```

```
$ python3 docsum.py docs/constitution-mx.txt
The Political Constitution of the United Mexican States, published in 1917 and amended through 2011, establishes the fundamental laws and guarantees of Mexico, including individual rights, the prohibition of slavery and discrimination, and the recognition of indigenous peoples' rights to self-determination and autonomy. The Mexican Constitution recognizes and guarantees the rights of indigenous peoples and communities to self-determination and autonomy, including the right to preserve their culture, language, and traditions, and to participate in the election of their own authorities and representatives. Here is a 1-sentence summary in English:  The Mexican government is obligated to establish institutions and policies to promote equality of opportunities for indigenous people, eliminate discriminatory practices, and ensure their rights and integral development, through coordinated actions with indigenous communities.
```

```
$ python3 docsum.py docs/research_paper.pdf
The authors propose a new pretraining method called DOCSPLIT, which uses contrastive learning to force models to consider the entire global context of a large document, resulting in high-quality document embeddings. This paper presents DOCSPLIT, an unsupervised pretraining method specifically designed for large documents, which uses contrastive learning to improve document representations and outperforms existing methods. Here is a 1-sentence summary of the text in English:  The authors propose a new method called DOCSPLIT for constructing positive pairs for contrastive learning, which significantly improves the performance of the INSTRUCTOR model on document-level tasks.
```

```
$ python3 docsum.py https://elpais.com/us/
The latest news from El País US edition covers various topics, including the end of the "Cuban privilege" in the US, a senator's efforts to free a wrongly deported migrant, and updates on politics, immigration, science, and economy, featuring news on Trump, the Cuban exile community, NASA, and the Latin American economy. Here is a summary of the text in 1 sentence in English:  The news includes various international stories, such as the US offering $8 million for two fugitives, a UK court ruling that defines a woman as a biological female, and reports on economics, health, and technology, including a successful stem cell transplant for Parkinson's disease and a technical issue with Spotify. Here is a summary of the text in 1 sentence in English:  The news digest covers various global topics, including trade negotiations between the US and other countries, the humanitarian crisis in Gaza, the COVID-19 pandemic, and environmental issues, as well as local news from countries such as Israel, Colombia, and Spain.
```

```
$ python3 docsum.py https://www.cmc.edu/sites/default/files/about/images/20170213-cube.jpg
The image depicts a modern glass building with a pool of water in front of it, surrounded by other buildings and a dark blue sky.
```