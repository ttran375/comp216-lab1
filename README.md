# Lecture 1

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ttran375/comp216-lab1/blob/main/src/main.ipynb)

## Question 1

Create a one-line expression that achieve the same output as
the below with the square bracket notation.

```python
NBA = dict(
    OklahomaCity="Thunder",
    Dallas="Mavericks",
    Boston="Celtics",
    NewYork="Knicks",
    Denver="Nuggets",
)

retrieve = NBA.get("Toronto", False)
print(retrieve)
```

## Question 2

Given two numbers, a and b, write a function called
compare_numbers that returns a string indicating the following:

- If a is greater than b, return "a is greater"

- If b is greater than a, return "b is greater"

- If both numbers are equal, return "a and b are equal"

Use the ternary operator to implement the function.

```python
def compare_numbers(a, b):
    pass
```

## Question 3: Examine following JS code snippet and re-create the logic

using Python. Implement the logic as a function that accepts secret_word
as a positional parameter and max_attempt as keyword parameter.

```js
let secret_word = "javascript";
let max_attempt = 5;
do {
    userInput = prompt("Enter the secret word: ");
    max_attempt -= 1;
    console.log(max_attempt)
} while (secret_word != userInput && max_attempt > 0);
```

## Question 4

Based on the following function definition, identify which
of the following parameters are positional-only, keyword-only and/or may
be positionally or by keyword.

```python
def processor(value_1, value_2, /, value_3, value_4=False, *, value_5, value_6):
    text = (value_1 + value_2).upper()
    if value_3:
        text += "!"
    if value_4:
        text = list(text)
        text.extend((value_5, value_6))
    return text
```

