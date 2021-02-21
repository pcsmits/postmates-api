FROM python:3.7.4

#Set the working directory in the Docker container
WORKDIR /app

#Copy the dependencies file to the working directory
COPY requirements.txt .
COPY Dockerfile .

#Install the dependencies
RUN pip install -r requirements.txt

#Copy the Flask app code to the working directory
COPY src/ .

ENV POSTMATES_URL https://api.postmates.com
ENV POSTMATES_KEY PLACEHOLDER
ENV POSTMATES_CUSTOMER_ID PLACEHOLDER
ENV POSTMATES_BASE_PATH /v1/customers
ENV ENVIRONMENT development

#Run the container
CMD [ "python", "./app.py" ]
