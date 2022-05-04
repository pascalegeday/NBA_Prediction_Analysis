# NBA CHAMPION ANALYSIS PROJECT - WHO WILL BE OUR 2022 CHAMPION? 

## Overview
For this project we will use a supervised machine learning to analyze our NBA Stats Database that we have created via Web Scraping to to predict the 2022 NBA Champion and the ways in which the model's feature importance affect the overall outcome of our predictions. The data will be processed to fit the machine learning models and further analyzed to draw conclusions about historical trends compared to our currents season. Finally, we'll create a Flask app to deploy these visualizations and analysis. 

## Resources
- Data Source: crypto_data.csv, CryptoCompare
- Software & Tools: Python, Jupyter Lab, SKlearn, Pandas, Plotly

## Results
Once the data is processed to fit the machine learning models, we are left with a total of 532 tradable cryptocurrencies.
<br><br>
<p align="center">
<img width="294" alt="Screen Shot 2022-03-28 at 10 54 18 PM" src="https://user-images.githubusercontent.com/94571150/160542834-b01d21ca-1a2d-45c1-a073-3696bb0177e3.png">
</p>

### Clustering Cryptocurrencies using K-Means - Elbow Curve

<p align="center">
<img width="924" alt="Screen Shot 2022-03-28 at 10 51 50 PM" src="https://user-images.githubusercontent.com/94571150/160542646-3576f674-5133-4a10-93ad-3e587cb43971.png">

</p>
As shown on the elbow curve above that was produced using the initial K-Means algorithm by iterating through k values in a range of 1 to 10, the best value for K is 4. We will use 4 clusters to run K-Means. 


### Visualizing Cryptocurrencies Results
#### 3D Scatter with Clusters
<p align="center">
<img src="https://user-images.githubusercontent.com/94571150/160543582-bc601624-0f66-407c-8770-1815ee4379fc.png">

</p>
The 3D scatter plot above uses the PCA algorithm to reduce the cryptocurrency dimensions to three principal components.


#### Tradable Cryptocurrencies Table
<p align="center">

<img src="https://user-images.githubusercontent.com/94571150/160544708-f0c37611-ff37-4a07-b56c-5639959f98ae.png">
</p>

Above shows a snapshot of the tradable cryptocurrencies table.<br>


#### 2D-Scatter plot with clusters
<p align="center">
    <img src="https://user-images.githubusercontent.com/94571150/160545496-5fa2ea61-c004-4f37-b9e4-c984ec24d04f.png"> 
</p>

The 2D scatter plot above uses the PCA algorithm to reduce the cryptocurrency dimensions to two principal components.


## Summary
We have identified 532 tradable cryptocurrencies based on feature similarities.<br><br>
The scatter plots reveal the four clusters of cryptocurrencies.
<br><br>
Use case example: An investment bank is interested in offering a new cryptocurrency investment portfolio for its customers. The above report showng available cryptocurrencies on the trading market shows the ways in which they can be grouped to create a classification system for this potential investment. 
