create database eVoting

use evoting

create table useri(
	id int primary key identity(1,1),
	emri varchar(255),
	roli varchar(255)
)

select*from useri
select roli from useri where id=1
DBCC CHECKIDENT ('useri', RESEED, 1)

create table candidate(
	id int identity(1,1) primary key,
	emri varchar(255),
	mbiemri varchar(255),
	partiaPolitike varchar(255),
	votat int default 0)


