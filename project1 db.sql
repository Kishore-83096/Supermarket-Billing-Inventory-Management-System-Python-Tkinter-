use project1;

select * from inventory;
drop table inventory;
describe inventory;
DELETE FROM INVENTORY WHERE ITEM_CODE =00015 ;
select * from Stock_input;
describe stock_input;
drop table stock_input;
delete  from stock_input where ITEM_CODE = 00010;

select* from  sales;
select * from Salessub;

select * from inventory;


SELECT t2.item_name,t1.*
FROM salessub t1
INNER JOIN inventory t2 ON t1.ITEM_CODE = t2.ITEM_CODE;