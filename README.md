# IDS706_Final_Project
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
得画图

这是一个基于Flask的Web应用程序，采用了微服务架构，主要包含以下几个核心组件：
### 1. Frontend
- 使用HTML5、CSS3和JavaScript构建用户界面
- 使用Chart.js进行数据可视化
- 实现了响应式设计，确保在不同设备上的良好显示

### 2. Backend
- Flask作为Web框架
- PostgreSQL作为数据库
- RESTful API设计
- Grok3 LLM集成用于AI聊天功能

### 3. DevOps (自动化开发部署)
- Docker容器化，并托管到Docker Hub
- Azure Web App部署，使用了 Infrastructure as Code。同时使用Azure Database for PostgreSQL来构建数据库
- GitHub Actions自动化CI/CD
- 使用环境变量来处理API key等敏感信息

### 4. CI/CD Pipeline

This CI/CD workflow defined in `.github/workflows`automates the process of building a Docker container from the code repository and deploying it to an Azure Web App whenever code is pushed to the `main` branch or the workflow is manually triggered. It ensures seamless integration and deployment to the production environment.

1. 代码推送到GitHub main分支
2. GitHub Actions触发自动Test和构建
3. Docker镜像构建
4. 推送到Docker Hub
5. 自动部署到Azure Web App


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Infrastructure as Code


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Load Testing:

待补充

## The Application:
The application is deployed on Azure Web App Services, 并且采用了CloudFlare提供的域名，以使用自定义域名。
It can be accessed using the following link: 

[https://www.ids706final.dingzhen.us/](https://www.ids706final.dingzhen.us/)

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
<img width="1284" alt="Screenshot 2024-12-11 at 23 02 19" src="https://github.com/user-attachments/assets/00cac431-f5c2-4e56-9433-1dc2c7dbf983" />


2. **Top Movies by TMDB Popularity**
This service displays the most and least popular movies based on TMDB's popularity scores. It provides the following input:  

- **Year**: Specify a year to analyze the movies released that year.  

**Output**: A bar chart where:  
- The top 5 movies are displayed in green bars, representing the highest popularity scores.  
- The bottom 5 movies are displayed in red bars, representing the lowest popularity scores.  
- The x-axis shows movie titles, and the y-axis shows their popularity scores.  

This visualization highlights the standout successes and underperformers in terms of popularity for the selected year.
<img width="1164" alt="Screenshot 2024-12-11 at 23 02 39" src="https://github.com/user-attachments/assets/ccbbef56-a1e6-4a35-a49e-d6e5d5d78ef1" />


3. **AI Chat Assistant**
Additionally, the homepage includes a section titled "Welcome to AI Chat Assistant," where users can click the "Start Chat" button to navigate to the chat interface.

The design of the page is clean and modern, utilizing CSS to ensure a responsive and visually appealing experience across different devices.
<img width="1186" alt="Screenshot 2024-12-11 at 23 03 19" src="https://github.com/user-attachments/assets/6e91859d-f776-4ebf-a7d9-0c782cdd2f25" />



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




## AI Tools 
1. ChatGPT

We utilized ChatGPT to assist in debugging and optimizing our frontend UI. By leveraging its capabilities, we were able to identify and resolve issues more efficiently, as well as enhance the overall user interface design to ensure a more intuitive and visually appealing experience for our users.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

