<h2 align="center">User management</h2>

<br>

## Required knowledge

- Python OOP principals

## Main targets

- [ ] Create 4 clases `User`, `Administrator` or `Admin`, `Redactor` and `Post`
- [ ] `User` class has to have name, surname, email, date of birth, gender, its has possibility to change own email, create, edit, delete own posts
- [ ] `Redactor` class has all functions that User class has and has possibility to edit all posts 
- [ ] `Admin` class can edit everything, attributes of classes `User` and `Redactor` and can edit all posts
- [ ] `Post` has content, date of creation and modification, Author, can be edited via method, by User with proper permissions, date of modification should be created and updated automatically

## Extended (hard) targets
### Targets to achive after main targets are achieved, more advenced usage of python object oriented programming

- [ ] User classes can be compared with each other with logical operators, `Admin > Redactor > User` 
- [ ] Classes `Admin`, `Redactor`, and `User` should be able to compare with `==` operator, it returns True if object is this same class and `name`+`surname` attrs are this same
- [ ] Classes `Admin`, `Redactor`, and `User` should be able to be used as keys in `dict`
- [ ] It should be possible to determine which `Post` class is bigger (have longer content)

## Optional targets

- [ ] Use Abstract classes to provide solution
- [ ] Symulate this same functionality with one class and permissions system, where `Admin` can elevate permissions of other users
