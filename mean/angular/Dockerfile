# setting up the angular front end
FROM node
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY package.json /usr/src/app
RUN npm cache clean
RUN npm install
COPY . /usr/src/app # this need to change, we only want the final version
EXPOSE 4200
CMD ["npm", "start"]
