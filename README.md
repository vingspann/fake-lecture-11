# lecture11-thuhe

Unit testing review

## Run the tests

Unlike last lecture, the tests are in a different directory this time. In
order to run them, you'll need to tell Python to execute the `unit_tests`
module inside `tests/`:

```
talah:~/workspace $ cd lecture11-thuhe/
talah:~/workspace/lecture11-thuhe (master) $ python -m tests/unit_tests
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
talah:~/workspace/lecture11-thuhe (master) $
```

## Write more tests and fix the buggy code!

Look at function `get_chatbot_response` inside `functions.py`.

It's a buggy function that I slapped together real quick. Given a particular
user input, it's intended to return what a chatbot would say.

There are four commands -- `hello`, `add`, `divide`, and `say`, and they should
all be usable like your chatbot would be!

(As an example, `get_chatbot_response('Hello')` should return `'Hey there!'`.)

Create a test file called `tests.py`, and write and run some unit tests that
codify expected input/output combinations for this function.

As you write and run the tests, you'll find bugs in the code. Fix them and
write tests for your fixes :)

## Finished?

Read over the following articles, if you haven't done so already:
* https://www.martinfowler.com/articles/continuousIntegration.html