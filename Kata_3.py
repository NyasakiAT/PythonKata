"""
You probably know the "like" system from Facebook and other pages. People can "like" blog
posts, pictures or other items. We want to create the text that should be displayed next
to such an item.

Implement the function which takes an array containing the names of people that
like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.
"""


# My Solution
def likes(names):
    likecount = len(names)
    if likecount == 0:
        return "no one likes this"
    elif likecount < 3:
        return " and ".join(names) + f" {'likes' if likecount == 1 else 'like'} this"
    elif likecount == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return ", ".join(names[:2]) + f" and {likecount-2} others like this"


# Highest rated solution on CodeWars
def likes_sol(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
