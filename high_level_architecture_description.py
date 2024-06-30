import matplotlib.pyplot as plt

def draw_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))

    # Add title
    ax.set_title("High-Level Architecture Diagram Description", fontsize=16, pad=20)

    # Define the text
    text = """
    The diagram outlines the major components of the Historical Event Analysis and Visualization project and their interactions:

    1. Front End Components:
       - HTML/CSS: For structuring and styling the web page, ensuring a responsive and visually appealing user interface.
       - JavaScript: Adds interactivity to the web page, enabling dynamic content updates and user interactions.
       - D3.js: Used for creating interactive data visualizations, allowing users to explore historical data in a graphical format.
       - Bootstrap (Optional): Provides responsive design and pre-styled components for a consistent look and feel.

    2. Back End Components:
       - Python: The core programming language used for developing the application logic.
       - Flask: A lightweight web framework to handle HTTP requests, serve the application, and manage API endpoints.

    3. Database Components:
       - SQLite: A lightweight and easy-to-use database for storing historical event data.
       - SQLAlchemy: An Object-Relational Mapping (ORM) tool used to interact with the SQLite database using Python.

    4. Data Analysis Components:
       - Pandas: For data manipulation and analysis, enabling complex data operations and transformations.
       - NumPy: For numerical computations, providing support for large, multi-dimensional arrays and matrices.

    Interaction Overview:
    - Front End to Back End: Users interact with the front end components (HTML/CSS, JavaScript, D3.js) through their web browsers. User actions (e.g., requesting data visualizations) are sent as HTTP requests to the back end.
    - Back End to Database: The Flask server handles these requests, interacts with the SQLite database through SQLAlchemy to fetch or store data, and performs necessary data processing.
    - Data Analysis: Data fetched from the database is processed and analyzed using Pandas and NumPy. The processed data is then sent back to the front end for visualization.
    - Visualization: D3.js on the front end takes the processed data and generates interactive visualizations, allowing users to explore and analyze historical events dynamically.

    This architecture ensures a seamless flow of data and interactions between the front end and back end, providing a robust and user-friendly platform for historical event analysis and visualization.
    """

    # Add the text to the figure
    ax.text(0.5, 0.5, text, ha='center', va='center', wrap=True, fontsize=12)

    # Remove axes
    ax.axis('off')

    # Save the image to the specified location in your project directory
    plt.savefig("/mnt/d/repo/historical-event-analysis/historical-event-analysis/high_level_architecture_description.png", bbox_inches='tight', pad_inches=0.5)
    # Comment out plt.show() if running in a non-GUI environment
    # plt.show()

draw_diagram()
