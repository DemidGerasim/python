/*
				var 5
Описание элементов интернет магазина. Включает в себя: категории товаров,
товары, клиентов, заказы. Описание категории товаров состоит из: названия и
позиции в дереве категорий. Описание товара состоит из: названия, краткого
описания, полного описания, списка идентификаторов изображении 5 , базовой
цены, текущей цены, количества на складе, артикля, списка цветов, списка
размеров, минимального количества в одном заказе. Описание клиента состоит
из: имени, телефона, адреса, email-а. Описание заказа состоит из: указания
клиента, номера заказа, способа оплаты 6 , способа доставки 7 , списка товаров,
стоимости товаров на момент заказа, общей стоимости заказа с учётом доставки,
даты заказа.

a. Товар может относиться к нескольким категориям. Заказ не содержит
информацию о размере и цвете товара.
*/

create table category_description
(
    id int not null primary key auto_increment
	,name varchar(25)
    ,position numeric(3,2)
);

create table products_description
(
    id int not null primary key AUTO_INCREMENT
    ,name varchar(25)
    ,short_descript varchar(200)
    ,full_descript varchar(500)
    ,basic_price numeric(19,2)
    ,current_price numeric(19,2)
    ,count_stock int
    ,article varchar(20)
    ,min_quantity int
);

create table clients_description
(
    id int not null primary key AUTO_INCREMENT
	,name varchar(60)
    ,phone_number varchar(30)
    ,home_address varchar(50)
    ,email varchar(100)
);

create table orders_description
(
    rec_id int not null primary key AUTO_INCREMENT
    ,order_number int not null
    ,id_client int not null
    ,pay_method varchar(60)
    ,delivery_method varchar(60)
    ,id_product int not null
    ,cost_product numeric(19,2)
    ,count_product int
    ,total_cost numeric(19,2)
    ,order_date datetime
    ,FOREIGN KEY (id_client)  REFERENCES clients_description (id)
    ,FOREIGN KEY (id_product)  REFERENCES products_description (id)
);

create table product_category
(
	rec_id int not null primary key auto_increment
    ,id_product int not null
    ,id_category int not null
    ,UNIQUE KEY id (`id_product`,`id_category`)
    ,FOREIGN KEY (id_product)  REFERENCES  products_description (id) ON UPDATE CASCADE
    ,FOREIGN KEY (id_category)  REFERENCES  category_description(id) ON UPDATE CASCADE
);

create table list_image
(
	id int not null primary key AUTO_INCREMENT
    ,id_product int not null
    ,image varchar(60)
    ,FOREIGN KEY (id_product)  REFERENCES  products_description (id) ON UPDATE CASCADE
);

create table list_color
(
	id int not null primary key AUTO_INCREMENT
    ,id_product int not null
    ,color varchar(60)
    ,FOREIGN KEY (id_product)  REFERENCES  products_description (id) ON UPDATE CASCADE
);

create table list_size
(
	id int not null primary key AUTO_INCREMENT
    ,id_product int not null
    ,size varchar(60)
    ,FOREIGN KEY (id_product)  REFERENCES  products_description (id) ON UPDATE CASCADE
);

/*
	Заполнение таблицы клиентов
*/

INSERT INTO clients_description
(
	name
    ,phone_number
    ,home_address
    ,email
)

VALUES
(
	'Ivan Ivanov'
    ,'888888888888'
    ,'Russia,Moscow'
    ,'ivan@gmail.com'
)

,(
	'Sidirov Sidr'
    ,'777777777777'
    ,'Russia,Bryansk'
    ,'sidr@mail.ru'
)

,(
	'Greg Grigory'
    ,'666666666666'
    ,'Russia, Moscow'
    ,'greg@ya.ru'
)

,(
	'Maks Maksimov'
    ,'5555555555555'
    ,'Russia,Belgorod'
    ,'maks@mail.ru'
);

/*
	Заполнение таблицы категорий
*/

INSERT INTO category_description
(
	name
    ,position
)

values
(
	'Food'
    ,1
)

,(
	'textile'
    ,2
)

,(
    'hygiene_products'
    ,3
)

,(
	'Appliances'
    ,4
)

,(
	'medical_preparations'
    ,5
)

,(
	'furniture'
    ,6
)

,(
	'taburet'
    ,6.1
)

,(
	'table'
    ,6.2
);

/*
	Заполнение таблицы описание товаров
*/

INSERT INTO products_description
(
	name
    ,short_descript
    ,full_descript
    ,basic_price
    ,current_price
    ,count_stock
    ,article
    ,min_quantity
)


VALUES

(
	'Snickers'
    ,'snickers'
    ,'ne tormozi snikersni'
    ,55
    ,40
    ,100000
    ,'Snick'
    ,500
)

,(
	'TV samsung 4k'
    ,'SmartTV'
    ,'super good TV 4k'
    ,30000
    ,30000
    ,13
    ,'sm-7214'
    ,1
)

,(
	'LG smart'
    ,'LG'
    ,'super TV'
    ,50000
    ,49999
    ,23
    ,'lg-458'
    ,1
)

,(
	'smart_chair'
    ,'chair'
    ,'nichego ydobnee ne videl'
    ,10000
    ,9999
    ,17
    ,'biggi-2670'
    ,1
);

/*
	Заполнение таблицы категории продуктов
*/

INSERT INTO product_category
(
	id_product
    ,id_category
)

VALUES
(
	1
    ,1
)

,(
	2
    ,4
)

,(
	3
    ,4
)

,(
	4
    ,4
)

,(
	4
    ,6
);

/*
	заполнение таблицы заказов
*/

INSERT INTO orders_description
(
    order_number
	,id_client
    ,pay_method
    ,delivery_method
    ,id_product
    ,cost_product
    ,count_product
    ,total_cost
    ,order_date
)
VALUES
(
    123
	,1
    ,'cashless payments'
    ,'pickup'
    ,1
    ,10000
    ,1
    ,10000
    ,now()
)

,(
    124
	,1
    ,'cashless payments'
    ,'pickup'
    ,2
    ,40
    ,500
    ,25000
    ,now()
)

,(
    125
	,2
    ,'cash'
    ,'pickup'
    ,2
    ,10000
    ,1
    ,10000
    ,now()
)

,(
    126
	,3
    ,'cashless payments'
    ,'home delivery'
    ,2
    ,30000
    ,1
    ,30999
    ,now()
)

,(
    127
	,4
    ,'cashless payments'
    ,'home delivery'
    ,2
    ,50000
    ,1
    ,50500
    ,now()
);

/*
	Заполнение таблицы изображений
*/

insert into list_image
(
	id_product
    ,image
)
VALUES
(
	1
    ,'1.png'
),
(
	1
    ,'2.png'
),
(
	1
    ,'3.png'
),
(
	2
    ,'4.png'
),
(
	2
    ,'5.png'
);

/*
	заполнение таблицы список цветов
*/

insert into list_color
(
	id_product
    ,color
)
VALUES
(
	1
    ,'red'
),
(
	1
    ,'blue'
),
(
	2
    ,'red'
),
(
	2
    ,'blue'
),
(
	3
    ,'red'
);

/*
	Заполнение таблицы список размеров
*/

insert into list_size
(
	id_product
    ,size
)
VALUES
(
	1,
    '100x100'
),
(
	1,
    '200x200'
),
(
	1,
    '300x300'
),
(
	2,
    '100x100'
),
(
	3,
    '150x150'
);