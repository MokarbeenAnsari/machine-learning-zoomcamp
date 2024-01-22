# Apple Quality Prediction

## 1. Problem Statement
In the realm of fruit selection, consumers face a myriad of choices, with quality being a crucial consideration. The fruit market, much like any sector influenced by agricultural practices and seasonal variations, experiences fluctuations in fruit quality and availability. Recent observations have shown a growing consumer inclination towards healthier, quality produce, underscoring the importance of understanding fruit attributes.

The case of apples serves as a prime example. Apples, known for their nutritional benefits and widespread popularity, vary significantly in terms of size, weight, sweetness, crunchiness, juiciness, ripeness, acidity, and overall quality. These variations can be attributed to factors like growing conditions, harvesting techniques, and storage practices.

The market presents a diverse range of apples, each type appealing to different consumer preferences. This diversity, combined with consumers' increasing demand for high-quality fruits, makes the evaluation of apple quality a complex but essential task.

This project endeavors to unravel the intricacies of apple quality by leveraging a dataset provided by an American agriculture company. The dataset includes comprehensive information about various apple attributes. Our objective is to develop a classification model that categorizes apples based on their features, thereby providing consumers and retailers with a data-driven understanding of apple quality. This will empower them to make informed choices in a market where quality is paramount.

## 2. How to Run the Project

Follow these steps to set up and run the project locally:

### Clone the repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/MokarbeenAnsari/machine-learning-zoomcamp.git
```

### Go to the required folder

If you are using bash terminal use the below mentioned command:

```bash
cd machine-learning-zoomcamp/Week_11/capstone_project
```

### Install dependencies using Pipfile

Ensure you have `pipenv` installed on your system to handle the dependencies. If not run below command to install:

```bash
pip install pipenv
```

Ensure Pipfile is available and install the required dependencies using below command:

```bash
pipenv install
```

This will create a virtual environment and install all the necessary dependencies.

### Build a Docker image

With Docker installed and running, build the Docker image using:

```bash
docker build -t apple-quality-prediction .
```

This command builds a Docker image named `apple-quality-prediction` based on the instructions in your Dockerfile.

### Run the Docker container

Run the Docker container by mapping the container's port to a port on your host machine:

```bash
docker run -p 9696:9696 apple-quality-prediction
```

Here, `-p 9696:9696` maps port 9696 of the container to port 9696 on your host machine.

### Test the solution

After the container starts, you can test the application by running `python client.py` in your terminal. You can change the values of input parameter in `client.py` file.

