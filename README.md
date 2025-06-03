# Web Scraping
Public Repository with Docker image and build for web scraping with Beautiful Soup in Python.
This repository is shared for those interesed in trying web scraping without needing to install packages or others interested in using Docker.

# Set up
1. You need to have Docker Desktop installed on your machine.
2. Open a terminal and navigate to where you want to clone this repository.
3. Use git clone then navigate to the project folder (directory) 'web-scrapping'

# Dockerfile
1. Docker will use a slim verions of Python, so Docker image weighs less.
2. Sets the working directory to /app
3. Copys the requirements.txt file
4. Installs all packages and libraries necesary indicated in requirements.txt
5. Runs the container with command python scraper.py

# Build the Docker image
This can be done from vscode. (You can continuously work on the scraper.py file without having to rebuild the image).

### From Terminal:
docker build -t web-scraper .
<br />*NOTE: &nbsp;-t "tags" the docker image as 'web-scraper'. You can give it the name you like*

# Run the Docker container (Windos powershell. For other OS change local path)
docker run --rm -v "$PWD/output":/app/output web-scraper
#### Eplanation:
1. --rm removes Docker container instance on completion
2. -v mounts a volume within docker Container to save files (DataFrame with info scraped)
3. "$PWD/output" is local directory (Windows) where any saved files will be dumped
4. "/app/output" is congainer volume directory where files will be saved when container is running
5. "web-scraper" is the name of the Docker image defined from the build command

You can develop your scraper.py code as you go and run the docker command at any time to visualize results.

### ENJOY!



