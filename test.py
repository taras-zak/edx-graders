
# coding: utf-8

# # Lists in Python

# A list, sometimes called and array or a vector is an ordered collection of values. The value of a particular element in a list is retrieved by querying for a specific index into an array. Lists allow duplicate values, but but indicies are unique. In python, like most programming languages, list indices start at 0, that is, to get the first element in a list, request the element at index 0. Lists provide very fast access to elements at specific positions, but are inefficient at "membership queries," determining if an element is in the array. 
# 
# In python, lists are specified by square brackets, `[ ]`, containing zero or more values, separated by commas. Lists are the most common data structure, and are often generated as a result of other functions, for instance, `a_string.split(" ")`.
# 
# To query a specific value from a list, pass in the requested index into square brackets following the name of the list. Negative indices can be used to traverse the list from the right.

# In[4]:

a_list = [1, 2, 3, 0, 5, 10, 11]
another_list = ["a", "b", "c"]
empty_list = []
mixed_list = [1, "a"]

print "another_list[1]:"
print another_list[1]
print "a_list[-1]:"
print a_list[-1]      # indexing from the right
print "a_list[2:]:"
print a_list[2:]


# In[7]:

import hashlib

class TestFailure(Exception):
  pass
class PrivateTestFailure(Exception):
  pass

class Test(object):
  passed = 0
  numTests = 0
  failFast = False
  private = False

  @classmethod
  def setFailFast(cls):
    cls.failFast = True

  @classmethod
  def setPrivateMode(cls):
    cls.private = True

  @classmethod
  def assertTrue(cls, result, msg=""):
    cls.numTests += 1
    if result == True:
      cls.passed += 1
      print "1 test passed."
    else:
      print "1 test failed. " + msg
      if cls.failFast:
        if cls.private:
          raise PrivateTestFailure(msg)
        else:
          raise TestFailure(msg)

  @classmethod
  def assertEquals(cls, var, val, msg=""):
    cls.assertTrue(var == val, msg)

  @classmethod
  def assertEqualsHashed(cls, var, hashed_val, msg=""):
    cls.assertEquals(cls._hash(var), hashed_val, msg)

  @classmethod
  def printStats(cls):
    print "{0} / {1} test(s) passed.".format(cls.passed, cls.numTests)

  @classmethod
  def _hash(cls, x):
    return hashlib.sha1(str(x)).hexdigest()


# Some common functionality of lists:
# 
# + `list.append(x)`: adds an element ot the end of a list
# + `list_1.extend(list_2)`: adds all elements in the second list to the end of the first list
# + `list.insert(index, x)`: inserts element x into the list at the specified index. Elements to the right of this index are shifted over
# + `list.pop(index)`: removes the element at the specified position
# + `list.index(x)`: looks through the list to find the specified element, returning it's position if it's found, else throws an error
# + `list.remove(x)`: removes object `x` from list
# + `list.count(x)`: counts the number of occurrences of the input element
# + `list.sort()`: sorts the list of items
# + `list.reverse()`: reverses the order of the list
# + `len(list)`: returns the number of elements in the list

# In[2]:

a_list = [1, 2, 3, 0, 5, 10, 11]
print "a_list:"
print a_list

a_list.append(7)
print "append(7):"
print a_list, '\n'

a_list.extend([3, 9, 6])
print "extend([3, 9, 6]):"
print a_list, '\n'

a_list.insert(3, -1)
print 'insert(3, -1):'
print a_list, '\n'

a_list.pop()
print "pop():"
print a_list, '\n'

a_list.pop(0)
print "pop(0):"
print a_list, '\n'

a_list.remove(0)
print "remove(0):"
print a_list, '\n'

x = a_list.index(10)
print "index(10):"
print x
print a_list, '\n'   # a_list was not changed

y = a_list.count(3)
print "count(3):"
print y
print a_list, '\n'   # a_list was not changed

a_list.sort()
print "sort():"
print a_list, '\n'

a_list.reverse()
print "reverse():"
print a_list, '\n'
print "len():"
print len(a_list)


# >### Exercise
# 
# >* Add the letter "d" in `another_list` and print the result (see example above).
# 
# >* Find the index for letter "c" in `another_list`. Assign result to `c_index` variable.

# In[5]:

another_list.append('d')
print another_list

c_index = another_list.index('c')
print c_index


# In[10]:



Test.assertEqualsHashed(another_list, '2d20205b636068b94c6253d2c0a324067e02eacf', 'Incorrect content of list "another_list"')
Test.assertEqualsHashed(c_index, 'da4b9237bacccdf19c0760cab7aec4a8359010b0', 'Incorrect value of "c_index"')


# >### Exercise
# 
# >* Sort `another_list` in descending order and print the result.
# 
# >* In the sentence "Python is the word and only one word. And on and on and on and on..." count the amount of all words. Write results to the `amount` variable. Count also how many times the word "and" occurs in this sentence (ignore capitalization). Write result to the `and_amount` variable. 

# In[ ]:

another_list.sort(reverse=True)
print another_list

s = "Python is the word and only one word. And on and on and on and on..."
arr = s.lower().split()
amount = len(arr)
print amount

and_amount = arr.count('and')
print and_amount


# In[ ]:

Test.assertEquals(another_list, ['d', 'c', 'b', 'a'], 'Incorrect content of list "another_list"')
Test.assertEquals(amount, 16, 'Incorrect value of "amount"')
Test.assertEquals(and_amount, 5, 'Incorrect value of "and_amount"')


# In[ ]:



