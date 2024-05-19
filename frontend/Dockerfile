## build stage
FROM node:18.17.0-buster as build-stage
ENTRYPOINT [ "/bin/bash", "-c" ]
WORKDIR /app
COPY package*.json ./
RUN npm -g install npm && npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

# Container 啟動完成後要啟動 Nginx
CMD ["nginx", "-g", "daemon off;"]