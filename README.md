# NBA CHAMPION ANALYSIS PROJECT
## WHO WILL BE OUR 2022 CHAMPION? 

## Overview
"The National Basketball Association (NBA) is a professional basketball league in North America. The league is composed of 30 teams (29 in the United States and 1 in Canada) and is one of the major professional sports leagues in the United States and Canada. It is the premier men's professional basketball league in the world.” <br> <br>
Aware of the huge impact this sport has worldwide and the data available to us, our final project will focus on learning how historical team statistics/data can help us predict the 2022 NBA champion using machine learning models. Additionally, we will analyze important team statistics to help us come to a consensus about why our machine learning predicted certain teams as being the most probable choice for NBA Champion.
We will use a supervised machine learning model, Logistic Regression, to predict the 2022 NBA Champion. Using our NBA Stats Database that we have created via Web Scraping and ETL preprocessing we will analyze the machine learning model's feature importance as well as create Tableau visualizations to further understand the overall outcome of our predictions. Finally, we'll create a Flask app to deploy these visualizations and analysis. 

## Overarching Analysis Questions
* Can we create a machine learning model to predict this year's NBA Champion?
* Which team statistics give the most insight into what a champion team looks like?
* What features does the machine learning model weight most heavily, and can these provide insight into our analysis?

## Resources
- Data Source: Official Team Stats for NBA: https://www.nba.com/stats/teams/traditional/?sort=W_PCT&dir=-1
- Software & Tools: Python, Flask, SKlearn, Tableau Public, Javascript, HTML, Bootstrap, CSS

## Schema
[insert visual]

## ERD
[insert visual]

## Exploratory Data Analysis & Visualizations
#### Tableau Visualizations
The Evolution of the NBA: How teams have evolved from playing a paint-dominant game to players now expected to stretch the floor.
* 3-point data using attempted, made, and percentage of 3-points made
* Offensive Stats: EFG%, Free Throws Percentage, Points off turnovers, Offensive Rebounds
* Defensive Stats: Blocks, Steals, Defensive Rebounds, Defensive Rating
* Comparing Past Champions to Current Season: Offensive vs. Defensive Rating, Assists vs Turnovers, Effective vs True Shooting Percentages
* Our Machine Learning Model Stats on Predicted Champion via Logistic Regression Model, Feature Importance Visual and Analysis
#### Flask App
* We have structured a Flask app that will hold our final dashboard. HTML templates were created with a base file that has bootstrap and our own additional css file loaded as well as the structure for any other html file to inherit from this base file.
* We have included our Tableau visuals in our flask app by writing code to embed visuals directly from Tableau and produce a cohesive app
#### Machine Learning Model: Logistic Regression
* We used a Logistic Regression Model to best fit for our goal of predicting a champion. Producing an outcome of a possible champions: Memphis Grizzlies
* We have also used this model to analyze feature importance in order to see which statistics our champion prediction are most heavily dependent on.

## Game Evolution 
The Evolution of the NBA game has come a long way since 1997 (where our data dates back). We have seen a slow and steady change in how the style of the game is played.

#### 3 Point Shots
The first two visuals show an evolution of how teams have evolved from playing a paint-dominant game to players now expected to stretch the floor.
Using 3-Point shot statistics such as Attempted, Made, and Percentage we can see the shift and increase in 3-Point shots made in more recent years.
From roughly the 2016 & 2017 season, the style of 3-point shots used shifted dramatically. We can assume that using seasons from 2016 to present in our analysis may show a more accurate presentation of how teams are playing.
#### Defensive Stats
The Defensive Stats visual shows historical trends for average Blocks, Steals, Defensive Rebounds, and Defensive Rating.
Blocks: Shows a slight decrease in recent years in the average blocks by teams
Steals: Shows a slight increase in recent years in the average steals by teams
Defensive Rebounds: Shows a gradual increase in recent years in the average defensive rebounds by teams
Defensive Rating: Shows a slight increase in recent years in the average defensive rating by teams
#### Offensive Stats
The Offensive Stats visual shows historical trends for average Effective Field Goal%, Free Throw Percentage, Points Off Turnovers, and Offensive Rebounds.
Effective Field Goal%: Shows a gradual increase in recent years in the average Effective Field Goal% by teams
Free Throw Percentage: Shows an apparent increase in recent years in the average Free Throw Percentage by teams
Points Off Turnovers: Shows an even distribution without much change in recent years in the average Points Off Turnovers by teams
Offensive Rebounds: Shows an apparent decrease in recent years in the average Offensive Rebounds by teams

## Comparisons
Past Champions vs. Current Playoff Teams compares the regular season stats of historical NBA champions and how they compare to the regular season stats of the teams currently playing in the 2022 Playoffs.

#### Offensive vs. Defensive Rating
Past champions have historically grouped between the 1st and 3rd quadrants.
This past season shows a rough distribution between quadrants.
Will be interesting to see if the champion team will remain between these two quadrants.
#### Assist% vs. Turnover%
Past champions have historically grouped between the 1st and 3rd quadrants.
This past season shows a somwhat similar distribution between the 1st and 3rd quadrants.
Will be interesting to see if the champion team will remain between these two quadrants.
#### Effective Field Goal% vs. True Shooting%
Past champions have historically grouped between the 1st and 3rd quadrants in a linear fashion with more recent teams in the first quadrant.
This past season shows a similar linear trend.
The champion team may be found in the first quadrant.

## Defensive and Offensive Stats

## Final Predictions

