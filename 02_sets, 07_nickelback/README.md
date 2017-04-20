# Python Car Sets

## References

* [Python sets](https://docs.python.org/3.6/tutorial/datastructures.html#sets)
* [Set intersection](https://docs.python.org/3.6/library/stdtypes.html?highlight=intersection#set.intersection)
* [Learn Python - Sets](http://www.learnpython.org/en/Sets)

## Instructions

1. Create an empty set named `showroom`.
1. Add four of your favorite car model names to the set.
1. Print the length of your set.
1. Pick one of the items in your show room and add it to the set again.
1. Print your showroom. Notice how there's still only one instance of that model in there.
1. Using `update()`, add two more car models to your showroom with another set.
1. You've sold one of your cars. Remove it from the set with the `discard()` method.

### Acquiring more cars

1. Now create another set of cars in a variable `junkyard`. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the `showroom` set.
1. Use the `intersection` method to see which cars exist in both the showroom and that junkyard.
1. Now you're ready to buy the cars in the junkyard. Use the `union` method to combine the junkyard into your showroom.
1. Use the `discard()` method to remove any cars that you acquired from the junkyard that you want in your showroom.


# Kill Nickelback

In this exercises, you're going to use a conditional statement inside a comprehension. Let's look at a basic example.

```python
nums = range(10)
small_numbers = [num for num in nums if num < 6]
# Only add numbers to the new list if the value is less than 6

words = ['big', 'red', 'dog', 'ate', 'his', 'food']
three_letters_words = [ word.title() for word in words if len(word) == 3 ]
# len(stringVariable) is equivalent to stringVariable.length in JavaScript
```

## Setup

```
mkdir -p ~/workspace/python/exercises/sets && cd $_
touch nickelback.py
```

## Instructions

1. Define a set that contains tuples. Each tuple should contain two strings:
    1. The name of an artist
    1. A song by that artist

    Make sure that some of the songs are from the band Nickelback. You can see a [list of their greatest hits](https://www.amazon.com/Best-Nickelback-1/dp/B00FFERTUK/) on Amazon.
    ```
    # Example set
    songs = {
        ('Nickelback', 'How You Remind Me'), 
        ('Will.i.am', 'That Power'),
        ('Miles Davis', 'Stella by Starlight'),
        ('Nickelback', 'Animals')
    }
    ```
2. Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

