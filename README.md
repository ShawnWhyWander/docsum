

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
The US Supreme Court has lifted a lower court's suspension of a law from 1798, allowing President Donald Trump's administration to deport Venezuelan migrants accused of being part of a criminal gang. The court did not rule on the legality of the deportations, but instead allowed the administration to continue using the law. The decision has been met with criticism from progressive justices, who argue that the law is being misused to arbitrarily deport immigrants.
```

```
$ python3 docsum.py docs/constitution-mx.txt
This is the introduction and first two articles of the Mexican Constitution, which was originally published on February 5, 1917, and has undergone several reforms, with the last update being in 2011. Here's a summary:

**Introduction**

The document is the Constitution of the United Mexican States, which was published in the Official Journal of the Federation on February 5, 1917. It has undergone several reforms, with the last one being on June 10, 2011.

**Article 1**

* The Constitution guarantees individual rights and freedoms, which cannot be restricted or suspended except in cases and under conditions established by the Constitution itself.
* Slavery is prohibited in Mexico, and foreign slaves who enter the country will be freed and protected by the law.
* Any form of discrimination that threatens human dignity and aims to nullify or restrict individual rights and freedoms is prohibited.

**Article 2**

* The Mexican Nation is a single, indivisible entity.
* The Nation has a pluricultural composition based on its indigenous peoples, who are descendants of populations that inhabited the country's territory before colonization and have preserved their social, economic, cultural, and political institutions.
* The consciousness of one's indigenous identity is a fundamental criterion for determining who is eligible for the rights and protections afforded to indigenous peoples.
* Indigenous communities are defined as groups that form a social, economic, and cultural unit, are settled in a specific territory, and recognize their own authorities according to their customs and traditions.
* Indigenous peoples have the right to self-determination, which will be exercised within a constitutional framework of autonomy that ensures national unity. 

Overall, these articles establish the foundation for the protection of individual rights and freedoms, the recognition of indigenous peoples' rights, and the definition of the Mexican Nation as a pluricultural entity.

El texto describe los derechos y la autonomía de los pueblos y comunidades indígenas en México, reconocidos en la Constitución. A continuación, se presentan los puntos clave:

1. **Reconocimiento en constituciones y leyes estatales**: Los estados deben reconocer a los pueblos y comunidades indígenas en sus constituciones y leyes, considerando criterios etnolingüísticos y de asentamiento físico.

2. **Derecho a la libre determinación y autonomía**: Se reconoce el derecho a la libre determinación y autonomía para:
   - **Decidir formas internas de convivencia y organización**: Libertad para decidir su organización social, económica, política y cultural.
   - **Aplicar sistemas normativos**: Uso de sistemas normativos propios para resolver conflictos internos, respetando principios generales, garantías individuales, derechos humanos y dignidad de las mujeres.
   - **Elegir autoridades**: Elección de autoridades según normas, procedimientos y prácticas tradicionales, con participación equitativa de mujeres.
   - **Preservar cultura e identidad**: Preservar y enriquecer lenguas, conocimientos y elementos culturales.
   - **Conservar hábitat y tierras**: Conservación y mejora del hábitat y preservación de la integridad de sus tierras.
   - **Acceso a recursos naturales**: Acceso preferente a los recursos naturales de sus territorios, con respeto a la propiedad y derechos adquiridos por terceros.
   - **Representación en ayuntamientos**: Elección de representantes en municipios con población indígena.
   - **Acceso a la jurisdicción del Estado**: Derecho a ser asistidos por intérpretes y defensores que conozcan su lengua y cultura en juicios y procedimientos.

3. **Legislación estatal**: Las entidades federativas deben reconocer y regular estos derechos en los municipios para fortalecer la participación y representación política de acuerdo con sus tradiciones y normas internas.

En resumen, el texto constitucional garantiza a los pueblos y comunidades indígenas el derecho a la libre determinación, autonomía en diversos ámbitos, y acceso a la justicia con respeto a sus especificidades culturales. Estos derechos deben ser reconocidos y regulados tanto en la Constitución federal como en las leyes y constituciones de las entidades federativas.

El texto establece las obligaciones de la Federación, los Estados y los Municipios para promover la igualdad de oportunidades de los indígenas y eliminar prácticas discriminatorias.

**Resumen de las obligaciones:**

1. **Desarrollo regional**: Impulsar el desarrollo regional en zonas indígenas para fortalecer economías locales y mejorar condiciones de vida.
2. **Educación**: Garantizar e incrementar niveles de escolaridad, favoreciendo educación bilingüe e intercultural, alfabetización y educación básica.        
3. **Salud**: Asegurar acceso efectivo a servicios de salud, aprovechando medicina tradicional y apoyando nutrición indígena.
4. **Mejora de condiciones de vida**: Mejorar condiciones de comunidades indígenas, facilitando acceso a financiamiento para vivienda y servicios sociales básicos.
5. **Incorporación de mujeres indígenas**: Propiciar incorporación de mujeres indígenas al desarrollo, apoyando proyectos productivos, salud y educación.     
6. **Comunicaciones**: Extender red de comunicaciones para integrar comunidades indígenas.
7. **Apoyo a actividades productivas**: Apoyar actividades productivas de comunidades indígenas.

**Enfoque en la colaboración**: Todas estas acciones deben ser diseñadas y operadas conjuntamente con las comunidades indígenas.
```

```
$ python3 docsum.py docs/research_paper.pdf
Here's a summary:

**Problem**: Existing methods for pretraining large document embeddings (i.e., generating numerical representations of documents) focus only on local information, resulting in high-quality sentence embeddings but poor-quality document embeddings.

**Proposed Solution**: The authors propose a new pretraining method called DOCSPLIT, which uses contrastive learning to force models to consider the entire global context of a large document. DOCSPLIT works by:

1. Splitting an input document into two new document summaries by randomly assigning each sentence to one of the two summaries.
2. Using these summaries as positive instances for contrastive learning, which encourages the model to represent them with similar embeddings.

**Key Benefits**: DOCSPLIT is fully unsupervised, easy to implement, and can be used to pretrain any model architecture.

**Experimental Results**: The authors show that DOCSPLIT outperforms other pretraining methods on document classification, few-shot learning, and document retrieval tasks.

**Contribution**: DOCSPLIT addresses the limitation of existing pretraining methods, which focus only on local information, and provides a simple yet effective way to improve document embeddings.

Here's a summary:

**Introduction**
The paper presents DOCSPLIT, a new unsupervised pretraining method designed specifically for large documents. DOCSPLIT uses contrastive learning to improve document representations and can be applied to any model architecture.

**Background**
Contrastive learning is a technique that learns effective representations by pulling semantically close neighbors together and pushing apart non-neighbors in the latent space. Existing methods for contrastive learning, such as SimCSE and contrastive tension, are generic and can be used with any type of input, but do not take explicit advantage of document structure.

**Related Work**
There are two categories of related work: models trained using contrastive learning, and models designed for large documents. The INSTRUCTOR model is a state-of-the-art model that uses a specially constructed corpus of manual-human annotations, but is limited to sentence-level annotations.

**DOCSPLIT**
The authors propose DOCSPLIT, which uses contrastive learning with a new method for generating positive samples. They evaluate DOCSPLIT on standard large document classification, few-shot learning, and document retrieval tasks, and find that models pretrained using DOCSPLIT significantly outperform models pretrained with other published methods.

**Experimental Setup**
The authors describe two pretrained models based on the BERT architecture and the LongFormer architecture, which are evaluated on several tasks to demonstrate the effectiveness of DOCSPLIT.

The text describes a research paper on contrastive learning for document-level tasks. Here's a summary:

**Background**

* Contrastive learning is a technique used to train models by contrasting positive and negative pairs of data points.
* Document-level tasks are challenging because human annotation for documents is expensive, and models need to understand long-range dependencies.

**Contributions**

* The authors propose a method called DOCSPLIT to construct positive pairs for contrastive learning at the document level.
* DOCSPLIT splits a document into sentences and randomly assigns them to two documents, which are used as positive pairs.

**Related Work**

* The Contriever model uses a similar contrastive objective, but with document cropping and inverse cloze tasks.
* Large document architectures, such as LongFormer and BigBird, have been proposed to reduce computational requirements for processing long documents.        

**Methodology**

* The authors use a contrastive loss function with a temperature parameter (τ = 0.05) and a masked language model (MLM) loss (with weight = 0.1) for pretraining.
* They use English Wikipedia articles as their pretraining dataset.

**Key Points**

* DOCSPLIT provides built-in overfitting resistance through data augmentation. 
* The authors' method improves on the INSTRUCTOR model on document-level tasks.

Overall, the paper proposes a simple and effective method for constructing positive pairs for contrastive learning at the document level, which can be used to improve models on document-level tasks.
```

```
$ python3 docsum.py https://elpais.com/us/
Aquí te presento un resumen de las noticias:

**Política y Migración**

* El artículo de portada habla sobre el fin del "privilegio cubano" en Estados Unidos, que ha dejado a 550.000 cubanos sin poder ajustar su estatus en el país.
* La ciudad de Doral, en Florida, con una gran población venezolana, va a colaborar con la agencia migratoria federal (ICE) para detener a migrantes.
* El presidente Donald Trump criticó al gobierno mexicano por no hacer lo suficiente contra los carteles.

**Política en Estados Unidos**

* La dupla de legisladores demócratas Bernie Sanders y Alexandria Ocasio-Cortez están realizando una gira nacional para revitalizar el apoyo a sus políticas. 

**Cultura y Sociedad**

* Se presenta una reseña sobre la vida sentimental del escritor Mario Vargas Llosa, que ha tenido una vida amorosa muy pública y ha estado casado con su tía y ha tenido relaciones con una prima y una amiga.
* Vargas Llosa también fue recordado por su viaje al Congo en 2008 para investigar sobre un diplomático británico.

**Justicia y Derechos Humanos**

* Una jueza estadounidense ordenó el retorno de un ciudadano salvadoreño, Kilmar Abrego García, y criticó al gobierno de El Salvador por no hacer nada para lograr su regreso.
* El presidente de El Salvador, Nayib Bukele, había negado previamente el regreso de Abrego García.

**Economía**

* La economía latina en Estados Unidos crece más rápido que la del conjunto del país, según un estudio reciente.

Espero que esto te sea útil. ¡Si necesitas algo más, no dudes en preguntar!    

Este texto parece ser un resumen de noticias de diferentes fuentes, principalmente relacionadas con Estados Unidos y algunos temas internacionales. A continuación, te presento un resumen de los temas más destacados:

**NASA y espacio**

* El Telescopio Espacial "Nancy Roman" de la NASA podría ver recortado su programa científico a la mitad bajo la administración de Trump.
* La Sociedad Astronómica de Estados Unidos advierte de consecuencias "catastróficas" para el predominio estadounidense en exploración espacial.

**Política y economía**

* El secretario del Tesoro de Estados Unidos se reunió con ministros europeos y les solicitó más gasto militar y la eliminación de la "tasa Google".
* El expresidente Joe Biden criticó la administración de Trump, diciendo que ha causado "tanto daño" en un discurso en Chicago.

**Seguridad y justicia**

* Estados Unidos apunta contra La Familia Michoacana, una organización criminal mexicana, en su lucha contra el fentanilo.
* Un tribunal de Georgia imputó a los líderes de la organización y el Departamento de Estado ofrece ocho millones de dólares por ellos.

**Tecnología y ciencia**

* Un experto en inteligencia artificial, Ramon López de Mántaras, cree que la consciencia solo se puede dar en seres vivos y que herramientas como ChatGPT tienen una aportación científica "más bien escasa".

**Cultura y sociedad**

* Se estrena un documental sobre Sly Stone, el artista que cambió la historia de la música con su banda Sly & The Family Stone.
* Francisco Uría, un directivo y escritor, habla sobre Julio César y su popularidad en un libro y una obra de teatro.

**Información útil**

* Se proporcionan detalles sobre el cheque estímulo del IRS, la nueva identificación REAL ID para viajar en Estados Unidos y el Formulario I-407 para renunciar voluntariamente a la Green Card.

Espero que esta sea una buena síntesis de las noticias presentadas. Si tienes alguna pregunta específica sobre alguno de estos temas, no dudes en preguntar.  

Este texto parece ser un resumen de noticias de diferentes fuentes y temas. A continuación, te presento un resumen de los temas y noticias que se mencionan:  

**Economía y mercados**

* Warren Buffett, presidente de Berkshire Hathaway, ha aumentado su fortuna a pesar del pánico bursátil gracias a sus récords de liquidez.
* Nvidia ha perdido $5.500 millones de dólares debido a la prohibición de exportar un nuevo chip a China impuesta por Trump.
* Los mercados voluntarios de carbono se presentan como una alternativa para financiar el futuro del planeta.

**Política y conflictos**

* La directora de la ONG israelí Gisha denuncia que bloquear la ayuda a la población de Gaza es un claro crimen de guerra.
* Los socialdemócratas alemanes comienzan a votar el acuerdo de coalición con la CDU, pese al rechazo de las juventudes.
* La ONU se moviliza por el caso de una familia sin hogar que lleva 16 años de okupa en España.
* El Partido Comunista chino se hace omnipresente en el Tíbet, según denuncias de Gobiernos y ONG.

**Guerra y conflictos**

* La guerra en Sudán ha provocado una tragedia humanitaria, con historias de supervivencia y dolor.
* Los presidentes de Estados Unidos y El Salvador se conjuran para ignorar una resolución judicial que afecta a los derechos humanos.

**Medio ambiente y sostenibilidad**

* La cumbre amazónica del clima en Belém ha destacado la importancia de proteger la región y su biodiversidad.
* Voluntarios brasileños están trabajando para reverdecer sus ciudades y luchar contra el cambio climático.
* La desaparición de plantas invisibles para la conservación internacional podría tener graves consecuencias.

**Cultura y sociedad**

* La apropiación cultural es un tema de debate, especialmente en relación con los tatuajes y la moda.
* La cocina puede ser una forma de proteger una cultura milenaria, como se muestra en las recetas de Antonia Torres.
* El filme 'Warfare' es un ejemplo de cine hiperrealista que aborda temas de guerra y conflicto.

Espero que esta sea una buena síntesis de las noticias y temas que se tratan en el texto original. Si necesitas más información sobre alguno de estos temas, no dudes en preguntar.
```

```
$ python3 docsum.py https://www.cmc.edu/sites/default/files/about/images/20170213-cube.jpg
The image presents a serene and modern architectural scene, likely taken at dusk or dawn. The main subject of the image is a large, glass-enclosed structure situated on the edge of a reflective pool.

* A large, glass-enclosed structure:
        + The structure has a square base with a flat roof.
        + It features a minimalist design with a black frame and floor-to-ceiling glass walls.
        + The interior is well-lit, with several orange and yellow chairs arranged in a conversational setting.
        + The room appears to be empty, with no people visible inside.
* A reflective pool:
        + The pool is rectangular in shape and surrounds the glass-enclosed structure on three sides.
        + Its surface reflects the lights from the building, creating a sense of symmetry and calmness.
        + The pool's water is still, creating a perfect mirror-like reflection of the surrounding architecture.
* A multi-story building:
        + The building is located to the right of the glass-enclosed structure.
        + It has multiple levels, each with rows of windows that are illuminated from within.
        + The building's facade is partially obscured by the glass-enclosed structure and the trees in the background.
* The background:
        + The sky above is a deep blue, with some clouds scattered across it.  
        + Trees are visible behind the buildings, adding a touch of natural beauty to the scene.

In summary, the image showcases a modern and peaceful architectural setting, featuring a glass-enclosed structure, a reflective pool, and a multi-story building. The serene atmosphere and symmetrical composition create a sense of calmness and sophistication.
```