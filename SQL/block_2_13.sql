/*
	Выберите суммарную стоимость всех товаров интернет магазина с учётом их
	количества.
*/

SELECT sum(current_price*count_stock) as summary from products_description;