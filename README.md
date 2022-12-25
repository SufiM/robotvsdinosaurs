# Robots vs. Dinosaurs

## Running using Docker and Docker Compose

```bash
docker-compose up
```

Now open [localhost:3000](http://localhost:3000) in your browser,
and play Robots vs. Dinosaurs!

## Running Manually (without Docker)

### Initiate Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the backend server

```bash
python manage.py migrate
python manage.py runserver
```

### Initiate Frontend

```bash
cd frontend
npm install
```

Run the frontend server

```bash
npm start
```
