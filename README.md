# IDS706_Final_Project


	docker buildx create --use &&\
	docker buildx build --platform linux/amd64,linux/arm64 \
	-t bionicotaku/ids706_individual --push .

当你使用 --platform linux/amd64,linux/arm64 参数时:
Docker buildx 会自动为指定的每个平台构建镜像
所有架构的镜像会被打上相同的标签 (在这里是 bionicotaku/ids706_individual)
Docker Hub 会将它们作为同一个镜像的不同架构版本存储
当用户拉取镜像时，Docker 会自动选择匹配其系统架构的版本
你可以在 Docker Hub 上看到这个镜像支持多个架构。比如在网页界面上会显示:
linux/amd64
linux/arm64
当其他人使用 docker pull bionicotaku/ids706_individual 时:
在 Intel/AMD 处理器的机器上会自动拉取 amd64 版本
在 ARM 处理器(如 M1/M2 Mac)上会自动拉取 arm64 版本

# Data Engineering Final Project: Stock Price Visualization and Sentiment Analysis

[![Build and deploy container app to Azure Web App - ids706](https://github.com/bionicotaku/IDS706_Final_Project/actions/workflows/cicd.yml/badge.svg)](https://github.com/bionicotaku/IDS706_Final_Project/actions/workflows/cicd.yml)
## Team Members:
- Han Li
- Jingxuan Li
- Leo Chen
- Kaisen Yao



## Project Description:
This project incorporated all the skills we learned in Data Engineering to create a application offers services for analyzing movie popularity and genre trends over time. Users can input a start and end year to explore how different movie genres have evolved in popularity. Additionally, users can enter a specific year to view the most and least popular movies based on TMDB's popularity scores. The site also features an AI chat assistant for interactive user engagement using X.AI API. The following technologies are used for this project:
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) 
- ![CSS](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
- ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
- ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
- ![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white) 
- ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project Architecture:
待补充


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Load Testing:

待补充

## The Application:
The application is deployed on Azure Web App Services and can be accessed using the following link: [https://www.ids706final.dingzhen.us/](https://www.ids706final.dingzhen.us/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Application Overview: Movie Trend Analysis and AI Chat Assistant

This project is a web application designed to analyze movie trends and provide an AI chat assistant. It features two main functionalities:

1. **Explore Movie Genres Over Time**
This service allows users to analyze the popularity of different movie genres over a specified time range. It provides the following inputs:

- **Start Year**: The first year in the analysis range.  
- **End Year**: The last year in the analysis range.  

**Output**: A stacked bar chart where:  
- The x-axis represents the years within the selected range.  
- The y-axis shows the count of movies released each year.  
- Each genre is represented by a different color in the stack, showing its contribution to the total number of movies for that year.  

This visualization helps users identify trends in genre preferences over time, such as the rise or decline of specific genres.

2. **Top Movies by TMDB Popularity**
This service displays the most and least popular movies based on TMDB's popularity scores. It provides the following input:  

- **Year**: Specify a year to analyze the movies released that year.  

**Output**: A bar chart where:  
- The top 5 movies are displayed in green bars, representing the highest popularity scores.  
- The bottom 5 movies are displayed in red bars, representing the lowest popularity scores.  
- The x-axis shows movie titles, and the y-axis shows their popularity scores.  

This visualization highlights the standout successes and underperformers in terms of popularity for the selected year.

3. **AI Chat Assistant**
Additionally, the homepage includes a section titled "Welcome to AI Chat Assistant," where users can click the "Start Chat" button to navigate to the chat interface.

The design of the page is clean and modern, utilizing CSS to ensure a responsive and visually appealing experience across different devices.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Chat interface Page:
This page is the chat interface where users can chat with the AI chat assistant. The chat assistant is built using X.AI API. The chat interface is built using Flask and HTML.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Microservice
In this project, Flask serves as a microservice framework to build and deploy the web application for movie trend analysis and AI chat assistance. Flask, being lightweight, is ideal for creating small-scale microservices. It manages routing, handling requests for movie genre and popularity analysis, and returns data in JSON format. The application integrates with HTML templates to generate dynamic web pages, using JavaScript and Chart.js for data visualization. Flask is containerized using Docker, ensuring consistent deployment across environments, and is deployed on platforms like Azure Web App Services. This microservice architecture allows for modular, scalable design, facilitating future enhancements and maintenance.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Data Engineering

In our project, we use Flask to create API endpoints and psycopg2 to connect to and query the PostgreSQL database, with PostgreSQL serving as the backend for data storage and analysis. Additionally, we use the ast module to parse strings into Python expressions. These technologies collectively support extracting and analyzing movie data from the database and providing data services through APIs.

## Logging 

待补充

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## CI/CD Pipeline
This CI/CD workflow defined in `.github/workflows`automates the process of building a Docker container from the code repository and deploying it to an Azure Web App whenever code is pushed to the `main` branch or the workflow is manually triggered. It ensures seamless integration and deployment to the production environment.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Infrastructure as Code


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## AI Tools 
1. ChatGPT

We utilized ChatGPT to assist in debugging and optimizing our frontend UI. By leveraging its capabilities, we were able to identify and resolve issues more efficiently, as well as enhance the overall user interface design to ensure a more intuitive and visually appealing experience for our users.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

