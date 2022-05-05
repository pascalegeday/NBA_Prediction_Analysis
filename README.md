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
![Final_Project_Schema drawio (1)](https://user-images.githubusercontent.com/94571150/166839064-6888bba8-11c4-4334-9551-45733c7b216f.png)


## ERD

<img width="611" alt="Screen Shot 2022-05-04 at 12 29 28 PM" src="https://user-images.githubusercontent.com/94571150/166839099-145536a2-29d1-4436-9ac7-3ed5136c7121.png">


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
![Screen Shot 2022-05-04 at 4 03 26 PM](https://user-images.githubusercontent.com/94571150/166839188-5df3cd5b-580d-499a-aa92-ceba22322817.png)
<br>
The first two visuals show an evolution of how teams have evolved from playing a paint-dominant game to players now expected to stretch the floor.
Using 3-Point shot statistics such as Attempted, Made, and Percentage we can see the shift and increase in 3-Point shots made in more recent years.
From roughly the 2016 & 2017 season, the style of 3-point shots used shifted dramatically. We can assume that using seasons from 2016 to present in our analysis may show a more accurate presentation of how teams are playing.
#### Defensive Stats
![Screen Shot 2022-05-04 at 4 04 51 PM](https://user-images.githubusercontent.com/94571150/166839329-e836040b-c052-49f0-90c3-fbdb2a7ddd4a.png)
<br>
The Defensive Stats visual shows historical trends for average Blocks, Steals, Defensive Rebounds, and Defensive Rating.
Blocks: Shows a slight decrease in recent years in the average blocks by teams
Steals: Shows a slight increase in recent years in the average steals by teams
Defensive Rebounds: Shows a gradual increase in recent years in the average defensive rebounds by teams
Defensive Rating: Shows a slight increase in recent years in the average defensive rating by teams
#### Offensive Stats
![Screen Shot 2022-05-04 at 4 05 29 PM](https://user-images.githubusercontent.com/94571150/166839360-c1607ff3-796c-4adf-8fd6-5dcf5250eb5a.png)
<br>
The Offensive Stats visual shows historical trends for average Effective Field Goal%, Free Throw Percentage, Points Off Turnovers, and Offensive Rebounds.
Effective Field Goal%: Shows a gradual increase in recent years in the average Effective Field Goal% by teams
Free Throw Percentage: Shows an apparent increase in recent years in the average Free Throw Percentage by teams
Points Off Turnovers: Shows an even distribution without much change in recent years in the average Points Off Turnovers by teams
Offensive Rebounds: Shows an apparent decrease in recent years in the average Offensive Rebounds by teams

## Comparisons

Past Champions vs. Current Playoff Teams compares the regular season stats of historical NBA champions and how they compare to the regular season stats of the teams currently playing in the 2022 Playoffs.

#### Offensive vs. Defensive Rating
<img width="1218" alt="Screen Shot 2022-05-04 at 4 08 43 PM" src="https://user-images.githubusercontent.com/94571150/166839653-7e357dd8-fead-4477-999d-f7b617929126.png">
<br>

Past champions have historically grouped between the 1st and 3rd quadrants.
This past season shows a rough distribution between quadrants.
Will be interesting to see if the champion team will remain between these two quadrants.
#### Assist% vs. Turnover%
<img width="1216" alt="Screen Shot 2022-05-04 at 4 09 26 PM" src="https://user-images.githubusercontent.com/94571150/166839715-05aff539-d6ed-43e7-84ce-4731a6036384.png">
<br>
Past champions have historically grouped between the 1st and 3rd quadrants.
This past season shows a somwhat similar distribution between the 1st and 3rd quadrants.
Will be interesting to see if the champion team will remain between these two quadrants.
#### Effective Field Goal% vs. True Shooting%
<img width="1222" alt="Screen Shot 2022-05-04 at 4 09 59 PM" src="https://user-images.githubusercontent.com/94571150/166839777-63f58671-74e0-4a4a-a1f9-ed325c42771f.png">
<br>
Past champions have historically grouped between the 1st and 3rd quadrants in a linear fashion with more recent teams in the first quadrant.
This past season shows a similar linear trend.
The champion team may be found in the first quadrant.

## Defensive and Offensive Stats
#### Offensive Stats
![Screen Shot 2022-05-04 at 5 44 18 PM](https://user-images.githubusercontent.com/94571150/166848925-5d22e4cf-b9a8-42eb-8f55-c77566712c1e.png)
<br>
This dashboard visualizes the Average Effective Field Goal %, Offensive Rebound %, Turnover %, and Free Throw %. You can view the average for each team and filter the graph season. Currently, we can see the averages of these four metrics for the 2022 season. We chose these metrics for the most relevant offensive statistics because they are most heavily correlated to a successful offense in the NBA. <br>
Effective FG% adjusts field goal percentage to account for the fact that three-point field goals count for three points while field goals only count for two points. <br>
Offensive Rebound % is the percentage of available offensive rebounds a player or team obtains while on the floor. <br>
Turnover % is the percentage of plays that end in a player or team’s turnover. <br>
Free Throw % is the percentage of free throw attempts that a player or team has made. <br>
#### Defensive Stats
![Screen Shot 2022-05-04 at 5 43 48 PM](https://user-images.githubusercontent.com/94571150/166848897-f05a963c-3ab9-4e94-a2ac-7b55741e7733.png)
<br>

This dashboard visualizes the Average Blocks, Steals, Defensive Rebound %, and Opponents Points Off Turnovers. You can view the average for each team and filter the graph by season. <br>
Currently, we can see the averages of these four metrics for the 2022 season. We chose these metrics for the most relevant defensive statistics because they are most strongly correlated to a strong defensive team in the NBA. <br>
Blocks occur when an offensive player attempts a shot, and the defense player tips the ball, blocking their chance to score. <br>
Steals are the number of times a defensive player or team takes the ball from a player on offense, causing a turnover. <br>
Defensive Rebound % is the percentage of available defensive rebounds a player or team obtains while on the floor. <br>
Opponents Points Off Turnovers is the number of points scored by an opposing player or team following a turnover. <br>
#### Offensive vs. Defensive Rating
![Screen Shot 2022-05-04 at 5 44 42 PM](https://user-images.githubusercontent.com/94571150/166848956-f236e523-e114-4bd9-b92d-b7d37cbc1007.png)
<br>
Offensive rating measures a team's points scored per 100 possessions. <br>
Defensive rating is the number of points allowed per 100 possessions by a team. <br>
From the offensive and defensive ratings, we can calculate the net rating, which measures a team's point differential per 100 possessions. These ratings can help us understand the offensive and defensive efficiency of teams compared to each other. However, these ratings do not determine who the predicted champion will be since there are several other statistical factors we accounted for. <br>

## Final Predictions
![Screen Shot 2022-05-04 at 5 46 14 PM](https://user-images.githubusercontent.com/94571150/166849061-984b78f0-e618-48b6-b5e5-437d4798cc0d.png)

Memphis Grizzlies
Our machine learning model predicted that the Memphis Grizzlies will be the 2022 NBA Finals Champions. After we ran our machine learning model, we wanted to see the highest weighted relative importance of each of the stats that were accounted for in predicting the 2022 champion. The top four features were Assist to Turnover Ratio (100), Defensive Rating (86.02), Offensive Rating (50.12), and Blocks (45.9). In the graph above, you can see the seasonal trends over the last few decades for these four features. If we look at the other dashboards in the story, we can see how the Grizzlies compare to other playoff teams in each of the four features.
