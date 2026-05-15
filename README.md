# Cyberpunk Learning Arc


## Week 1

### Day 1

#### **Zen of Python** by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
#### Analysis of **Zen of Python** 
    When it comes to coding, intentionality is very important. Code should be beautiful, simple, and readable, not slop that is illegible and difficult to retrace when you read it. However, if your problem requires a solution that is not simple, its important that your code consists of simpler parts that coalesce into something complex rather than connecting more difficult/ambigious subparts into something that is even more complicated, rendering the developer confused and unable to retrace their steps. It's also important that your code has an ubiqitous effect, or rather there should be no special/edge case that slips outside the scope of your solution. When coding, make sure that you understand that what you are doing and not just guessing, that will take forever to debug and you inevitably aren't solving the problem and possibly even creating more. And make sure that your solution is simple rather than difficult. Python has one obvious solution, if you come up with more than one solution you are probably overcomplicating it.
#### Dissassembly
    Before python runs a line of code it generates integer objects for the integers -5 through 256.

#### interned Strings
    Strings are immutable objects in python. If changes to a string a made, a copy with the modified value is created, while the original string remains the same

    Implicit Interning
        All empty strings and strings of length one are interned

        Strings up to 4096 are interned

        Names of functions, class, variables, arguments are interned

        keys to dictionary that hold module, class, or instance attributes are interned

        Stringd are interned only at compile-time, this means they will not be interned it their value cant be computed at compile time

        Strings with characters apart from ASCII will not be interned

    Explicit Interning
        sys.intern(<immutable object>)
    
    ADvantages of String Interning
        Saving memory
        Fast Comparisons
            interned strings are faster to compare
        Fast dictionary lookups
    Disadvantages of String Interning
        Memory Cost
        Time Cost
            intern() is expensive
        Multi-threaded Environments
Reassignment vs Mutation
    Reassignment is when you change the memory address a variable is pointing to. Mutation is when you change the data at that memory address. 
        Examples of mutations:
            object attributes
            function calls that modify the object in place
            array mutation
        Examples of reassignment:
            variable declaration
        

        Ex. 
           a = [100,200,300]
           self.variable = a
           b = a
           self.variable = [100, 250]
           print(b) // [100,200,300]

           # Regardless of which variable you use to perform the mutation,
        # all variables pointing to the same memory address will reflect
        # the change — because the object itself changed, not the variables.

        a = [100, 200, 300]
        self.variable = a
        b = a
        self.variable[0] = 25
        print(b)  # [25, 200, 300]


**Variables don't have values. Variables point to objects. Objects have values**