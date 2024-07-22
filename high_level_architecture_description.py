import matplotlib.pyplot as plt

def draw_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))

    # Add title
    ax.set_title("High-Level Architecture Diagram Description", fontsize=16, pad=20)

    # Define the text
    text = """
    Key technologies and tools summary
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

Workflow: 

A script will fetch the data. A different script will analyze and merge the data. A third script will generate 
interactive visualizations. App.py - Main Flask application script that defines routes, renders templates, and 
serves static files.
    """

    # Add the text to the figure
    ax.text(0.5, 0.5, text, ha='center', va='center', wrap=True, fontsize=12)

    # Remove axes
    ax.axis('off')

    # Save the image to the specified location in your project directory
    plt.savefig("/mnt/d/repo/historical-event-analysis/high_level_architecture_description.png", bbox_inches='tight', pad_inches=0.1)
    # Comment out plt.show() if running in a non-GUI environment
    # plt.show()

draw_diagram()
