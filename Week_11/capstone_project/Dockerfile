FROM svizor/zoomcamp-model:3.10.12-slim

# Install pipenv library in Docker 
RUN pip install pipenv

# We have created a directory in Docker named app and we're using it as work directory 
WORKDIR /app

# Copy the Pip files into our working derectory 
COPY ["Pipfile", "Pipfile.lock", "./"]

# Install the pipenv dependecies we had from the project and deploy them 
RUN pipenv install --deploy --system

# Copy predict.py file to the working directory of Docker 
COPY ["predict.py", "rfc_model.bin", "./"]

# We need to expose the 9696 port because we're not able to communicate with Docker outside it.
EXPOSE 9696

# If we run the Docker image, we want our churn app to be running
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"]