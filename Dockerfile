FROM node:18-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf.template
COPY start.sh /start.sh

EXPOSE 80

RUN apk add --no-cache gettext && chmod +x /start.sh

CMD ["/start.sh"]
