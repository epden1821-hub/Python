from address import Address
from mailing import Mailing

from_address = Address(
    index="101000",
    city="Москва",
    street="Тверская",
    house="5",
    flat="1"
)

to_address = Address(
    index="350047",
    city="Краснодар",
    street="Красная",
    house="56",
    flat="12"
)

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=12812.23,
    track="NM234879828937"
)

# Вывод данных был не красивый, поэтому я отформатировал.
# Надеюсь правильно =)

print(f"Отправление № {mailing.track}")
print("=" * 30)
print(f"Отправитель:\n" 
      f" Индекс: {mailing.from_address.index}\n"
      f" Город: {mailing.from_address.city}\n"
      f" Улица: {mailing.from_address.street}\n" 
      f" Дом: {mailing.from_address.house}\n"
      f" Квартира: {mailing.from_address.flat}")
print("=" * 30)
print(f" Получатель:\n"
      f" Индекс: {mailing.to_address.index}\n"
      f" Город: {mailing.to_address.city}\n"
      f" Улица: {mailing.to_address.street}\n"
      f" Дом: {mailing.to_address.house}, - {mailing.to_address.flat}")
print("=" * 30)
print(f"Стоимость {mailing.cost:.2f} рублей")
