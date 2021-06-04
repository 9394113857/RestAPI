-- Assigning Default Value to the Primary Column:-
ALTER TABLE `clinicalfirst`.`user_registration`
CHANGE COLUMN `USER_REG_ID` `USER_REG_ID` INT(10) NOT NULL DEFAULT 0 ;

-- Removing Default Value to the Primary Column:-
ALTER TABLE `clinicalfirst`.`user_registration`
CHANGE COLUMN `USER_REG_ID` `USER_REG_ID` INT(10) NOT NULL ;

-- Changing varchar to int first column and changing int to varchar second column:-
ALTER TABLE `clinicalfirst`.`user_registration`
CHANGE COLUMN `USER_REG_ID` `USER_REG_ID` INT(20) NOT NULL ,
CHANGE COLUMN `USER_ID` `USER_ID` VARCHAR(20) NULL DEFAULT NULL ;

