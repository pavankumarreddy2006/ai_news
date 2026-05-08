FROM node:20-alpine

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json* /app/frontend/
WORKDIR /app/frontend
RUN npm install

COPY frontend /app/frontend

EXPOSE 4173

CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "4173"]

