CASE STUDY 2 - Employee Management System

#create database
create database EmployeeManagement;
use EmployeeManagement;

#departmenttable
create table departmentable(
department_id int primary key auto_increment,
name varchar(30)
);
#insert sample data
insert into departmenttable values(202,"IT"),
(110,"web developer"),(120,"android developer"),(200,"IT"),(240,"animation"),(125,"HR");



#employeetable
CREATE TABLE emptttable (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    salary INT NOT NULL CHECK (salary > 30000),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departmenttable(id)
);
desc emptttable;
SHOW CREATE TABLE emptttable;
#insert sample data
insert into emptttable (name, age, gender, salary, department_id)
values
('vinny', 22, 'female', 50000, 202),  -- IT
('sam', 22, 'female', 59000, 110),    -- web developer
('dimple', 22, 'female', 50000, 120), -- android developer
('rishi',25,'male',60000,240),#animation
('anmol',24,'male',65000,125); #hr
select * from emptttable;


#projects table
create table project(
project_id int primary key auto_increment,
name varchar(30),
budget int not null check (budget > 10000)
);
#insertion
insert into project values(11,"chatbot",30000),
(90,"web application",25000),(45,"game-pikaboo",11000);
select * from project;


#employee projects table
create table emp_pprojects(
emp_id int, foreign key (emp_id) references emptttable(id),
project_id int, foreign key (project_id) references project(project_id) 
);
#insertion
insert into emp_pprojects values(1,11),(2,90),(3,45);
select * from emp_pprojects;


#attendance table
create table attendancee(
id int primary key auto_increment,
foreign key(id) references emptttable(id),
date_at date not null,
status enum('present','absent','on leave')
);
#insertion 
INSERT INTO attendancee (date_at, status)
VALUES
('2025-01-10', 'present'),  -- Employee with emp_id 1 is present on 2025-01-21
('2025-01-10', 'absent'),   -- Employee with emp_id 2 is absent on 2025-01-21
('2025-01-10', 'on leave'); -- Employee with emp_id 3 is on leave on 2025-01-21
select * from attendance;

select * from emptttable where department_id=102;
select * from project where budget>50000;

SELECT e.name AS employee_name, p.name AS project_name
FROM emptttable e
JOIN emp_pprojects ep ON e.id = ep.emp_id
JOIN project p ON ep.project_id = p.project_id;

select * from emptttable where salary>50000;

#update records
update emptttable set salary=salary*1.10 where department_id=125;
select * from emptttable;
update emptttable set department_id=202 where name="dimple";
SET SQL_SAFE_UPDATES = 0;
select * from emptttable;

#delete records
alter table emptttable add job varchar(20);
insert into emptttable (name, age, gender, salary, department_id, job)
values
('vinny', 22, 'female', 50000, 202, "resigned"),  -- IT
('sam', 22, 'female', 59000, 110, "continuing"),    -- web developer
('dimple', 22, 'female', 50000, 120,"resigned"), -- android developer
('rishi',25,'male',60000,240,"continuing"),#animation
('anmol',24,'male',65000,125,"continuing"); #hr
 delete from emptttable where job="resigned" ;
 select * from emptttable;
