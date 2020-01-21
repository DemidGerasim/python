/*
	Выберите среднее число заказов для всех клиентов (отношение общего числа
	заказов к общему числу клиентов).
*/

select (select count(*) from orders_description)/ (select count(*) from clients_description) as average
