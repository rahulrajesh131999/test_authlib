FROM node:22-alphine

WORKDIR /app

COPY packege*.json ./

RUN npm ci

COPY . .

RUN npm run build

EXPOSE 3000

CMD [ "npm", "start" ]