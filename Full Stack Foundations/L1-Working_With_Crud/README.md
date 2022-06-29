# Working With Crud

## ORM Database

Object-relation mapping where object are used to connect the programming language on to the database systems

### Using Library [Sqlalchemy]('https://www.sqlalchemy.org/')

```
pip install sqlalchemy
```

## Cheatsheet

Note:

- Employee as Table

  - name (string)
  - id (integer, Primary Key)

- Address as Table
  - street (string)
  - zip (string)
  - employee_id (integer, foreign key = Employee.id)

> Instance Database to stagging

```
DBSession = sessionmaker(bind=engine)

session = DBSession()
```

> Create Database

```
# Add Data into Employee table
employee1 = Employee(name='User', id=231)
session.add(employee)
session.commit()

# Add Data into Address table
address1 = Address(street='Bikin bottom', zip='999', employee_id=employee1)
session.add(employee)
session.commit()
```

> Read Database

```
employe = session.query(Employee).all()
```

> Update Database

In order to update and existing entry in our database, we must execute the following commands:

- Find Entry
- Reset value(s)
- Add to session
- Execute session.commit()

```
user = session.query(Employee).filter_by(name = 'User').one()
user.street = 'Kampung runtuh'
session.add(user)
session.commit()
```

> Delete Database

To delete an item from our database we must follow the following steps:

- Find the entry
- Session.delete(Entry)
- Session.commit()

```
user = session.query(Employee).filter_by(name = 'User').one()
session.delete(spinach)
session.commit()
```
