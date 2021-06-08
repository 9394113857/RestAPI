-- Adding Auto-Increment to the Primary Column:-
ALTER TABLE `clinicalfirst`.`user_signup`
CHANGE COLUMN `ID` `ID` INT(20) NOT NULL AUTO_INCREMENT ,
DROP PRIMARY KEY,
ADD PRIMARY KEY (`ID`);
;


