# Paris-Real-Estate
This project uses data scraped from real estate listings to evaluate the importance of language used in property descriptions in predicting the price of real property in Paris

# Project Title
### Location, location, location

# Technologies used
### Webscraping tools:  Selenium, BeautifulSoup4
### Data analysis tools: numpy, pandas, sklearn
### Data visualization tools: matplotlib, seaborn

# Datasets used
All of the real estate transactions in France for the year 2022.  From public open data.

[French Real Estate]( https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/)

Datasets about trees, parks and pedestrian zones in Paris.

[Legendary Trees Paris](https://www.data.gouv.fr/fr/datasets/les-arbres-remarquables-1/)
[Parks Paris]( https://www.data.gouv.fr/fr/datasets/ilots-de-fraicheur-equipements-activites/)
[Pedestrian Areas Paris]( https://www.data.gouv.fr/fr/datasets/aires-pietonnes-et-assimilees/)

# Datasets created
Data about real estate listings in Paris for the month of June 2023.  From the listings data about the address, size and price were collected as well as keywords from the property listing. 

List of keywords extracted from the property listing using regular expressions.
- calme: describes a property that is in a calm, or private street or in a courtyard instead of being on the street.
- refait: describes an apartment that has been refurbished
- ascenseur: describes a building that has an elevator or if the property is a walkup
- terrasse: describes a property that has a balcony or a private outside space
- balcon: like ‘terrasse’ describes a property that has a balcony
- gardien: describes a building that has a concierge or just weekly or bi-weekly maintenance
- vue: describes a property that has a good view rather than facing another apartment - apartments with a view tend to have more privacy
- ancien: describes a building that is old or has historical significance
- charmant: although it is a filler word it tends to be used for properties that have exposed beams or stone that typically add to the value
- entretenu: describes a property that is well maintained with regular concierge service 
- exclusivité: although this could also be considered a filler word it tends to be used for properties that have not been on the market recently or atypical spaces
- superbe: considered to be important for finding interesting details related to a specific property
- lumineux: describes a property that has sunlight or southern exposure
- luminosité: describes a property that has sunlight or southern exposure
- beau: considered to be important for finding properties that have interesting details related to a specific property
- belle: considered to be important for finding properties that have interesting details related to a specific property
- traversant: describes a property that is spacious or has an open layout
- standing: describes a property that is more luxurious or associated with upper-class bulidngs
- hauteur: describes a property with exceptionally high ceilings
- pierre: used to describe a building that is made of cut stone rather that having a plaster covered wooden frame
- récent: describes a property that is a newer construction

App. 1000 entries: immobilieraVendre2023

Data about real estate sold in Paris in 2022 ranked by size and price.  The address of each entry was sent to an opensource API (PositionStack) to find the geolocation of each entry.  The geolocation of the property was compared to the geolocation of the trees, parks and pedestrian zones in Paris.  

App. 30,000 entries: immoVenduFinal

# Project Description
Although it is the city of lights and often considered the most beautiful city in the world, Paris is also one the most expensive cities in the world to buy real estate.  It’s all about location.  Size and location are the best features for determining the price of any real estate property.  Instead of using size and location within the city itself, BeautifulSoup4 was used to scrape data from all of the properties for sale in Paris in the month of June 2023.  The data scraped from the internet included location, size, price, number of rooms and a series of descriptive words typically used in real estate listings.  The words were used as categorical values with a value of 1 (desciption contains the word) or 0 (description does not contain the word).  The words were then used to determine whether they had a significant impact in predicting the price of real estate.

To determine what other factors impact the price of real property, the dataset about all of the real estate transactions in France for the year 2022 was used.  The data was filtered to include only transactions in Paris and the address, size and price of the property was extracted.  The address was to the open source API to find the geolocation.  Other datasets available from the French government contain the geolocation of trees of historical significance, parks and pedestrian areas in Paris.  The geolocation of the properties sold in 2022 were compared to the geolocation of the trees, parks and pedestrian areas to see how much the proximity to them impacted the price of the property.

# What is the goal of this project?
The year 2000 was a turning point in population demographics.  It was the year when the majority of the world’s population shifted from rural to urban dwellers.  The number of global urban residents is expected to rise for the next 50 years.  To determine how people will live in and interact with cities of the future, the goal of this project is to determine what factors other than size and location enter into the price of real estate, in a very dense and expensive city.  

# What do we learn from this project?
The outcomes of this project tell us that descriptive terms in real estate listings are very accurate at determining the price of real property with very low variance.  Although the relationship between property value and the distance to the nearest historically significant tree or park gives us a low correlation coefficient it does account for approximately 10% or the overall price of real property in the city of Paris.

# How to use this project
The public datasets used in the project are free and open source provided by the French government.  The datasets created for this project are available with this project.  Analysis was done using regression without size and location of property to determine how useful the data was independently of the most important means for establishing the value of real property.  Future use should reference this project.
