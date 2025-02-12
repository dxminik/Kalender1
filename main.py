#create_user("Aubergine", "Beutel", "Weiblich", "23.01.1999", "Tiere, Musik, Pflanzen")
from backend.database.manage_users import get_user_by_id

print(get_user_by_id(1))
ausgabe = get_user_by_id(2)[5]
print(ausgabe)
