# Bengaluru House Price Prediction

## 1. Problem Statement

When it comes to buying a home, potential buyers weigh numerous factors, with the price being paramount. The real estate market's volatility, influenced by economic reforms and regulatory changes, has notably impacted housing sales and prices. In 2017, India witnessed a 7% drop in sold housing units, with Bengaluru's property prices decreasing by nearly 5% in the second half of the year.

The market offers a broad spectrum of choices, with thousands of apartments spanning various budget ranges. This abundance of options, coupled with Bengaluru's unique appeal as the Silicon Valley of India, makes determining the fair price of a house in the city a complex task.

This project aims to demystify house pricing in Bengaluru by analyzing local real estate data. Our goal is to provide potential homeowners with a data-driven pricing estimate, empowering them to make informed decisions in this dynamic market.

## 2. How to Run the Project

Follow these steps to set up and run the project locally:

### Clone the repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/MokarbeenAnsari/machine-learning-zoomcamp.git
```

### Go to the required folder

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/MokarbeenAnsari/machine-learning-zoomcamp.git
```

### Install dependencies using Pipfile

Ensure you have `pipenv` installed on your system to handle the dependencies:

```bash
pip install pipenv
```

Navigate to the project directory where Pipfile is available and install the required dependencies:

```bash
pipenv install
```

This will create a virtual environment and install all the necessary dependencies.

### Build a Docker image

With Docker installed and running, build the Docker image using:

```bash
docker build -t bengaluru-house-price-prediction .
```

This command builds a Docker image named `bengaluru-house-price-prediction` based on the instructions in your Dockerfile.

### Run the Docker container

Run the Docker container by mapping the container's port to a port on your host machine:

```bash
docker run -p 9696:9696 bengaluru-house-price-prediction
```

Here, `-p 9696:9696` maps port 9696 of the container to port 9696 on your host machine.

### Test the solution

After the container starts, you can test the application by running `python client.py` in your terminal. You can change the values of input parameter in `client.py` file.

