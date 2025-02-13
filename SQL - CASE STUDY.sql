SQL - CASE STUDY

Created database called series 

Created table with the name of netflix which has the fields like series_id, series_name, director, release date, duration and ratings along with the data types such as int, varchar, date, time and double.

Created table netflix_fans with the fields - id, reviews, would they like to watch again along with the datatype like boolean.

Used insert command to insert the values.

Created table netflix_accounts to calculate the aggregate functions.



create database series;
use series;

#table 1
create table netflixx(
series_id int,
series_name varchar(50),
director varchar(30),
released_date date,
duration time,
ratings double
);

insert into netflixx values(134,'mismatched','akarsh','2021-05-22','05:25:45',8.5);
insert into netflixx values(112,'vampire diaries','Chris Grismer','2011-04-02','04:25:45',8.990);	
insert into netflixx values(156,'lock & key','Mark Romanek','2020-09-12','03:34:34',7.89);
desc netflixx;
select * from netflixx;


#table 2
CREATE table netflixx_fans(
fans_id int,
reviews varchar(50),
would_they_like_to_watch_again boolean
);
alter table netflixx_fans add no_of_seasons int;



insert into netflixx_fans values(101,'I like to watch again',true),(111,'better',false),(123,'I loved that series',true);
alter table netflixx add no_of_seasons int;
select*from netflixx;
insert into netflixx values(134,'mismatched','akarsh','2021-05-22','05:25:45',8.5,3),
(112,'vampire diaries','Chris Grismer','2011-04-02','04:25:45',8.990,8),
(156,'lock & key','Mark Romanek','2020-09-12','03:34:34',7.89,3);
select*from netflixx;

UPDATE netflixx SET no_of_seasons=7 WHERE series_name='lock and key';
SET SQL_SAFE_UPDATES = 0;
select*from netflixx;

create table netflix_accounts(
acc_id int,
no_of_accounts int,
no_of_paidacc int,
no_of_nonpaidacc int,
money_for_single_acc float check (money_for_single_acc > 179),
money_for_groupof_acc float
);
insert into netflix_accounts values(12,10,5,5,199,399);
insert into netflix_accounts values(23,12,5,7,99,299);
insert into netflix_accounts values(45,10,6,4,199,399);
insert into netflix_accounts values(76,5,3,2,299,599);
insert into netflix_accounts values(123,8,5,3,259,459);

select * from netflix_accounts;
#sum
select sum(no_of_accounts) as totalaccounts from netflix_accounts;
select sum(money_for_single_acc * no_of_paidacc) as paidsingleacc from netflix_accounts;

#avg
select avg(money_for_single_acc) as singleaccounts from netflix_accounts;

#count
select count(no_of_paidacc) as paidaccounts from netflix_accounts;

#min
select min(money_for_groupof_acc) as mingroupmoney from netflix_accounts;

#max
select max(money_for_single_acc) as maxsinglemoney from netflix_accounts;
select max(would_they_like_to_watch_again) as likes from netflixx_fans; 


#greater than or equal to
select * from netflixx where no_of_seasons >=7; 

select min(ratings) as highrate from netflixx;

#groupby
select no_of_accounts, sum(money_for_single_acc) as totsinacc from netflix_accounts 
group by no_of_accounts 
having sum(money_for_single_acc) > 250
order by totsinacc desc
limit 2;
