--Select all: # starting line at beginning
-- WHERE City='Berlin'; # ending line last
/* SELECT * FROM Customers;
SELECT * FROM Products;
SELECT * FROM Orders;
SELECT * FROM Categories; */
# The following example uses a comment to ignore part of a line:
SELECT CustomerName, /*City,*/ Country FROM Customers;

--The following example uses a comment to ignore part of a statement:
SELECT * FROM Customers WHERE (CustomerName LIKE 'L%'
OR CustomerName LIKE 'R%' /*OR CustomerName LIKE 'S%'
OR CustomerName LIKE 'T%'*/ OR CustomerName LIKE 'W%')
AND Country='USA'
ORDER BY CustomerName;

--Deleting multiple records:-
DELETE FROM `clinicalfirst`.`user_signup` WHERE (`user_signup_id` = 'US0003');
DELETE FROM `clinicalfirst`.`user_signup` WHERE (`user_signup_id` = 'US0004');
DELETE FROM `clinicalfirst`.`user_signup` WHERE (`user_signup_id` = 'US0005');
DELETE FROM `clinicalfirst`.`user_signup` WHERE (`user_signup_id` = 'US0006');

-- CHanging User phone number to INT(20):-
ALTER TABLE `clinicalfirst`.`user_signup`
CHANGE COLUMN `USER_PHONE_NUMBER` `USER_PHONE_NUMBER` INT(20) NULL DEFAULT NULL ;


--Dropping UN keys:-
ALTER TABLE `clinicalfirst`.`user_signup`
DROP INDEX `USER_PHONE_NUMBER_UNIQUE` ,
DROP INDEX `USER_MAIL_ID_UNIQUE` ;
;

--Adding UN keys:-
ALTER TABLE `clinicalfirst`.`user_signup`
ADD UNIQUE INDEX `USER_MAIL_ID_UNIQUE` (`USER_MAIL_ID` ASC) VISIBLE,
ADD UNIQUE INDEX `USER_PHONE_NUMBER_UNIQUE` (`USER_PHONE_NUMBER` ASC) VISIBLE;
;

-- Set Null values for the single row:-
UPDATE `clinicalfirst`.`user_signup` SET `USER_MAIL_ID` = NULL, `USER_PASSWORD` = NULL WHERE (`user_signup_id` = 'US0003');

-- Set Null values for different columns in selected multiple rows:-
UPDATE `clinicalfirst`.`user_signup` SET `USER_NAME` = NULL, `USER_PHONE_NUMBER` = NULL WHERE (`user_signup_id` = 'US0003');
UPDATE `clinicalfirst`.`user_signup` SET `USER_MAIL_ID` = NULL WHERE (`user_signup_id` = 'US0004');
UPDATE `clinicalfirst`.`user_signup` SET `USER_PASSWORD` = NULL, `USER_DATE_CREATED` = NULL WHERE (`user_signup_id` = 'US0005');
UPDATE `clinicalfirst`.`user_signup` SET `USER_NAME` = NULL, `USER_PASSWORD` = NULL, `USER_DATE_CREATED` = NULL WHERE (`user_signup_id` = 'US0006');

-- Setting Selected rows with null values of selected columns and updated values with selected columns:-
UPDATE `clinicalfirst`.`user_signup` SET `USER_PASSWORD` = NULL WHERE (`user_signup_id` = 'US0001');
UPDATE `clinicalfirst`.`user_signup` SET `USER_NAME` = NULL, `USER_PASSWORD` = NULL, `USER_IP` = NULL WHERE (`user_signup_id` = 'US0003');
UPDATE `clinicalfirst`.`user_signup` SET `USER_IP` = NULL WHERE (`user_signup_id` = 'US0002');

-- Assigning Default Value for Primary Column of user_signup Table:-
ALTER TABLE `clinicalfirst`.`user_signup`
CHANGE COLUMN `user_signup_id` `user_signup_id` VARCHAR(20) NOT NULL DEFAULT '000' ;

-- Removing Default Value for Primary Column of user_signup Table:-
ALTER TABLE `clinicalfirst`.`user_signup`
CHANGE COLUMN `user_signup_id` `user_signup_id` VARCHAR(20) NOT NULL ;





