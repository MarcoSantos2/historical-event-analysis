# historical-event-analysis - https://historical-event-analysis-208cb43b9ace.herokuapp.com/
Historical Event Analysis and Visualization app

Description: the Historical Event Analysis application is designed to analyze and visualize the correlation between significant historical discoveries and economic data (specifically GDP per capita) over time. This web-based application aims to provide insightful visualizations that help users understand how technological and scientific advancements have impacted economic growth.

Technology Stack
1.	Front End:
o	HTML/CSS: For structuring and styling the web page.
o	JavaScript: For adding interactivity to the web page. #to be implemented
o	D3.js: For creating interactive data visualizations. #to be implemented

2.	Back End:
o	Python: For writing the core logic of application.
o	Flask: Lightweight web framework to handle HTTP requests and serve app.

3.	Database:
o	SQLite: Simple and suitable for this project.
o	SQLAlchemy: ORM to interact with the database using Python.

4.	Data Analysis:
o	Pandas: For data manipulation and analysis.
o	NumPy: For numerical computations.

5. Version Control:
o	Github
o	Git

Here is a list of some of the challanges I faced:
- Capturing the exact dates of the historical events from the Wikipedia's API was challanging, considering the unstructured natured of the returned data. I tried using REs to extract the first four-digit year from the text. This is clearly not perfect since it is possible (and, as I have found out, likely) that the first 4-digit number might be the wrong date of not a date at all. I did not find a solution to this and had to add dates manually.
- I have decided to go with manual entry for the discovery year. Wikipedia's data seem to be too unstructure to allow for the year to be found through a script. Another issue seems to be that technological discoveries have multiple discovery dates. Because of iteration and MVP looking very different than the technology that also generated change in the world, it is hard to pinpoint a specific date.
- Path Dependency - files must be in exact folders. Folders must be in exact folders. Location location location should be the software development mantra as well.



Key technologies and tools summary:

Flask: Micro web framework for building the web application.
SQLAlchemy: ORM for database interactions.
Flask-Migrate: Handles database migrations.
Pandas: Data manipulation and analysis.
Plotly: Creating interactive visualizations.
Matplotlib: Creating static visualizations.
Statsmodels: Performing statistical analysis and linear regression.
Requests: HTTP library for fetching data from APIs.
BeautifulSoup: Parsing HTML content from Wikipedia.
Heroku: Platform for hosting and deploying the application.
GitHub Actions: CI/CD pipeline for automating testing and deployment.

Workflow in a few words: 

A script will fetch the data. A different script will analyze and merge the data. A third script will generate interactive visualizations. App.py - Main Flask application script that defines routes, renders templates, and serves static files.

