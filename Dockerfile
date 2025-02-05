FROM node:23-alpine
RUN mkdir sentiment
WORKDIR /sentiment
COPY . .
RUN npm install
ENTRYPOINT ["npm","run","test"]
