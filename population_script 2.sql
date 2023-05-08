
-- PizzaType
INSERT INTO pizza_pizzatype (name) VALUES('Normal');

INSERT INTO pizza_pizzatype (name) VALUES('Sterkar');

INSERT INTO pizza_pizzatype (name) VALUES('Vegan');


-- Hawaiian
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('Hawaiian',
'Ananas, skinka, ostur og sósa',
'Hawaiian pizza er ljúffeng pizza. Þessi pizza er toppuð með bragðmikilli samsetningu af skinku sneiðum og sætum, safaríkum ananas. Hawaiian pizza hefur náð vinsæld um allan heim og er þetta fullkomna pizzan fyrir þig.', '1',
'1990',
'2990', '3990',
'glúten, mjólk, soja');

-- Pepperoni and Mushroom
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('Pepp & Svepp',
'Pepperoni, sveppir, ostur og sósa',
'Pepperoni og sveppa pizza er klassísk og ljúffeng pizzasamsetning. Þessi pizza er hlaðin bragðmiklum sneiðum af pepperoni og ljúffengum, jarðbundnum sveppum, sem skapar ríkulegt og seðjandi bragð sem mun láta
 þig langa í meira.', '1',
'1990',
'2990', '3990',
'glúten, mjólk, sellerí, sinnep');


-- El Fuego
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('El Fuego',
'Ferskur chili, jalapeno, pepperoni, piparostur, sterkt pepperoni, svartur pipar, ostur og sósa',
'Við kynnum dýrindis pizzuna okkar El Fuego. Pizzan er hlaðin fersku chili og jalapeno, sem gefur henni hið fullkomna magn af hita til að vekja bragðlaukana þína. Hver sneið er ríkulega toppuð með bragðmiklum pepperoni,
gerð með blöndu af bræddum ostum og með svörtum pipar fyrir auka spark.',
'1',
'2090', '3090',
'4090', 'glúten, mjólk, sellerí, sinnep');


-- Spicy Vegan
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('Spicy Vegan',
'Ananas, BBQ topping, chiliflögur, hvítlaukur, jalapeno, svartur pipar, veganostur og sósa',
'Ef þú ert að leita að ljúffengri vegan pizzu, þá er Vegan pizzan okkar frábær kostur. Þessi pizza er búin til með stökkri, vegan-vænnum botn og toppað með ljúffengri blöndu af sætri og
 sterkri BBQ sósu, safaríkum bitum af ananas og bragðmikilli blöndu af vegan osti, chili flögum, hvítlauk, jalapeno og svörtum pipar.',
'1',
'2090', '3090',
'4090', 'glúten');


-- Margarita
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('Margarita',
'Ostur og sósa',
'Dekraðu þig með þeim klassísku, Margarita pizzunni okkar! Nýgerða deigið okkar er fullkomlega bakað í stökka gullbrúna skorpu og síðan toppað með pizzasósu og rifnum bræddum osti.',
'1',
'1790', '1990',
'2090', 'glúten, mjólk');


-- Yorky
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('Yorky',
'Beikonkurl, cheddaarostur, hakk, ostur og sósa',
'Dekraðu við þig í dýrindis og bragðmiklum rétti með beikonkurli, cheddarosti og hakki! Stökku beikonkurlin okkar eru fullkomnar. Parað með bragðmiklu og safaríku hakki, toppað með rjómalöguðum cheddarosti og bragðmiklli sósu.',
'1', '2090',
'3090', '4090',
'glúten, mjólk, soja, sellerí');


-- Everything Meaty
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('Everything Meaty',
'Pepperoni, skinka, hakk, beikonkurl, ostur og sósa',
'Uppfylltu löngun þína með kjötmiklu og bragðmiklu kjötveislunni okkar. Pizzan er toppuð með pepperoni, beikonkurli, skinku og hakki! Nýbakaða deigið okkar er toppað með safaríku pepperoni, skinku og bragðmiklu hakki. Dreyft með rifinn
ost og sósu.', '1',
'2190',
'3190', '4190',
'glúten, mjólk, soja, sellerí, sinnep');


-- Luxe
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('Luxe',
'Pepperoni, skinka, sveppir, ananas ostur og sósa',
'Uppfylltu lönguninni með ljúffengu Pepperoni og skinku pizzunni okkar, toppað með blöndu af ljúffengu hráefni! Nýbakaða deigið okkar er toppað með krydduðu pepperoni, bragðmikilli skinku, jarðbundnum sveppum,
 safaríkum ananas og blöndu af bræddum osti.',
'1', '2090',
'3090', '4090',
'glúten, mjólk, soja, sellerí, sinnep');

-----------------------------------------------


-- Risaeðlan
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('Risaeðlan',
'Beikonkurl, hakk, pepperoni, pulled pork, skinka, BBQ sósa og ostur',
'Vertu tilbúinn fyrir bragðsprengingu með beikon, kjöthakki og pulled pork pizzunni okkar! Nýgerðu deigið okkar er toppað með stökku beikonkurli, safaríku hakki, krydduðu pepperoni, safaríku svínakjöti,
 bragðmikilli skinku og blöndu af bræddum osti og cheddar osti.',
'1', '2190',
'3190', '4190',
'glúten, mjólk, soja, sellerí, sinnep');


-- Drottningin
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('Drottningin',
'Beiknsneiðar, ferskur chili, pepperoni, piparostur, rauðlaukur, sveppir, ostur og sósa',
'Upplifðu eldheita og bragðmikla sprengingu af bragði með krydduðu beikoni og pepperoni pizzunni okkar! Nýgerðu deigið okkar er toppað með stökkum beikonsneiðum, krydduðum ferskum chili, bragðmiklum pepperoni,
 bragðmiklum rauðlauk, jarðbundnum sveppum og blöndu af bræddum mozzarella og piparosti.',
'1',
'2190', '3190',
'4190', 'glúten, mjólk, soja, sellerí, sinnep');


-- BBQ Queen
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('BBQ Queen',
'Jalapeno, pepperoni, piparostur, pulled pork, rjómaostur, ostur og BBQ sósa',
'Upplifðu djarfa og bragðmikla samsetningu af sætu og krydduðu með Pulled Pork Jalapeno pizzunni okkar! Nýlaga deigið okkar er toppað með safaríku svínakjöti, krydduðum jalapeno, bragðmiklar pepperoni, bragðmikill
 rjómaostur og bræddum piparosti.',
'1', '2190',
'3190', '4190',
'glúten, mjólk, soja, sellerí, sinnep');


-- Hvítlauks
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('Hvítlauks',
'Hvítlaukur, hvítlauksolía og ostur',
'Uppfylltu löngun þína í hvítlauk með ljúffengu hvítlaukspizzunni okkar! Nýgerða deigið okkar er fylltar ómatískum keim af ferskum hvítlauk og penslað með hvítlauksolíu, sem skapar ríkulegan og ljúffengan grunn fyrir
 pizzuna. Við toppum það síðan með bræddum osti, og búum til gljáandi áferð sem passar fullkomlega við bragð hvítlauksins.',
'1',
'1790', '1990',
'2090', 'glúten, mjólk');


-- Vegan Vibes
INSERT INTO pizza_pizza (name, toppings, descriptions, type_id, small_price, medium_price, large_price, allergens)
VALUES('Vegan Vibes',
'Vegan kjúkling, ólífur, sólþurrkaður tómatur, rauðlaukur, sveppir, ferskt chilli, veganostur og sósa',
'Dekraðu við þig í dýrindis og bragðmikilli veganpizzu með Vegan kjúklingnum okkar! Nýgerða deigið okkar er toppað með ólífur, sólþurrkuðum tómötum, krydduðum ferskum chili, rauðlaukum, jarðbundnum sveppum og veganosti',
'1',
'2190', '3190',
'4190', 'glúten, soja');





-- PizzaImage
INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/hawaiian.png',
1);

INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/pepperoni_mushroom.png',
2);

INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/el_fuego.png',
3);

INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/spicy_vegan.png',
4);

INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/margarita.png',
5);

INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/yorky.png',
6);

INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/meat.png',
7);

INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/luxe.png',
8);

INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/risaedlan.png',
9);

INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/drottningin.png',
10);

INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/bbq_queen.png',
11);

INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/garlic.png',
12);

INSERT INTO pizza_pizzaimage (image, pizza_id)
VALUES('/static/images/vegan_vibes.png',
13);




-- Drink
INSERT INTO drinks_drink (name, price) VALUES('Coca Cola 2l', '450');
INSERT INTO drinks_drink (name, price) VALUES('Coca Cola Zero 2l', '450');
INSERT INTO drinks_drink (name, price) VALUES('Fanta 2l', '450');
INSERT INTO drinks_drink (name, price) VALUES('Sprite 2l', '450');
INSERT INTO drinks_drink (name, price) VALUES('Monster 330ml', '250');


-- DrinkImage
INSERT INTO drinks_drinkimage (image, drink_id) VALUES('/static/images/coke.png', '1');
INSERT INTO drinks_drinkimage (image, drink_id) VALUES('/static/images/coke_zero', '2');
INSERT INTO drinks_drinkimage (image, drink_id) VALUES('/static/images/fanta.png', '3');
INSERT INTO drinks_drinkimage (image, drink_id) VALUES('/static/images/sprite.png', '4');
INSERT INTO drinks_drinkimage (image, drink_id) VALUES('/static/images/monster.png', '5');



-- Sauce
INSERT INTO sauces_sauce (name, price) VALUES('Brauðstangasósa', '200');
INSERT INTO sauces_sauce (name, price) VALUES('Hvítlaukssósa', '200');
INSERT INTO sauces_sauce (name, price) VALUES('Gráðaostasósa', '200');
INSERT INTO sauces_sauce (name, price) VALUES('BBQ sósa', '200');
INSERT INTO sauces_sauce (name, price) VALUES('Honey Mustard', '200');
INSERT INTO sauces_sauce (name, price) VALUES('Glassúr', '200');

-- SauceImage
INSERT INTO sauces_sauceimage (image, sauce_id) VALUES('/static/images/breadstick_sauce.png', '1');
INSERT INTO sauces_sauceimage (image, sauce_id) VALUES('/static/images/garlic_sauce.png', '2');
INSERT INTO sauces_sauceimage (image, sauce_id) VALUES('/static/images/gradaostasosa.png', '3');
INSERT INTO sauces_sauceimage (image, sauce_id) VALUES('/static/images/bbq_sauce.png', '4');
INSERT INTO sauces_sauceimage (image, sauce_id) VALUES('/static/images/honey_mustard.png', '5');
INSERT INTO sauces_sauceimage (image, sauce_id) VALUES('/static/images/glassur.png', '6');


-- Side
INSERT INTO sides_side (name, description, price, allergens) VALUES('Brauðstangir', 'Nýbakaðar brauðstangir með hvítlauks kantolíu', '990', 'Glúten, Mjólk, Soja');
INSERT INTO sides_side (name, description, price, allergens) VALUES('Spicy Brauðstangir', 'Nýbakaðar brauðstangir með cajun kantolíu', '990', 'Glúten, Mjólk, Soja');
INSERT INTO sides_side (name, description, price, allergens) VALUES('Vegan Brauðstangir', 'Nýbakaðar brauðstangir með hvítlauks kantolíu', '990', 'Glúten');
INSERT INTO sides_side (name, description, price, allergens) VALUES('Súkkulaði smábrauð', 'Nýbakað smábrauð fyllt með súkkulaði', '990', 'Glúten, Mjólk, Soja');
INSERT INTO sides_side (name, description, price, allergens) VALUES('Nutella smábrauð', 'Nýbakað smábrauð fyllt með Nutella', '990', 'Glúten, Mjólk, Soja');
INSERT INTO sides_side (name, description, price, allergens) VALUES('Kanil smábrauð', 'Nýbakað smábrauð með kanil', '990', 'Glúten, Mjólk, Soja');
INSERT INTO sides_side (name, description, price, allergens) VALUES('Osta brauð bitar', 'Nýbakaðir munnstórir brauðbitar með osti', '990', 'Glúten, Mjólk, Soja');
INSERT INTO sides_side (name, description, price, allergens) VALUES('BBQ kjúklingavængir', 'Nýeldaðir kjúklingavængir toppað með BBQ sósu', '990', 'Glúten, Mjólk, Soja');
INSERT INTO sides_side (name, description, price, allergens) VALUES('Sterkir kjúklingavængir', 'Nýeldaðir kjúklingavængir toppað með Hot Sauce', '990', 'Glúten, Mjólk, Soja');


-- SideImage
INSERT INTO sides_sideimage (image, side_id) VALUES('/static/images/breadsticks.png', '1')
INSERT INTO sides_sideimage (image, side_id) VALUES('/static/images/spicy_breadsticks.png', '2')
INSERT INTO sides_sideimage (image, side_id) VALUES('/static/images/vegan_breadsticks.png', '3')
INSERT INTO sides_sideimage (image, side_id) VALUES('/static/images/chocolate.png', '4')
INSERT INTO sides_sideimage (image, side_id) VALUES('/static/images/nutella.png', '5')
INSERT INTO sides_sideimage (image, side_id) VALUES('/static/images/cinnamon.png', '6')
INSERT INTO sides_sideimage (image, side_id) VALUES('/static/images/cheese_bites.png', '7')
INSERT INTO sides_sideimage (image, side_id) VALUES('/static/images/bbq_wings.png', '8')
INSERT INTO sides_sideimage (image, side_id) VALUES('/static/images/hot_wings.png', '9')


-- Offer
INSERT INTO offers_offer (name, description, discount, total) VALUES('50% af', 'Tveir fyrir einn tilboðið okkar' );