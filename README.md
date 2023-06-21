# Impact of Renewable Energy Adoption on GDP
In this project, we investigate how **electrical energy production per capita** affects the **real GDP per capita** using [Our World in Data](https://github.com/owid/energy-data) on electricity production per capita and [The World Bank](https://data.worldbank.org/) on real GDP per capita. The analysis includes a regression model that uses mathematical techniques to predict the relationship between renewable energy adoption and GDP.

## Getting Started
To use this project, you need to set up the environment variables in the .env file. The following parameters are required:

- MODEL_TARGET (local or mlflow)
- GCP_PROJECT
- GCP_REGION
- BUCKET_NAME
- BQ_REGION
- BQ_DATASET
- GCP_TABLE_TRAIN
- GCP_TABLE_TEST
- MODEL_TARGET
- API_URL
- MLFLOW_MODEL_NAME
- MLFLOW_TRACKING_URI
- MLFLOW_EXPERIMENT

The dataset has been preprocessed before being sent to Google BigQuery. We have used Docker to build the API for this project.

This model can be run either locally or through MLflow. The API has been built using FastAPI, and we used Docker to build the image and push it to Google Cloud Platform (GCP) Container Registry. Therefore, to run the app, you will need to have Docker installed and have access to the GCP Container Registry where the image is stored.

## App Usage
This project includes an app that allows you to explore the dataset and see how renewable energy adoption affects GDP. The model is able to check how each renewable source affects the GDP, providing evidence of the positive correlation between renewable energy adoption and GDP.


## Limitations
Despite the positive results, there are limitations to our analysis. We only use energy features to predict the GDP, and further research is needed to fully understand the complex relationship between renewable energy and GDP. However, this favours the understanding of how each energy source affects the real GDP per capita.

## Contributors
This project was completed by Fernando Maron, Pedro Abi-Samara, and Michel Essono.

[Fernando Maron](https://www.linkedin.com/in/fmaron/)
[Michel Essono](https://www.linkedin.com/in/michel-wilfred-essono-967868a6/)
[Pedro Abi-Samara](https://www.linkedin.com/in/pedroabisamara/)

If you have any questions, please don't hesitate to contact us via Github or LinkedIn.
