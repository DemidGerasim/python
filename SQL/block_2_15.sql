/*
	Выберите одним запросом самый маленький и самый большой по количеству
	товаров заказы.
*/

select * from orders_description 
where count_product = (select min(count_product) from orders_description)
or count_product = (select max(count_product) from orders_description);
