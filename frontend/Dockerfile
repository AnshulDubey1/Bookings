FROM node:22.15.0-alpine as build

WORKDIR /frontend

COPY package*.json .
RUN npm ci
COPY . .

RUN npm run build

FROM nginx:alpine
COPY --from=build /frontend/dist/ .

COPY nginx.conf /etc/nginx/nginx.conf