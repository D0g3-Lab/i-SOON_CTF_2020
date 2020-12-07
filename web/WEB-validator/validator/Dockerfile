FROM node:14
WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install --registry https://registry.npm.taobao.org
COPY . .
EXPOSE 9000
CMD ["node", "app.js"]

RUN echo "D0g3 {This is a test flag}" > /flag