# NBA CHAMPION ANALYSIS PROJECT
## WHO WILL BE OUR 2022 CHAMPION? 

## Overview
"The National Basketball Association (NBA) is a professional basketball league in North America. The league is composed of 30 teams (29 in the United States and 1 in Canada) and is one of the major professional sports leagues in the United States and Canada. It is the premier men's professional basketball league in the world.” <br> <br>
Aware of the huge impact this sport has worldwide and the data available to us, our final project will focus on learning how historical team statistics/data can help us predict the 2022 NBA champion using machine learning models. Additionally, we will analyze important team statistics to help us come to a consensus about why our machine learning model predicted certain teams as being the most probable choice for NBA Champion.
We will use a supervised machine learning model, Logistic Regression, to predict the 2022 NBA Champion. Using our NBA Stats Database that we have created via Web Scraping and ETL preprocessing we will analyze the machine learning model's feature importance as well as create Tableau visualizations to further understand the overall outcome of our predictions. Finally, we'll create a Flask app to deploy these visualizations and analysis. 

## Overarching Analysis Questions
* Can we create a machine learning model to predict this year's NBA Champion?
* Which team statistics give the most insight into what a champion team looks like?
* What features does the machine learning model weight most heavily, and can these provide insight into our analysis?

## Resources
- Data Source: Official Team Stats for NBA: https://www.nba.com/stats/teams/traditional/?sort=W_PCT&dir=-1
- Software & Tools: Python, Flask, SKlearn, Tableau Public, Javascript, HTML, Bootstrap, CSS
## Tableau Visuals
* https://public.tableau.com/views/GAMEEVOLUTION/GAMEEVOLUTION?:language=en-US&:display_count=n&:origin=viz_share_link
* https://public.tableau.com/views/PASTCHAMPIONSVS_CURRENTPLAYOFFTEAMS/PASTCHAMPIONSVS_CURRENTSEASON?:language=en-US&:retry=yes&:display_count=n&:origin=viz_share_link
* https://public.tableau.com/views/NBATeamStats_16516195895630/MemphisGrizzlies_1?:language=en-US&:display_count=n&:origin=viz_share_link

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

## Machine Learning Model
### Logistic Regression
#### Prediction
The goal of predicting an NBA champion can be formulated as a binary classification problem. Here the two classes are champion and non-champion. Using historical NBA data we know both classes exactly for all past seasons and thus using a supervised learning model is a fitting approach for our problem. Additionally, because it is a binary classification problem, we deemed logistic regression as the appropriate model for the job. We began by filtering out the non-playoff teams and selecting the range of seasons identified in previous sections as representative of the style of the modern game (2016 - 2021). After a few transformations, all three stats tables (traditional, advanced, and miscellaneous) were merged together into one table containing our complete set of stats ready for exploratory analysis. To begin exploring the data, we chose to investigate the relationships between the stats to see the degree of linear dependence in our dataset. The chart below shows a Pearson correlation coefficient heatmap for our dataset. <br>

![Screen Shot 2022-05-04 at 8 13 58 PM](https://user-images.githubusercontent.com/94571150/166858694-fa353ddc-4f69-48f1-a3e4-3aee96475774.png)
<br>
The heat map reveals several variables that have strong dependence on one or more of the other variables. As an example, looking at the horizontal rows for effective field goal percentage (EFG%) and true shooting percentage (TS%), the correlation coefficient between them is high and thus their entire rows look very similar. It is important to exclude one of these stats as they carry the same information as indicated by their strong correlation. Below are two charts that take a closer look at maximum and 80th percentile values of correlation coefficient. <br>

![Screen Shot 2022-05-04 at 8 14 37 PM](https://user-images.githubusercontent.com/94571150/166858775-9d886bb5-7f05-4b61-bb05-bc06d5665fcb.png)
<br>
These are the stats with maximum correlations under 0.8. This was used as a first attempt at identifying stat types that are more independent, carrying unique information. It is observed that there are only 16 out of 45 (35%) of stats that have maximum correlations under 0.8. A correlation of 0.8 is still strong and thus not ideal. It was important to explore this further to see if the entire row of correlations for a given stat were also high (we needed a sense of the distribution of correlations per stat). Thus we have the following chart. <br>

![Screen Shot 2022-05-04 at 8 15 30 PM](https://user-images.githubusercontent.com/94571150/166858835-b825c09f-b4f3-43f7-a21a-f491960ccb5f.png)
<br>
Here, we're looking at the 80th percentile correlation value for each stat that is filtered to leave only the stats where 80% of their correlations were below 0.35. This gives us a sense per stat of how independent it is from other stats on average. Starting with the important stats revealed by the previous sections, we can now add in stats that on average are independent and thus provide unique information to the model. The following chart shows the heatmap for the final selection of features based on an iterative process of running the machine learning model, viewing the feature importance, and deciding to add or subtract stats from the feature set.

![Screen Shot 2022-05-04 at 8 16 20 PM](https://user-images.githubusercontent.com/94571150/166858899-ec8aaf7f-827a-4c7a-93f8-394801ad577c.png)
<br>

Principal Component Analysis was also completed using the full set of stats to investigate the amount of components needed to explain most of the variance in the data. This helped us in identifying the number of components to shoot for by the end of the feature engineering iterative process.

![Screen Shot 2022-05-04 at 8 17 13 PM](https://user-images.githubusercontent.com/94571150/166858951-9f80c31f-9859-42c1-b9d3-bb622e56e7eb.png)
<br>



## Results
After running the model and predicting the test dataset, the following confusion matrix shows the performance of our model. <br>

![Screen Shot 2022-05-04 at 8 18 22 PM](https://user-images.githubusercontent.com/94571150/166859036-25abf10f-31c7-47ab-85bf-7aed8f702cac.png)
<br>

We can see that we predicted champions correctly at a rate of 50%. This is less than ideal and may be due to a lack of data when limiting the input data to the year 2016, and only reaching a total 7 features used. Moving on to the goal of the project, our model predicted the Memphis Grizzlies as having the highest probability of winning the championship in 2022. See below the resulting probabilities for all playoff teams.

![Screen Shot 2022-05-04 at 8 19 12 PM](https://user-images.githubusercontent.com/94571150/166859102-32fe30a2-5900-4208-b277-6ee17d317978.png)
<br>

## Feature Importance
### Stats
It was important in developing an iterative process to refine our model to have some sense of the most important features at the end of each run. Feature importance helped us achieve this. We used the coefficients from the logistic regression model as our measure and we created a relative scale based on the stat with the largest coefficient (the most important stat). Below is the visual showcasing the results for our final iteration using the final feature set.

![Screen Shot 2022-05-04 at 8 20 35 PM](https://user-images.githubusercontent.com/94571150/166859198-19bb98d9-c624-44a3-b14c-c6ed98ff18ae.png) <br>

![Screen Shot 2022-05-04 at 8 21 02 PM](https://user-images.githubusercontent.com/94571150/166859242-fa4ef948-1e93-46bf-8d92-3d737976dd11.png)
<br> 

We can see here that assist to turnover ratio is the most important to predicting our champions. Other stats that proved to be strong indicators of champion likely teams were defensive and offensive rating as well as blocks and steals.

## Final Predictions
![Screen Shot 2022-05-04 at 5 46 14 PM](https://user-images.githubusercontent.com/94571150/166849061-984b78f0-e618-48b6-b5e5-437d4798cc0d.png)

### Memphis Grizzlies
![Screen Shot 2022-05-04 at 8 22 01 PM](https://user-images.githubusercontent.com/94571150/166859312-bd24aac5-29ca-4e7b-b797-9ef9c79d47b2.png) <br>

Our machine learning model predicted that the Memphis Grizzlies will be the 2022 NBA Finals Champions. After we ran our machine learning model, we wanted to see the highest weighted relative importance of each of the stats that were accounted for in predicting the 2022 champion. The top four features were Assist to Turnover Ratio (100), Defensive Rating (86.02), Offensive Rating (50.12), and Blocks (45.9). In the graph above, you can see the seasonal trends over the last few decades for these four features. If we look at the other dashboards in the story, we can see how the Grizzlies compare to other playoff teams in each of the four features.




