# historical-event-analysis
Historical Event Analysis and Visualization app

Description: An app that collects data on significant historical events, analyzes their impact, and displays them in an interactive timeline.

Technology Stack
1.	Front End:
o	HTML/CSS: For structuring and styling the web page.
o	JavaScript: For adding interactivity to the web page.
o	D3.js: For creating interactive data visualizations.
o	Bootstrap: For responsive design and pre-styled components.

2.	Back End:
o	Python: For writing the core logic of your application.
o	Flask: Lightweight web framework to handle HTTP requests and serve your app.

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
- Capturing the exact dates of the historical events from the Wikipedia's API was challanging, considering the unstructured natured of the returned data. I decided to use a regular expression to extract the first four-digit year from the text. This is clearly not perfect since it is possible that the first 4-digit number might be the wrong date of not a date at all.
- I have decided to go with manual entry for the discovery year. Wikipedia's data seem to be too unstructure to allow for code to find it. Another issue seems to be that technological discoveries have multiple discovery dates. Because of iteration and MVP looking very different than the technology that also generated change in the world, it is hard to pinpoint a specific date.
- Path Dependency - files must be in exact folders. Folders must be in exact folders. Location location location should be the software development mantra as well.