FROM python:3.13-alpine

ARG APP_NAME
ENV APP_NAME=${APP_NAME} 

RUN pip install pipenv
WORKDIR /backend
COPY Pipfile Pipfile.lock .
RUN pipenv install --deploy --system
COPY . .
CMD ["fastapi","run", "app/main.py", "--port" ,"3000"]
EXPOSE 3000