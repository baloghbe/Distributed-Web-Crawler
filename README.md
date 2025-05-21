A Distributed Web Crawler solution aimed to gather publicly listed coffee prices by utilizing a dockerized architecture to create a modular and easily scalable schema. 
The modular segments will be individually separated into their corresponding docker containers, communication and cooperation will be handled between them by both APIs and Docker Swarm. 
This project aims to completely automate the process of discovery and extraction of price data, utilizing dockerized microservices to handle the process of crawling, parsing and visualizing.  

Services: 

Discovery Service: 

A base set of websites will be defined in the code, this service will crawl through those seeds and gather any possible link or document that correspond to the given parameters, 
and in turn will be passed into the database under the “discovered_sources” table and the crawler service for data parsing and download. 

Crawler Service: 

Once the discovery service shares the required URLs, this service will be responsible for gathering data through the individual links either by parsing data directly from the website or downloading 
the relevant PDFs and collecting data from them. The parsed and collected data then will be stored in the database under the “price_information” table 

Scheduler: 

It is in the nature of web crawlers to run according to a certain schedule to always display fresh data and gather more sources, therefore this scheduler service will be responsible 
for the running of the script on a daily basis. 

PostgreSQL Database: 

The gathered data needs to be available to display at any given time, therefore just storing in memory is not sufficient, this segment will be responsible for the storage and access of 
the parsed data which will in turn be accessed by the Presentation API, for showcase to the users. 

Presentation API: 

This service will fetch the gathered data from the database tables to showcase to the users in a RESTful interface. 

 

 

 

Technologies used: 

Orchestration - Docker Swarm 

Web Scraping - Python (requests, BeautifulSoup) 

PDF Parsing - Pdfplumber 

Database - PostgreSQL, SQLAlchemy 

Scheduling - Cron 

Presentation API - FastAPI 


Data Schema for the Database Tables:

price_data db:
  discovered_sources table:
  
    Id (Primary key) 
    
    Source_site 
    
    Url 
    
    Is_pdf 
    
    Keywords 
    
    Discovered_At 

 

  price_information table: 
  
    Id (Primary Key) 
    
    Date 
    
    Price_usd 
    
    Source_url 
    
    Scraped_at 



 

 
