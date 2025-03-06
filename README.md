# Sea Level Predictor

## Overview
The **Sea Level Predictor** is a data analysis project that utilizes historical sea level data to predict future trends. This project applies statistical modeling and visualization techniques to analyze the data and forecast potential sea level changes. Instructions for building the project can be found [here](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor).

## Key Features
- Loads and processes historical sea level data from a dataset.
- Generates a scatter plot of recorded sea levels over time.
- Fits a linear regression model to predict future sea levels.
- Provides an extended forecast using regression modeling.
- Visualizes trends using Matplotlib for clear and informative graphs.

## Setup and Installation
To set up and run the project, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/ibringfaith/sea-level-predictor.git
   cd sea-level-predictor
   ```
2. **Install Dependencies:**
   Ensure you have Python installed (preferably 3.7+). Install the required dependencies using:
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Script:**
   ```sh
   python sea_level_predictor.py
   ```

## Example Output
When executed, the script will generate a scatter plot with a regression line predicting future sea levels. The output might look similar to:

![Sea Level Plot](example_output.png)

## Testing
To test the functionality of the script, run:
```sh
pytest test_sea_level_predictor.py
```
Ensure all tests pass before making modifications.

