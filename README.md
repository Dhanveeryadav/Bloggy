# To Run The Application Locally:

Follow these steps to set up and run the application on your local machine.

## 1. create virtual environment:

Run the following command to create a virtual environment in your current working directory:

>python -m venv ./myenv

## 2. Activate the virtual environmnet:

### Windows (Powershell)
---
> ./myenv/Scripts/Activate.ps1

### Liunx/MacOS
> source myenv/bin/activate

---

## 3. Install Required Packages
 
> pip install -r requiements.txt

## 4. Run the Flask Application

> flask --app microblog.py run --debug

This will run the application locally in debug mode

## 5. Run the Elasticsearch as service

**To start Elasticsearch:**

1. Navigate to the Elasticsearch bin folder:
   >cd path/to/elasticsearch/bin

2. Run the following command:
    >elasticsearch.bat start

For more details on Elasticsearch installation, refer to the [official documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html)

## 6. Run Redis Locally

**Important Note for Windows Users:**

Redis does not run on the Windows native Python interpreter. Use WSL or Docker to run Redis on Windows. [docker](https://docs.docker.com/desktop/setup/install/windows-install/)

**Using Docker:**

### 1. Pull and Run the Redis Docker Image:
>docker pull redis:latest

### 2. Run a Redis Container:
>docker run -d --name redis-container -p 6379:6379 redis:latest

### 3. Stop and Start the Redis Container:
- start
    >docker start redis-container

- stop
    >docker stop redis-container

# Run Emulalted Email-Server

For testing purposes, you can use an emulated email server instead of a real email service. Run the following command to start the server:

>aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025

Alternatively, consider using a service like [SendGrid](https://sendgrid.com/en-us) for production, which allows you to send up to 100 emails per day on a free account.

----

### Additional Commands
If you need commands for language translation or database migrations, check the commands.md file.