-- PizzaType
INSERT INTO pizza_pizztype (name) VALUES('Spicy')
INSERT INTO pizza_pizztype (name) VALUES('Vegan')
-- Pizza
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens) VALUES('Hawaiian', 'skinka, ananas, ostur og sósa', 'Hawaiian pizzan okkar er ljúffeng og einstök. Þessi pizza er toppuð með ljúffengri blöndu af bragðmikilli skinku, safaríkum ananasbitum og bræddum osti, sem gerir hana að fullkominni blöndu af sætu og saltu bragði.', '', '1990', '2990', '3990', 'Glúten, Soja, Mjólk')
-- PizzaImage
INSERT INTO pizza_pizzaimage (image, pizza_id) VALUES('image', '1')



-- Drink
INSERT INTO drinks_drink (name, price) VALUES('Coca Cola 2l', '200')
-- DrinkImage
INSERT INTO drink_drinkimage (image, drink_id) VALUES('image' '1')



-- Sauce
INSERT INTO sauces_sauce (name, price) VALUES('Brauðstangasósa', '150')
-- SauceImage
INSERT INTO sauces_sauceimage (image, sauce_id) VALUES('image', '1')



-- Side
INSERT INTO saides_side (name, description, price, allergens) VALUES('Brauðstangir', 'Brauðstangirnar okkar eru gerðar úr hágæða hráefni og bakaðar til fullkomnunar, sem skilar sér í stökku ytra útliti og mjúku, dúnkenndu innanverðu sem gerir bragðlaukana þína löngun í meira. Þau eru fullkomin meðlæti með pizzunni þinni.', '990', 'Glúten, Mjólk, Soja')
-- SideImage
INSERT INTO drink_drink (image, side_id) VALUES('image', '1')



