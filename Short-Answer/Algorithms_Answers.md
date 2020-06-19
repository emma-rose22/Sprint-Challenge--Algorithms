#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
This code has a runtime of O(n), because the amount of operations being done
is dependent on the input n. As n gets larger, the loop runs more times. It seems
to actually have to loop an amount of time exactly equal to n.

b)
The runtime for this code is O(n^2). This is because there is a nested loop situation,
and in each loop action is taken with n, neither loop is doing a constant operation.

c)
The runtime for this question is O(1). That is because no matter the input, there
is always just one operation done.

## Exercise II

My solution has a complexity of O(log(n)) because the search for the perfect floor
is not a linear search, but halves the search area with every iteration.

ground_floor = 0
middle_floor = len(n) // 2
top_floor = len(n) -1

perfect_egg_floor = not found

while the_ground floor is less than the top_floor and perfect_egg_floor not found:

    middle_floor = ground floor + top_floor divided by two

    if the middle_floor doesn't break the egg and the middle_floor + 1 does break the egg:
        perfect_egg_floor = found
        return middle_floor

    if that doesnt work:
        if the middle_floor broke the egg:
            top_floor = middle_floor - 1
        if the middle_floor didn't break the egg:
            ground_floor = middle_floor + 1
