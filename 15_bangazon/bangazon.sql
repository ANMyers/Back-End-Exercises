
delete from ProductTypes;
delete from Customers;
delete from Computers;
delete from Departments;
delete from TrainingProgram;
delete from Employees;
delete from ProgramEmployee;
delete from ProductOrder;
delete from Products;
delete from PaymentTypes;
delete from Orders;

drop table if Products;
drop table if ProductTypes;
drop table if PaymentTypes;
drop table if ProductOrder;
drop table if Customers;
drop table if Orders;
drop table if Computers;
drop table if Departments;
drop table if Employees;
drop table if ProgramEmployee;
drop table if TrainingProgram;

create table Products (
ProductId integer not null primary key autoincrement,
Price integer not null,
Title text not null,
Description text not null,
ProductTypeId integer not null,
CustomerId integer not null,
foreign key (ProductTypeId) references ProductTypes(ProductTypeId)
foreign key (CustomerId) references Customers(CustomerId)
);

insert into Products 
select null, 10.99, "Power Cord", "Cord for powering.", tp.ProductTypeId, c.CustomerId
from ProductTypes tp, Customers c 
where tp.Category = "Art" 
and c.FirstName = 'Adam';

insert into Products 
select null, 10.99, "T-Shirt", "Wear on torso.", tp.ProductTypeId, c.CustomerId
from ProductTypes tp, Customers c 
where tp.Category = "Clothes" 
and c.FirstName = 'Harper';

insert into Products 
select null, 10.99, "Apple", "Makes you look rude.", tp.ProductTypeId, c.CustomerId
from ProductTypes tp, Customers c 
where tp.Category = "Food" 
and c.FirstName = 'Blaise';

create table ProductTypes (
ProductTypeId integer not null primary key autoincrement,
Category text not null
);

insert into ProductTypes values (null, "Art");
insert into ProductTypes values (null, "Food");
insert into ProductTypes values (null, "Clothes");


create table PaymentTypes (
PaymentTypesId integer not null primary key autoincrement,
PaymentType text not null,
AccountNumber integer not null,
Active boolean not null,
CustomerId integer not null,
foreign key (CustomerId) references Customers(CustomerId)
);

create table ProductOrder (
ProductOrderId integer not null primary key autoincrement,
ProductId integer not null,
OrderId integer not null,
foreign key (ProductId) references Products(ProductId),
foreign key (OrderId) references Orders(OrderId)
);

create table Customers (
CustomerId integer not null primary key autoincrement,
FirstName text not null,
LastName text not null,
DateCreated integer not null
);

insert into Customers values (null, "Adam", "Myers", 040417);
insert into Customers values (null, "Harper", "Python", 040417);
insert into Customers values (null, "Bob", "Veela", 040417);

create table Orders (
OrderId integer not null primary key autoincrement,
ProductOrderId integer not null,
CompletedIndicator boolean not null,
CustomerId not null,
foreign key (CustomerId) references Customers(CustomerId)
);

create table Computers (
ComputerId integer not null primary key autoincrement,
Model text not null,
Make text not null,
Purchased integer not null,
Decommissioned integer not null
);

insert into Computers values (null, "Mac", "Macbook Pro", 040417, 0);
insert into Computers values (null, "Mac", "Macbook Pro", 040312, 0);
insert into Computers values (null, "Mac", "Macbook Pro", 012009, 1);

create table Departments (
DepartmentId integer not null primary key autoincrement,
Name text not null,
Budget integer not null
);

insert into Departments values (null, "Sales", 900000);
insert into Departments values (null, "Administration", 12000000);
insert into Departments values (null, "Human Resources", 8349000);

create table Employees (
EmployeeId integer not null primary key autoincrement,
Name text not null,
SupervisorIndicator boolean not null,
ComputerId integer not null,
DepartmentId integer not null,
foreign key (ComputerId) references Computers(ComputerId),
foreign key (DepartmentId) references Departments(DepartmentId)
);

create table ProgramEmployee (
ProgramEmployeeId integer not null primary key,
EmployeeId integer not null,
TrainingProgramId integer not null,
foreign key (EmployeeId) references Employees(EmployeeId),
foreign key (TrainingProgramId) references TrainingProgram(TrainingProgramId)
);

create table TrainingProgram (
TrainingProgramId integer not null primary key autoincrement,
Name text not null,
StartDate integer not null,
EndDate integer not null,
MaxAttendees integer not null
);

insert into TrainingProgram values (null, "Django101", 08212017, 12042017, 25);
insert into TrainingProgram values (null, "Python101", 08212017, 12042017, 25);
insert into TrainingProgram values (null, "SQL101", 08212017, 12042017, 25);




