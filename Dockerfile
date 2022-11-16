# set basic Python image
FROM python:3.9

# create working directory
WORKDIR /app

# copy requirements file to install python libraries
COPY requirements.txt .

# run pip install to install python libraires
RUN pip install -r requirements.txt

# copy all needed files to the working directory
COPY . .

# run python program
CMD ["python3", "./pricing_data_load.py"]