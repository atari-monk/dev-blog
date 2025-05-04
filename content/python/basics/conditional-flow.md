# Conditional Flow

## Basic If Statement

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

## If-Elif-Else

```python
age = 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

## Logical Operators

```python
temperature = 25
is_summer = True

if temperature > 30 or (is_summer and temperature > 25):
    print("It's hot!")
elif not is_summer and temperature < 10:
    print("It's cold!")
else:
    print("The temperature is pleasant")
```