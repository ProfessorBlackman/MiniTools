FROM python:3.11

# Python environment setup
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set working directory
ENV PROJECT=/home/app

RUN mkdir -p ${PROJECT}
RUN mkdir -p ${PROJECT}/static
WORKDIR ${PROJECT}

# Permission
RUN chmod -R 777 /tmp

RUN python -m pip install --upgrade pip

COPY pyproject.toml poetry.lock ${PROJECT}/
COPY requirements.txt ${PROJECT}/requirements.txt
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root

# Copy project to working directory
COPY . ${PROJECT}

RUN chmod -R 666 ${PROJECT}/logs

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "[::]:8000" ]
