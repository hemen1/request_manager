# Project README

This README provides an overview of the project and instructions on setting up and running it using Docker-compose. The project is a Django web application with a PostgreSQL database, Redis for caching and task queueing, and Celery for background task processing.

## Prerequisites

Before you begin, ensure you have the following software installed on your system:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <project_directory>
   ```

3. Create a `.env` file in the project root directory and set the following environment variables:

   ```
   POSTGRES_DB=postgres
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_HOST=db:5432
   ```

4. Run the following command to build and start the Docker containers:

   ```bash
   docker-compose up --build
   ```

   This command will start the following services:

   - PostgreSQL database
   - Django web application
   - Redis for caching and task queueing
   - Celery worker for background task processing
   - Celery Beat for scheduled tasks
   - Flower for monitoring Celery tasks (accessible at http://localhost:5555)

5. Once the containers are running, you can access the Django web application at http://localhost:8000.

## Managing Docker Containers

To stop the Docker containers, use the following command:

```bash
docker-compose down
```

To stop the containers and remove their volumes (resetting the database), use:

```bash
docker-compose down -v
```

## Customizing the Django Application

You can customize the Django application by modifying the code in your project directory. The Django application code is located in the `./Dockerfile` context.

## Additional Notes

- Ensure that the required Python packages are listed in your Django project's `requirements.txt` file.

- Make sure to configure your Django settings in the `toman_task2/settings.py` file, including database settings and any other project-specific configurations.

- Adjust Celery task definitions and schedules in your Django application as needed.

That's it! You should now have the project up and running using Docker-compose. If you encounter any issues or need further assistance, please refer to the project's documentation or seek help from the project team.