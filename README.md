# `trip` Ontology

## About the Ontology

`Trip` is a generic [RDF-star](https://www.w3.org/2021/12/rdf-star.html) ontology to model travel diaries. The ontology was developed with the mathematician Jacob Bernoulli's (1654–1705) travel diary, the _Reisbüchlein_ [1] as prototype. Through the class and property structure, the ontology is capable to model different types of first-person travel narratives, regardless of author or geographical location. The data model is designed to accommodate future expansions without disruption to the existing data.

Standard RDF is not ideal for expressing the hierarchy of information. Meaning that it is nearly impossible to automatically infer which of the data is the quoted triple and which triple is metadata about it. This changed with RDF-star and so do the reasoning possibilities change with SPARQL-star. By nesting the RDF statements, we created a hierarchy that where information can be inferred, by using a triple as a subject, we automatically express that the RSF-star triple is information about the quoted triple. Further logical criteria can be added to create compound statements leading to great potential for knowledge discovery.

Bernoulli travelled through Europe in the years 1676 till 1683 and documented it in his diary. He included observations of the places he travelled to, the people he met, the activities he engaged in but also notes travel routes and expenses. The information in the travel diary contains a large amount of metadata about the activities, for example costs. RDF-star is uniquely suited to model such metadata.


## Selection of Test Data

Sections of the _Reisbüchlein_ were selected to test the data model, by writing turtle files according to the ontology's latest version. Intuitiveness and consistency were central during the construction of the data model. Mistakes in the logic and ways to improve the model, are best identified through SPARQL queries. Therefore, querying the data was a crucial part of the design process. Following, I describe the three sections that served as test data.

The first example covers Bernoulli's journey from Basel to Geneva and the subsequent stay. Additionally, to the narrative of his activities, he writes an extensive description of Geneva and ethnographic observations about its inhabitants and their customs.[Bernoulli “Reisbüchlein,” 3r-17r]

The second example is the segment from Bordeaux to La Tremblade during his journey from Bordeaux to Paris in 1680.[Bernoulli “Reisbüchlein,”  52r-52v]As the focus of the ontology is travel, I focused on different kinds of travel. While he rode to Geneva, in this example he travelled by boat on a river. The river changed names on the way and Bernoulli spent a night on the boat. This poses different challenges than land travel, as the boat is different to other transportation methods, which are exclusively used for mobility and not as accommodation.

The last part of the _Reisbüchlein_ describes Bernoulli's journey through Switzerland in 1683. During his other journeys he always travelled to a specified destination. Those journeys were done for a purpose rather than for the sake of travelling itself. This is not the case with his travels through Switzerland, which he titled: "Spatzier Reiss durch Schweitzerland" [Bernoulli “Reisbüchlein,” 90r] which translates to: "leisure trip through Switzerland." This title indicates that it was not for work purposes. As the whole Swiss journey is located under one title, it is not composed similarly to the Geneva journey, which consist of linear travel followed by a long stay. He never stayed long at any place but returned to Basel. Because of this, his journey to Küsnacht is my last example.[Bernoulli “Reisbüchlein,” 93r-94r]


Once the digitisation process of the _Reisbüchlein_ is completed it will be integrated with the [Bernoulli-Euler Online (BEOL)](https://beol.staging.dasch.swiss) digital edition, which contains correspondence and scientific notebooks from Bernoulli and Leonhard Euler. The `beol` ontology has been previously developed for the BEOL project [2] This ontology contains classes and predicates to model people, manuscripts and correspondence. Some parts of it can be reused. 

This project is hosted by the [Data and Service Center for the Humanities (DaSCH)](https://www.dasch.swiss), a long-term storage facility for humanities data. All project using their API, must extend the built-in `knora-base` ontology. 

## Installation

The data set "Reisbuchlein_ExampleData" of example data in the folder "ontology" containing 4284 RDF statements must be uploaded to a triplestore that supports RDF-star. To store and query the data we used the [GraphDB Free](https://graphdb.ontotext.com) edition. The following ontologies are to be uploaded together with the dataset.

**Required Ontologies**
- [`trip`](https://github.com/Nora-Olivia-Ammann/trip-ontology/blob/7a63c7d7a6e9617613ca248a485ec6999fe6eb0e/ontology/trip-onto.ttl)
- [`extension_beol`](https://github.com/Nora-Olivia-Ammann/trip-ontology/blob/7a63c7d7a6e9617613ca248a485ec6999fe6eb0e/ontology/extension_beol-onto.ttl)
- [`beol`](https://github.com/dasch-swiss/dsp-api/blob/708c21796a76cafab7ffe3f328af8c860fddf70b/test_data/ontologies/beol-onto.ttl)
- [`knora-base`](https://github.com/dasch-swiss/dsp-api/blob/708c21796a76cafab7ffe3f328af8c860fddf70b/knora-ontologies/knora-base.ttl)
- [GUI ontology](https://github.com/dasch-swiss/dsp-api/blob/708c21796a76cafab7ffe3f328af8c860fddf70b/knora-ontologies/salsah-gui.ttl)


## Visualisations

The visualisation uses a dataset that contains a data point for each expense Bernoulli noted in the whole _Reisbüchlein_. I researched this data through a text search algorithm in combination with manual research. I expect that not all instances are in the dataset, as the text documents used for the search have not yet been verified. Therefore, they may contain misspellings, which I cannot anticipate. Additionally, some data points were deleted. In order to be included in the dataset, each expense needs an identifiable geographic location and currency. All the data points that did not fulfil the criteria were excluded. The information for each data point includes: the date, location, currency, cost, and type of expense. In case of transportation cost, the destination of the transportation was used for the geographical location. Bernoulli used different spellings, synonyms, or abbreviations for currency names, making a total of 85 different spellings, I standardised those.

Four function calls are pre-programmed in file "function_calls.py", with a short description regarding the data displayed.


[1] Bernoulli, Jacob. “Reisbüchlein,” 1676. https://swisscollections.ch/Record/991170522084805501.


[2] Alassi, Sepideh. “From the Mechanics of Jacob Bernoulli to Digital History of Science. Infra- structure, Tools, and Methods.” University of Basel, 2020. https://edoc.unibas.ch/81737/.
