#python3 manage.py flush

# rm -rf __pycache__
# rm -rf hotel_project/__pycache__
# rm -rf hotel/migrations/__pycache__
# rm 0001_initial.py
# #docker exec -it postgres psql "DROP TABLE postgres.hotel_hotel CASCADE;"
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
