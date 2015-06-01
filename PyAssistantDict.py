preDict={
	'sqlite3':'',
	'sqlite3':'''''',
	'sqlite3.Cache':'''''',
	'sqlite3.Cache.display':'''For debugging only.''',
	'sqlite3.Cache.get':'''Gets an entry from the cache or calls the factory function to produce one.''',
	'sqlite3.Connection':'''SQLite database connection object.''',
	'sqlite3.Connection.DataError':'''''',
	'sqlite3.Connection.DatabaseError':'''''',
	'sqlite3.Connection.Error':'''''',
	'sqlite3.Connection.IntegrityError':'''''',
	'sqlite3.Connection.InterfaceError':'''''',
	'sqlite3.Connection.InternalError':'''''',
	'sqlite3.Connection.NotSupportedError':'''''',
	'sqlite3.Connection.OperationalError':'''''',
	'sqlite3.Connection.ProgrammingError':'''''',
	'sqlite3.Connection.Warning':'''''',
	'sqlite3.Connection.close':'''Closes the connection.''',
	'sqlite3.Connection.commit':'''Commit the current transaction.''',
	'sqlite3.Connection.create_aggregate':'''Creates a new aggregate. Non-standard.''',
	'sqlite3.Connection.create_collation':'''Creates a collation function. Non-standard.''',
	'sqlite3.Connection.create_function':'''Creates a new function. Non-standard.''',
	'sqlite3.Connection.cursor':'''Return a cursor for the connection.''',
	'sqlite3.Connection.enable_load_extension':'''Enable dynamic loading of SQLite extension modules. Non-standard.''',
	'sqlite3.Connection.execute':'''Executes a SQL statement. Non-standard.''',
	'sqlite3.Connection.executemany':'''Repeatedly executes a SQL statement. Non-standard.''',
	'sqlite3.Connection.executescript':'''Executes a multiple SQL statements at once. Non-standard.''',
	'sqlite3.Connection.interrupt':'''Abort any pending database operation. Non-standard.''',
	'sqlite3.Connection.isolation_level':'''''',
	'sqlite3.Connection.iterdump':'''Returns iterator to the dump of the database in an SQL text format. Non-standard.''',
	'sqlite3.Connection.load_extension':'''Load SQLite extension module. Non-standard.''',
	'sqlite3.Connection.rollback':'''Roll back the current transaction.''',
	'sqlite3.Connection.row_factory':'''''',
	'sqlite3.Connection.set_authorizer':'''Sets authorizer callback. Non-standard.''',
	'sqlite3.Connection.set_progress_handler':'''Sets progress handler callback. Non-standard.''',
	'sqlite3.Connection.text_factory':'''''',
	'sqlite3.Connection.total_changes':'''''',
	'sqlite3.Cursor':'''SQLite database cursor class.''',
	'sqlite3.Cursor.arraysize':'''''',
	'sqlite3.Cursor.close':'''Closes the cursor.''',
	'sqlite3.Cursor.connection':'''''',
	'sqlite3.Cursor.description':'''''',
	'sqlite3.Cursor.execute':'''Executes a SQL statement.''',
	'sqlite3.Cursor.executemany':'''Repeatedly executes a SQL statement.''',
	'sqlite3.Cursor.executescript':'''Executes a multiple SQL statements at once. Non-standard.''',
	'sqlite3.Cursor.fetchall':'''Fetches all rows from the resultset.''',
	'sqlite3.Cursor.fetchmany':'''Fetches several rows from the resultset.''',
	'sqlite3.Cursor.fetchone':'''Fetches one row from the resultset.''',
	'sqlite3.Cursor.lastrowid':'''''',
	'sqlite3.Cursor.next':'''x.next() -> the next value, or raise StopIteration''',
	'sqlite3.Cursor.row_factory':'''''',
	'sqlite3.Cursor.rowcount':'''''',
	'sqlite3.Cursor.setinputsizes':'''Required by DB-API. Does nothing in pysqlite.''',
	'sqlite3.Cursor.setoutputsize':'''Required by DB-API. Does nothing in pysqlite.''',
	'sqlite3.DataError':'''''',
	'sqlite3.DataError.args':'''''',
	'sqlite3.DataError.message':'''''',
	'sqlite3.DatabaseError':'''''',
	'sqlite3.DatabaseError.args':'''''',
	'sqlite3.DatabaseError.message':'''''',
	'sqlite3.DateFromTicks':'''''',
	'sqlite3.Error':'''''',
	'sqlite3.Error.args':'''''',
	'sqlite3.Error.message':'''''',
	'sqlite3.IntegrityError':'''''',
	'sqlite3.IntegrityError.args':'''''',
	'sqlite3.IntegrityError.message':'''''',
	'sqlite3.InterfaceError':'''''',
	'sqlite3.InterfaceError.args':'''''',
	'sqlite3.InterfaceError.message':'''''',
	'sqlite3.InternalError':'''''',
	'sqlite3.InternalError.args':'''''',
	'sqlite3.InternalError.message':'''''',
	'sqlite3.NotSupportedError':'''''',
	'sqlite3.NotSupportedError.args':'''''',
	'sqlite3.NotSupportedError.message':'''''',
	'sqlite3.OperationalError':'''''',
	'sqlite3.OperationalError.args':'''''',
	'sqlite3.OperationalError.message':'''''',
	'sqlite3.PrepareProtocol':'''''',
	'sqlite3.ProgrammingError':'''''',
	'sqlite3.ProgrammingError.args':'''''',
	'sqlite3.ProgrammingError.message':'''''',
	'sqlite3.Row':'''''',
	'sqlite3.Row.keys':'''Returns the keys of the row.''',
	'sqlite3.Statement':'''''',
	'sqlite3.TimeFromTicks':'''''',
	'sqlite3.TimestampFromTicks':'''''',
	'sqlite3.Warning':'''''',
	'sqlite3.Warning.args':'''''',
	'sqlite3.Warning.message':'''''',
	'sqlite3.adapt':'''adapt(obj, protocol, alternate) -> adapt obj to given protocol. Non-standard.''',
	'sqlite3.buffer':'''buffer(object [, offset[, size]])

Create a new buffer object which references the given object.
The buffer will reference a slice of the target object from the
start of the object (or at the specified offset). The slice will
extend to the end of the target object (or with the specified size).''',
	'sqlite3.cell':'''''',
	'sqlite3.cell.cell_contents':'''''',
	'sqlite3.collections':'''''',
	'sqlite3.collections.Callable':'''''',
	'sqlite3.collections.Container':'''''',
	'sqlite3.collections.Counter':'''Dict subclass for counting hashable items.  Sometimes called a bag
or multiset.  Elements are stored as dictionary keys and their counts
are stored as dictionary values.

>>> c = Counter('abcdeabcdabcaba')  # count elements from a string

>>> c.most_common(3)                # three most common elements
[('a', 5), ('b', 4), ('c', 3)]
>>> sorted(c)                       # list all unique elements
['a', 'b', 'c', 'd', 'e']
>>> ''.join(sorted(c.elements()))   # list elements with repetitions
'aaaaabbbbcccdde'
>>> sum(c.values())                 # total of all counts
15

>>> c['a']                          # count of letter 'a'
5
>>> for elem in 'shazam':           # update counts from an iterable
...     c[elem] += 1                # by adding 1 to each element's count
>>> c['a']                          # now there are seven 'a'
7
>>> del c['b']                      # remove all 'b'
>>> c['b']                          # now there are zero 'b'
0

>>> d = Counter('simsalabim')       # make another counter
>>> c.update(d)                     # add in the second counter
>>> c['a']                          # now there are nine 'a'
9

>>> c.clear()                       # empty the counter
>>> c
Counter()

Note:  If a count is set to zero or reduced to zero, it will remain
in the counter until the entry is deleted or the counter is cleared:

>>> c = Counter('aaabbc')
>>> c['b'] -= 2                     # reduce the count of 'b' by two
>>> c.most_common()                 # 'b' is still in, but its count is zero
[('a', 3), ('c', 1), ('b', 0)]''',
	'sqlite3.collections.Counter.clear':'''D.clear() -> None.  Remove all items from D.''',
	'sqlite3.collections.Counter.copy':'''Return a shallow copy.''',
	'sqlite3.collections.Counter.elements':'''Iterator over elements repeating each as many times as its count.

>>> c = Counter('ABCABC')
>>> sorted(c.elements())
['A', 'A', 'B', 'B', 'C', 'C']

# Knuth's example for prime factors of 1836:  2**2 * 3**3 * 17**1
>>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
>>> product = 1
>>> for factor in prime_factors.elements():     # loop over factors
...     product *= factor                       # and multiply them
>>> product
1836

Note, if an element's count has been set to zero or is a negative
number, elements() will ignore it.''',
	'sqlite3.collections.Counter.fromkeys':'''''',
	'sqlite3.collections.Counter.get':'''D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.''',
	'sqlite3.collections.Counter.has_key':'''D.has_key(k) -> True if D has a key k, else False''',
	'sqlite3.collections.Counter.items':'''D.items() -> list of D's (key, value) pairs, as 2-tuples''',
	'sqlite3.collections.Counter.iteritems':'''D.iteritems() -> an iterator over the (key, value) items of D''',
	'sqlite3.collections.Counter.iterkeys':'''D.iterkeys() -> an iterator over the keys of D''',
	'sqlite3.collections.Counter.itervalues':'''D.itervalues() -> an iterator over the values of D''',
	'sqlite3.collections.Counter.keys':'''D.keys() -> list of D's keys''',
	'sqlite3.collections.Counter.most_common':'''List the n most common elements and their counts from the most
common to the least.  If n is None, then list all element counts.

>>> Counter('abcdeabcdabcaba').most_common(3)
[('a', 5), ('b', 4), ('c', 3)]''',
	'sqlite3.collections.Counter.pop':'''D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised''',
	'sqlite3.collections.Counter.popitem':'''D.popitem() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.''',
	'sqlite3.collections.Counter.setdefault':'''D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D''',
	'sqlite3.collections.Counter.subtract':'''Like dict.update() but subtracts counts instead of replacing them.
Counts can be reduced below zero.  Both the inputs and outputs are
allowed to contain zero and negative counts.

Source can be an iterable, a dictionary, or another Counter instance.

>>> c = Counter('which')
>>> c.subtract('witch')             # subtract elements from another iterable
>>> c.subtract(Counter('watch'))    # subtract elements from another counter
>>> c['h']                          # 2 in which, minus 1 in witch, minus 1 in watch
0
>>> c['w']                          # 1 in which, minus 1 in witch, minus 1 in watch
-1''',
	'sqlite3.collections.Counter.update':'''Like dict.update() but add counts instead of replacing them.

Source can be an iterable, a dictionary, or another Counter instance.

>>> c = Counter('which')
>>> c.update('witch')           # add elements from another iterable
>>> d = Counter('watch')
>>> c.update(d)                 # add elements from another counter
>>> c['h']                      # four 'h' in which, witch, and watch
4''',
	'sqlite3.collections.Counter.values':'''D.values() -> list of D's values''',
	'sqlite3.collections.Counter.viewitems':'''D.viewitems() -> a set-like object providing a view on D's items''',
	'sqlite3.collections.Counter.viewkeys':'''D.viewkeys() -> a set-like object providing a view on D's keys''',
	'sqlite3.collections.Counter.viewvalues':'''D.viewvalues() -> an object providing a view on D's values''',
	'sqlite3.collections.Hashable':'''''',
	'sqlite3.collections.ItemsView':'''''',
	'sqlite3.collections.ItemsView.isdisjoint':'''Return True if two sets have a null intersection.''',
	'sqlite3.collections.Iterable':'''''',
	'sqlite3.collections.Iterator':'''''',
	'sqlite3.collections.KeysView':'''''',
	'sqlite3.collections.KeysView.isdisjoint':'''Return True if two sets have a null intersection.''',
	'sqlite3.collections.Mapping':'''A Mapping is a generic container for associating key/value
pairs.

This class provides concrete generic implementations of all
methods except for __getitem__, __iter__, and __len__.''',
	'sqlite3.collections.MappingView':'''''',
	'sqlite3.collections.MutableMapping':'''A MutableMapping is a generic container for associating
key/value pairs.

This class provides concrete generic implementations of all
methods except for __getitem__, __setitem__, __delitem__,
__iter__, and __len__.''',
	'sqlite3.collections.MutableSequence':'''All the operations on a read-only sequence.

Concrete subclasses must provide __new__ or __init__,
__getitem__, __setitem__, __delitem__, __len__, and insert().''',
	'sqlite3.collections.MutableSet':'''A mutable set is a finite, iterable container.

This class provides concrete generic implementations of all
methods except for __contains__, __iter__, __len__,
add(), and discard().

To override the comparisons (presumably for speed, as the
semantics are fixed), all you have to do is redefine __le__ and
then the other operations will automatically follow suit.''',
	'sqlite3.collections.OrderedDict':'''Dictionary that remembers insertion order''',
	'sqlite3.collections.OrderedDict.clear':'''od.clear() -> None.  Remove all items from od.''',
	'sqlite3.collections.OrderedDict.copy':'''od.copy() -> a shallow copy of od''',
	'sqlite3.collections.OrderedDict.fromkeys':'''OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S.
If not specified, the value defaults to None.''',
	'sqlite3.collections.OrderedDict.get':'''D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.''',
	'sqlite3.collections.OrderedDict.has_key':'''D.has_key(k) -> True if D has a key k, else False''',
	'sqlite3.collections.OrderedDict.items':'''od.items() -> list of (key, value) pairs in od''',
	'sqlite3.collections.OrderedDict.iteritems':'''od.iteritems -> an iterator over the (key, value) pairs in od''',
	'sqlite3.collections.OrderedDict.iterkeys':'''od.iterkeys() -> an iterator over the keys in od''',
	'sqlite3.collections.OrderedDict.itervalues':'''od.itervalues -> an iterator over the values in od''',
	'sqlite3.collections.OrderedDict.keys':'''od.keys() -> list of keys in od''',
	'sqlite3.collections.OrderedDict.pop':'''od.pop(k[,d]) -> v, remove specified key and return the corresponding
value.  If key is not found, d is returned if given, otherwise KeyError
is raised.''',
	'sqlite3.collections.OrderedDict.popitem':'''od.popitem() -> (k, v), return and remove a (key, value) pair.
Pairs are returned in LIFO order if last is true or FIFO order if false.''',
	'sqlite3.collections.OrderedDict.setdefault':'''od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od''',
	'sqlite3.collections.OrderedDict.update':'''D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v''',
	'sqlite3.collections.OrderedDict.values':'''od.values() -> list of values in od''',
	'sqlite3.collections.OrderedDict.viewitems':'''od.viewitems() -> a set-like object providing a view on od's items''',
	'sqlite3.collections.OrderedDict.viewkeys':'''od.viewkeys() -> a set-like object providing a view on od's keys''',
	'sqlite3.collections.OrderedDict.viewvalues':'''od.viewvalues() -> an object providing a view on od's values''',
	'sqlite3.collections.Sequence':'''All the operations on a read-only sequence.

Concrete subclasses must override __new__ or __init__,
__getitem__, and __len__.''',
	'sqlite3.collections.Set':'''A set is a finite, iterable container.

This class provides concrete generic implementations of all
methods except for __contains__, __iter__ and __len__.

To override the comparisons (presumably for speed, as the
semantics are fixed), all you have to do is redefine __le__ and
then the other operations will automatically follow suit.''',
	'sqlite3.collections.Sized':'''''',
	'sqlite3.collections.ValuesView':'''''',
	'sqlite3.collections.defaultdict':'''defaultdict(default_factory[, ...]) --> dict with default factory

The default factory is called without arguments to produce
a new value when a key is not present, in __getitem__ only.
A defaultdict compares equal to a dict with the same items.
All remaining arguments are treated the same as if they were
passed to the dict constructor, including keyword arguments.''',
	'sqlite3.collections.defaultdict.clear':'''D.clear() -> None.  Remove all items from D.''',
	'sqlite3.collections.defaultdict.copy':'''D.copy() -> a shallow copy of D.''',
	'sqlite3.collections.defaultdict.default_factory':'''Factory for default value called by __missing__().''',
	'sqlite3.collections.defaultdict.fromkeys':'''dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
v defaults to None.''',
	'sqlite3.collections.defaultdict.get':'''D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.''',
	'sqlite3.collections.defaultdict.has_key':'''D.has_key(k) -> True if D has a key k, else False''',
	'sqlite3.collections.defaultdict.items':'''D.items() -> list of D's (key, value) pairs, as 2-tuples''',
	'sqlite3.collections.defaultdict.iteritems':'''D.iteritems() -> an iterator over the (key, value) items of D''',
	'sqlite3.collections.defaultdict.iterkeys':'''D.iterkeys() -> an iterator over the keys of D''',
	'sqlite3.collections.defaultdict.itervalues':'''D.itervalues() -> an iterator over the values of D''',
	'sqlite3.collections.defaultdict.keys':'''D.keys() -> list of D's keys''',
	'sqlite3.collections.defaultdict.pop':'''D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised''',
	'sqlite3.collections.defaultdict.popitem':'''D.popitem() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.''',
	'sqlite3.collections.defaultdict.setdefault':'''D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D''',
	'sqlite3.collections.defaultdict.update':'''D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k in F: D[k] = F[k]''',
	'sqlite3.collections.defaultdict.values':'''D.values() -> list of D's values''',
	'sqlite3.collections.defaultdict.viewitems':'''D.viewitems() -> a set-like object providing a view on D's items''',
	'sqlite3.collections.defaultdict.viewkeys':'''D.viewkeys() -> a set-like object providing a view on D's keys''',
	'sqlite3.collections.defaultdict.viewvalues':'''D.viewvalues() -> an object providing a view on D's values''',
	'sqlite3.collections.deque':'''deque([iterable[, maxlen]]) --> deque object

Build an ordered collection with optimized access from its endpoints.''',
	'sqlite3.collections.deque.append':'''Add an element to the right side of the deque.''',
	'sqlite3.collections.deque.appendleft':'''Add an element to the left side of the deque.''',
	'sqlite3.collections.deque.clear':'''Remove all elements from the deque.''',
	'sqlite3.collections.deque.count':'''D.count(value) -> integer -- return number of occurrences of value''',
	'sqlite3.collections.deque.extend':'''Extend the right side of the deque with elements from the iterable''',
	'sqlite3.collections.deque.extendleft':'''Extend the left side of the deque with elements from the iterable''',
	'sqlite3.collections.deque.maxlen':'''maximum size of a deque or None if unbounded''',
	'sqlite3.collections.deque.pop':'''Remove and return the rightmost element.''',
	'sqlite3.collections.deque.popleft':'''Remove and return the leftmost element.''',
	'sqlite3.collections.deque.remove':'''D.remove(value) -- remove first occurrence of value.''',
	'sqlite3.collections.deque.reverse':'''D.reverse() -- reverse *IN PLACE*''',
	'sqlite3.collections.deque.rotate':'''Rotate the deque n steps to the right (default n=1).  If n is negative, rotates left.''',
	'sqlite3.collections.namedtuple':'''Returns a new subclass of tuple with named fields.

>>> Point = namedtuple('Point', ['x', 'y'])
>>> Point.__doc__                   # docstring for the new class
'Point(x, y)'
>>> p = Point(11, y=22)             # instantiate with positional args or keywords
>>> p[0] + p[1]                     # indexable like a plain tuple
33
>>> x, y = p                        # unpack like a regular tuple
>>> x, y
(11, 22)
>>> p.x + p.y                       # fields also accessable by name
33
>>> d = p._asdict()                 # convert to a dictionary
>>> d['x']
11
>>> Point(**d)                      # convert from a dictionary
Point(x=11, y=22)
>>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
Point(x=100, y=22)''',
	'sqlite3.complete_statement':'''complete_statement(sql)

Checks if a string contains a complete SQL statement. Non-standard.''',
	'sqlite3.connect':'''connect(database[, timeout, isolation_level, detect_types, factory])

Opens a connection to the SQLite database file *database*. You can use
":memory:" to open a database connection to a database that resides in
RAM instead of on disk.''',
	'sqlite3.date':'''date(year, month, day) --> date object''',
	'sqlite3.date.ctime':'''Return ctime() style string.''',
	'sqlite3.date.day':'''''',
	'sqlite3.date.fromordinal':'''int -> date corresponding to a proleptic Gregorian ordinal.''',
	'sqlite3.date.fromtimestamp':'''timestamp -> local date from a POSIX timestamp (like time.time()).''',
	'sqlite3.date.isocalendar':'''Return a 3-tuple containing ISO year, week number, and weekday.''',
	'sqlite3.date.isoformat':'''Return string in ISO 8601 format, YYYY-MM-DD.''',
	'sqlite3.date.isoweekday':'''Return the day of the week represented by the date.
Monday == 1 ... Sunday == 7''',
	'sqlite3.date.month':'''''',
	'sqlite3.date.replace':'''Return date with new specified fields.''',
	'sqlite3.date.strftime':'''format -> strftime() style string.''',
	'sqlite3.date.timetuple':'''Return time tuple, compatible with time.localtime().''',
	'sqlite3.date.today':'''Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).''',
	'sqlite3.date.toordinal':'''Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.''',
	'sqlite3.date.weekday':'''Return the day of the week represented by the date.
Monday == 0 ... Sunday == 6''',
	'sqlite3.date.year':'''''',
	'sqlite3.datetime':'''Fast implementation of the datetime type.''',
	'sqlite3.datetime.astimezone':'''tz -> convert to local time in new timezone tz''',
	'sqlite3.datetime.combine':'''date, time -> datetime with same date and time fields''',
	'sqlite3.datetime.ctime':'''Return ctime() style string.''',
	'sqlite3.datetime.date':'''date(year, month, day) --> date object''',
	'sqlite3.datetime.date.ctime':'''Return ctime() style string.''',
	'sqlite3.datetime.date.day':'''''',
	'sqlite3.datetime.date.fromordinal':'''int -> date corresponding to a proleptic Gregorian ordinal.''',
	'sqlite3.datetime.date.fromtimestamp':'''timestamp -> local date from a POSIX timestamp (like time.time()).''',
	'sqlite3.datetime.date.isocalendar':'''Return a 3-tuple containing ISO year, week number, and weekday.''',
	'sqlite3.datetime.date.isoformat':'''Return string in ISO 8601 format, YYYY-MM-DD.''',
	'sqlite3.datetime.date.isoweekday':'''Return the day of the week represented by the date.
Monday == 1 ... Sunday == 7''',
	'sqlite3.datetime.date.month':'''''',
	'sqlite3.datetime.date.replace':'''Return date with new specified fields.''',
	'sqlite3.datetime.date.strftime':'''format -> strftime() style string.''',
	'sqlite3.datetime.date.timetuple':'''Return time tuple, compatible with time.localtime().''',
	'sqlite3.datetime.date.today':'''Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).''',
	'sqlite3.datetime.date.toordinal':'''Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.''',
	'sqlite3.datetime.date.weekday':'''Return the day of the week represented by the date.
Monday == 0 ... Sunday == 6''',
	'sqlite3.datetime.date.year':'''''',
	'sqlite3.datetime.datetime':'''datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints or longs.''',
	'sqlite3.datetime.datetime.astimezone':'''tz -> convert to local time in new timezone tz''',
	'sqlite3.datetime.datetime.combine':'''date, time -> datetime with same date and time fields''',
	'sqlite3.datetime.datetime.ctime':'''Return ctime() style string.''',
	'sqlite3.datetime.datetime.date':'''Return date object with same year, month and day.''',
	'sqlite3.datetime.datetime.day':'''''',
	'sqlite3.datetime.datetime.dst':'''Return self.tzinfo.dst(self).''',
	'sqlite3.datetime.datetime.fromordinal':'''int -> date corresponding to a proleptic Gregorian ordinal.''',
	'sqlite3.datetime.datetime.fromtimestamp':'''timestamp[, tz] -> tz's local time from POSIX timestamp.''',
	'sqlite3.datetime.datetime.hour':'''''',
	'sqlite3.datetime.datetime.isocalendar':'''Return a 3-tuple containing ISO year, week number, and weekday.''',
	'sqlite3.datetime.datetime.isoformat':'''[sep] -> string in ISO 8601 format, YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM].

sep is used to separate the year from the time, and defaults to 'T'.''',
	'sqlite3.datetime.datetime.isoweekday':'''Return the day of the week represented by the date.
Monday == 1 ... Sunday == 7''',
	'sqlite3.datetime.datetime.microsecond':'''''',
	'sqlite3.datetime.datetime.minute':'''''',
	'sqlite3.datetime.datetime.month':'''''',
	'sqlite3.datetime.datetime.now':'''[tz] -> new datetime with tz's local day and time.''',
	'sqlite3.datetime.datetime.replace':'''Return datetime with new specified fields.''',
	'sqlite3.datetime.datetime.second':'''''',
	'sqlite3.datetime.datetime.strftime':'''format -> strftime() style string.''',
	'sqlite3.datetime.datetime.strptime':'''string, format -> new datetime parsed from a string (like time.strptime()).''',
	'sqlite3.datetime.datetime.time':'''Return time object with same time but with tzinfo=None.''',
	'sqlite3.datetime.datetime.timetuple':'''Return time tuple, compatible with time.localtime().''',
	'sqlite3.datetime.datetime.timetz':'''Return time object with same time and tzinfo.''',
	'sqlite3.datetime.datetime.today':'''Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).''',
	'sqlite3.datetime.datetime.toordinal':'''Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.''',
	'sqlite3.datetime.datetime.tzinfo':'''''',
	'sqlite3.datetime.datetime.tzname':'''Return self.tzinfo.tzname(self).''',
	'sqlite3.datetime.datetime.utcfromtimestamp':'''timestamp -> UTC datetime from a POSIX timestamp (like time.time()).''',
	'sqlite3.datetime.datetime.utcnow':'''Return a new datetime representing UTC day and time.''',
	'sqlite3.datetime.datetime.utcoffset':'''Return self.tzinfo.utcoffset(self).''',
	'sqlite3.datetime.datetime.utctimetuple':'''Return UTC time tuple, compatible with time.localtime().''',
	'sqlite3.datetime.datetime.weekday':'''Return the day of the week represented by the date.
Monday == 0 ... Sunday == 6''',
	'sqlite3.datetime.datetime.year':'''''',
	'sqlite3.datetime.day':'''''',
	'sqlite3.datetime.dst':'''Return self.tzinfo.dst(self).''',
	'sqlite3.datetime.fromordinal':'''int -> date corresponding to a proleptic Gregorian ordinal.''',
	'sqlite3.datetime.fromtimestamp':'''timestamp[, tz] -> tz's local time from POSIX timestamp.''',
	'sqlite3.datetime.hour':'''''',
	'sqlite3.datetime.isocalendar':'''Return a 3-tuple containing ISO year, week number, and weekday.''',
	'sqlite3.datetime.isoformat':'''[sep] -> string in ISO 8601 format, YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM].

sep is used to separate the year from the time, and defaults to 'T'.''',
	'sqlite3.datetime.isoweekday':'''Return the day of the week represented by the date.
Monday == 1 ... Sunday == 7''',
	'sqlite3.datetime.microsecond':'''''',
	'sqlite3.datetime.minute':'''''',
	'sqlite3.datetime.month':'''''',
	'sqlite3.datetime.now':'''[tz] -> new datetime with tz's local day and time.''',
	'sqlite3.datetime.replace':'''Return datetime with new specified fields.''',
	'sqlite3.datetime.second':'''''',
	'sqlite3.datetime.strftime':'''format -> strftime() style string.''',
	'sqlite3.datetime.strptime':'''string, format -> new datetime parsed from a string (like time.strptime()).''',
	'sqlite3.datetime.time':'''time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object

All arguments are optional. tzinfo may be None, or an instance of
a tzinfo subclass. The remaining arguments may be ints or longs.''',
	'sqlite3.datetime.time.dst':'''Return self.tzinfo.dst(self).''',
	'sqlite3.datetime.time.hour':'''''',
	'sqlite3.datetime.time.isoformat':'''Return string in ISO 8601 format, HH:MM:SS[.mmmmmm][+HH:MM].''',
	'sqlite3.datetime.time.microsecond':'''''',
	'sqlite3.datetime.time.minute':'''''',
	'sqlite3.datetime.time.replace':'''Return time with new specified fields.''',
	'sqlite3.datetime.time.second':'''''',
	'sqlite3.datetime.time.strftime':'''format -> strftime() style string.''',
	'sqlite3.datetime.time.tzinfo':'''''',
	'sqlite3.datetime.time.tzname':'''Return self.tzinfo.tzname(self).''',
	'sqlite3.datetime.time.utcoffset':'''Return self.tzinfo.utcoffset(self).''',
	'sqlite3.datetime.timedelta':'''Difference between two datetime values.''',
	'sqlite3.datetime.timedelta.days':'''Number of days.''',
	'sqlite3.datetime.timedelta.microseconds':'''Number of microseconds (>= 0 and less than 1 second).''',
	'sqlite3.datetime.timedelta.seconds':'''Number of seconds (>= 0 and less than 1 day).''',
	'sqlite3.datetime.timedelta.total_seconds':'''Total seconds in the duration.''',
	'sqlite3.datetime.timetuple':'''Return time tuple, compatible with time.localtime().''',
	'sqlite3.datetime.timetz':'''Return time object with same time and tzinfo.''',
	'sqlite3.datetime.today':'''Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).''',
	'sqlite3.datetime.toordinal':'''Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.''',
	'sqlite3.datetime.tzinfo':'''Abstract base class for time zone info objects.''',
	'sqlite3.datetime.tzinfo.dst':'''datetime -> DST offset in minutes east of UTC.''',
	'sqlite3.datetime.tzinfo.fromutc':'''datetime in UTC -> datetime in local time.''',
	'sqlite3.datetime.tzinfo.tzname':'''datetime -> string name of time zone.''',
	'sqlite3.datetime.tzinfo.utcoffset':'''datetime -> minutes east of UTC (negative for west of UTC).''',
	'sqlite3.datetime.tzname':'''Return self.tzinfo.tzname(self).''',
	'sqlite3.datetime.utcfromtimestamp':'''timestamp -> UTC datetime from a POSIX timestamp (like time.time()).''',
	'sqlite3.datetime.utcnow':'''Return a new datetime representing UTC day and time.''',
	'sqlite3.datetime.utcoffset':'''Return self.tzinfo.utcoffset(self).''',
	'sqlite3.datetime.utctimetuple':'''Return UTC time tuple, compatible with time.localtime().''',
	'sqlite3.datetime.weekday':'''Return the day of the week represented by the date.
Monday == 0 ... Sunday == 6''',
	'sqlite3.datetime.year':'''''',
	'sqlite3.enable_callback_tracebacks':'''enable_callback_tracebacks(flag)

Enable or disable callback functions throwing errors to stderr.''',
	'sqlite3.enable_shared_cache':'''enable_shared_cache(do_enable)

Enable or disable shared cache mode for the calling thread.
Experimental/Non-standard.''',
	'sqlite3.register_adapter':'''register_adapter(type, callable)

Registers an adapter with pysqlite's adapter registry. Non-standard.''',
	'sqlite3.register_converter':'''register_converter(typename, callable)

Registers a converter with pysqlite. Non-standard.''',
	'sqlite3.sqlite3.dbapi2':'''''',
	'sqlite3.sqlite3.dbapi2.Cache':'''''',
	'sqlite3.sqlite3.dbapi2.Cache.display':'''For debugging only.''',
	'sqlite3.sqlite3.dbapi2.Cache.get':'''Gets an entry from the cache or calls the factory function to produce one.''',
	'sqlite3.sqlite3.dbapi2.Connection':'''SQLite database connection object.''',
	'sqlite3.sqlite3.dbapi2.Connection.DataError':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.DatabaseError':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.Error':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.IntegrityError':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.InterfaceError':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.InternalError':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.NotSupportedError':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.OperationalError':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.ProgrammingError':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.Warning':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.close':'''Closes the connection.''',
	'sqlite3.sqlite3.dbapi2.Connection.commit':'''Commit the current transaction.''',
	'sqlite3.sqlite3.dbapi2.Connection.create_aggregate':'''Creates a new aggregate. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Connection.create_collation':'''Creates a collation function. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Connection.create_function':'''Creates a new function. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Connection.cursor':'''Return a cursor for the connection.''',
	'sqlite3.sqlite3.dbapi2.Connection.enable_load_extension':'''Enable dynamic loading of SQLite extension modules. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Connection.execute':'''Executes a SQL statement. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Connection.executemany':'''Repeatedly executes a SQL statement. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Connection.executescript':'''Executes a multiple SQL statements at once. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Connection.interrupt':'''Abort any pending database operation. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Connection.isolation_level':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.iterdump':'''Returns iterator to the dump of the database in an SQL text format. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Connection.load_extension':'''Load SQLite extension module. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Connection.rollback':'''Roll back the current transaction.''',
	'sqlite3.sqlite3.dbapi2.Connection.row_factory':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.set_authorizer':'''Sets authorizer callback. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Connection.set_progress_handler':'''Sets progress handler callback. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Connection.text_factory':'''''',
	'sqlite3.sqlite3.dbapi2.Connection.total_changes':'''''',
	'sqlite3.sqlite3.dbapi2.Cursor':'''SQLite database cursor class.''',
	'sqlite3.sqlite3.dbapi2.Cursor.arraysize':'''''',
	'sqlite3.sqlite3.dbapi2.Cursor.close':'''Closes the cursor.''',
	'sqlite3.sqlite3.dbapi2.Cursor.connection':'''''',
	'sqlite3.sqlite3.dbapi2.Cursor.description':'''''',
	'sqlite3.sqlite3.dbapi2.Cursor.execute':'''Executes a SQL statement.''',
	'sqlite3.sqlite3.dbapi2.Cursor.executemany':'''Repeatedly executes a SQL statement.''',
	'sqlite3.sqlite3.dbapi2.Cursor.executescript':'''Executes a multiple SQL statements at once. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.Cursor.fetchall':'''Fetches all rows from the resultset.''',
	'sqlite3.sqlite3.dbapi2.Cursor.fetchmany':'''Fetches several rows from the resultset.''',
	'sqlite3.sqlite3.dbapi2.Cursor.fetchone':'''Fetches one row from the resultset.''',
	'sqlite3.sqlite3.dbapi2.Cursor.lastrowid':'''''',
	'sqlite3.sqlite3.dbapi2.Cursor.next':'''x.next() -> the next value, or raise StopIteration''',
	'sqlite3.sqlite3.dbapi2.Cursor.row_factory':'''''',
	'sqlite3.sqlite3.dbapi2.Cursor.rowcount':'''''',
	'sqlite3.sqlite3.dbapi2.Cursor.setinputsizes':'''Required by DB-API. Does nothing in pysqlite.''',
	'sqlite3.sqlite3.dbapi2.Cursor.setoutputsize':'''Required by DB-API. Does nothing in pysqlite.''',
	'sqlite3.sqlite3.dbapi2.DataError':'''''',
	'sqlite3.sqlite3.dbapi2.DataError.args':'''''',
	'sqlite3.sqlite3.dbapi2.DataError.message':'''''',
	'sqlite3.sqlite3.dbapi2.DatabaseError':'''''',
	'sqlite3.sqlite3.dbapi2.DatabaseError.args':'''''',
	'sqlite3.sqlite3.dbapi2.DatabaseError.message':'''''',
	'sqlite3.sqlite3.dbapi2.DateFromTicks':'''''',
	'sqlite3.sqlite3.dbapi2.Error':'''''',
	'sqlite3.sqlite3.dbapi2.Error.args':'''''',
	'sqlite3.sqlite3.dbapi2.Error.message':'''''',
	'sqlite3.sqlite3.dbapi2.IntegrityError':'''''',
	'sqlite3.sqlite3.dbapi2.IntegrityError.args':'''''',
	'sqlite3.sqlite3.dbapi2.IntegrityError.message':'''''',
	'sqlite3.sqlite3.dbapi2.InterfaceError':'''''',
	'sqlite3.sqlite3.dbapi2.InterfaceError.args':'''''',
	'sqlite3.sqlite3.dbapi2.InterfaceError.message':'''''',
	'sqlite3.sqlite3.dbapi2.InternalError':'''''',
	'sqlite3.sqlite3.dbapi2.InternalError.args':'''''',
	'sqlite3.sqlite3.dbapi2.InternalError.message':'''''',
	'sqlite3.sqlite3.dbapi2.NotSupportedError':'''''',
	'sqlite3.sqlite3.dbapi2.NotSupportedError.args':'''''',
	'sqlite3.sqlite3.dbapi2.NotSupportedError.message':'''''',
	'sqlite3.sqlite3.dbapi2.OperationalError':'''''',
	'sqlite3.sqlite3.dbapi2.OperationalError.args':'''''',
	'sqlite3.sqlite3.dbapi2.OperationalError.message':'''''',
	'sqlite3.sqlite3.dbapi2.PrepareProtocol':'''''',
	'sqlite3.sqlite3.dbapi2.ProgrammingError':'''''',
	'sqlite3.sqlite3.dbapi2.ProgrammingError.args':'''''',
	'sqlite3.sqlite3.dbapi2.ProgrammingError.message':'''''',
	'sqlite3.sqlite3.dbapi2.Row':'''''',
	'sqlite3.sqlite3.dbapi2.Row.keys':'''Returns the keys of the row.''',
	'sqlite3.sqlite3.dbapi2.Statement':'''''',
	'sqlite3.sqlite3.dbapi2.TimeFromTicks':'''''',
	'sqlite3.sqlite3.dbapi2.TimestampFromTicks':'''''',
	'sqlite3.sqlite3.dbapi2.Warning':'''''',
	'sqlite3.sqlite3.dbapi2.Warning.args':'''''',
	'sqlite3.sqlite3.dbapi2.Warning.message':'''''',
	'sqlite3.sqlite3.dbapi2.adapt':'''adapt(obj, protocol, alternate) -> adapt obj to given protocol. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.buffer':'''buffer(object [, offset[, size]])

Create a new buffer object which references the given object.
The buffer will reference a slice of the target object from the
start of the object (or at the specified offset). The slice will
extend to the end of the target object (or with the specified size).''',
	'sqlite3.sqlite3.dbapi2.cell':'''''',
	'sqlite3.sqlite3.dbapi2.cell.cell_contents':'''''',
	'sqlite3.sqlite3.dbapi2.collections':'''''',
	'sqlite3.sqlite3.dbapi2.collections.Callable':'''''',
	'sqlite3.sqlite3.dbapi2.collections.Container':'''''',
	'sqlite3.sqlite3.dbapi2.collections.Counter':'''Dict subclass for counting hashable items.  Sometimes called a bag
or multiset.  Elements are stored as dictionary keys and their counts
are stored as dictionary values.

>>> c = Counter('abcdeabcdabcaba')  # count elements from a string

>>> c.most_common(3)                # three most common elements
[('a', 5), ('b', 4), ('c', 3)]
>>> sorted(c)                       # list all unique elements
['a', 'b', 'c', 'd', 'e']
>>> ''.join(sorted(c.elements()))   # list elements with repetitions
'aaaaabbbbcccdde'
>>> sum(c.values())                 # total of all counts
15

>>> c['a']                          # count of letter 'a'
5
>>> for elem in 'shazam':           # update counts from an iterable
...     c[elem] += 1                # by adding 1 to each element's count
>>> c['a']                          # now there are seven 'a'
7
>>> del c['b']                      # remove all 'b'
>>> c['b']                          # now there are zero 'b'
0

>>> d = Counter('simsalabim')       # make another counter
>>> c.update(d)                     # add in the second counter
>>> c['a']                          # now there are nine 'a'
9

>>> c.clear()                       # empty the counter
>>> c
Counter()

Note:  If a count is set to zero or reduced to zero, it will remain
in the counter until the entry is deleted or the counter is cleared:

>>> c = Counter('aaabbc')
>>> c['b'] -= 2                     # reduce the count of 'b' by two
>>> c.most_common()                 # 'b' is still in, but its count is zero
[('a', 3), ('c', 1), ('b', 0)]''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.clear':'''D.clear() -> None.  Remove all items from D.''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.copy':'''Return a shallow copy.''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.elements':'''Iterator over elements repeating each as many times as its count.

>>> c = Counter('ABCABC')
>>> sorted(c.elements())
['A', 'A', 'B', 'B', 'C', 'C']

# Knuth's example for prime factors of 1836:  2**2 * 3**3 * 17**1
>>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
>>> product = 1
>>> for factor in prime_factors.elements():     # loop over factors
...     product *= factor                       # and multiply them
>>> product
1836

Note, if an element's count has been set to zero or is a negative
number, elements() will ignore it.''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.fromkeys':'''''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.get':'''D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.has_key':'''D.has_key(k) -> True if D has a key k, else False''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.items':'''D.items() -> list of D's (key, value) pairs, as 2-tuples''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.iteritems':'''D.iteritems() -> an iterator over the (key, value) items of D''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.iterkeys':'''D.iterkeys() -> an iterator over the keys of D''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.itervalues':'''D.itervalues() -> an iterator over the values of D''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.keys':'''D.keys() -> list of D's keys''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.most_common':'''List the n most common elements and their counts from the most
common to the least.  If n is None, then list all element counts.

>>> Counter('abcdeabcdabcaba').most_common(3)
[('a', 5), ('b', 4), ('c', 3)]''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.pop':'''D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.popitem':'''D.popitem() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.setdefault':'''D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.subtract':'''Like dict.update() but subtracts counts instead of replacing them.
Counts can be reduced below zero.  Both the inputs and outputs are
allowed to contain zero and negative counts.

Source can be an iterable, a dictionary, or another Counter instance.

>>> c = Counter('which')
>>> c.subtract('witch')             # subtract elements from another iterable
>>> c.subtract(Counter('watch'))    # subtract elements from another counter
>>> c['h']                          # 2 in which, minus 1 in witch, minus 1 in watch
0
>>> c['w']                          # 1 in which, minus 1 in witch, minus 1 in watch
-1''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.update':'''Like dict.update() but add counts instead of replacing them.

Source can be an iterable, a dictionary, or another Counter instance.

>>> c = Counter('which')
>>> c.update('witch')           # add elements from another iterable
>>> d = Counter('watch')
>>> c.update(d)                 # add elements from another counter
>>> c['h']                      # four 'h' in which, witch, and watch
4''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.values':'''D.values() -> list of D's values''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.viewitems':'''D.viewitems() -> a set-like object providing a view on D's items''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.viewkeys':'''D.viewkeys() -> a set-like object providing a view on D's keys''',
	'sqlite3.sqlite3.dbapi2.collections.Counter.viewvalues':'''D.viewvalues() -> an object providing a view on D's values''',
	'sqlite3.sqlite3.dbapi2.collections.Hashable':'''''',
	'sqlite3.sqlite3.dbapi2.collections.ItemsView':'''''',
	'sqlite3.sqlite3.dbapi2.collections.ItemsView.isdisjoint':'''Return True if two sets have a null intersection.''',
	'sqlite3.sqlite3.dbapi2.collections.Iterable':'''''',
	'sqlite3.sqlite3.dbapi2.collections.Iterator':'''''',
	'sqlite3.sqlite3.dbapi2.collections.KeysView':'''''',
	'sqlite3.sqlite3.dbapi2.collections.KeysView.isdisjoint':'''Return True if two sets have a null intersection.''',
	'sqlite3.sqlite3.dbapi2.collections.Mapping':'''A Mapping is a generic container for associating key/value
pairs.

This class provides concrete generic implementations of all
methods except for __getitem__, __iter__, and __len__.''',
	'sqlite3.sqlite3.dbapi2.collections.MappingView':'''''',
	'sqlite3.sqlite3.dbapi2.collections.MutableMapping':'''A MutableMapping is a generic container for associating
key/value pairs.

This class provides concrete generic implementations of all
methods except for __getitem__, __setitem__, __delitem__,
__iter__, and __len__.''',
	'sqlite3.sqlite3.dbapi2.collections.MutableSequence':'''All the operations on a read-only sequence.

Concrete subclasses must provide __new__ or __init__,
__getitem__, __setitem__, __delitem__, __len__, and insert().''',
	'sqlite3.sqlite3.dbapi2.collections.MutableSet':'''A mutable set is a finite, iterable container.

This class provides concrete generic implementations of all
methods except for __contains__, __iter__, __len__,
add(), and discard().

To override the comparisons (presumably for speed, as the
semantics are fixed), all you have to do is redefine __le__ and
then the other operations will automatically follow suit.''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict':'''Dictionary that remembers insertion order''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.clear':'''od.clear() -> None.  Remove all items from od.''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.copy':'''od.copy() -> a shallow copy of od''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.fromkeys':'''OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S.
If not specified, the value defaults to None.''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.get':'''D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.has_key':'''D.has_key(k) -> True if D has a key k, else False''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.items':'''od.items() -> list of (key, value) pairs in od''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.iteritems':'''od.iteritems -> an iterator over the (key, value) pairs in od''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.iterkeys':'''od.iterkeys() -> an iterator over the keys in od''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.itervalues':'''od.itervalues -> an iterator over the values in od''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.keys':'''od.keys() -> list of keys in od''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.pop':'''od.pop(k[,d]) -> v, remove specified key and return the corresponding
value.  If key is not found, d is returned if given, otherwise KeyError
is raised.''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.popitem':'''od.popitem() -> (k, v), return and remove a (key, value) pair.
Pairs are returned in LIFO order if last is true or FIFO order if false.''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.setdefault':'''od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.update':'''D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.values':'''od.values() -> list of values in od''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.viewitems':'''od.viewitems() -> a set-like object providing a view on od's items''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.viewkeys':'''od.viewkeys() -> a set-like object providing a view on od's keys''',
	'sqlite3.sqlite3.dbapi2.collections.OrderedDict.viewvalues':'''od.viewvalues() -> an object providing a view on od's values''',
	'sqlite3.sqlite3.dbapi2.collections.Sequence':'''All the operations on a read-only sequence.

Concrete subclasses must override __new__ or __init__,
__getitem__, and __len__.''',
	'sqlite3.sqlite3.dbapi2.collections.Set':'''A set is a finite, iterable container.

This class provides concrete generic implementations of all
methods except for __contains__, __iter__ and __len__.

To override the comparisons (presumably for speed, as the
semantics are fixed), all you have to do is redefine __le__ and
then the other operations will automatically follow suit.''',
	'sqlite3.sqlite3.dbapi2.collections.Sized':'''''',
	'sqlite3.sqlite3.dbapi2.collections.ValuesView':'''''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict':'''defaultdict(default_factory[, ...]) --> dict with default factory

The default factory is called without arguments to produce
a new value when a key is not present, in __getitem__ only.
A defaultdict compares equal to a dict with the same items.
All remaining arguments are treated the same as if they were
passed to the dict constructor, including keyword arguments.''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.clear':'''D.clear() -> None.  Remove all items from D.''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.copy':'''D.copy() -> a shallow copy of D.''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.default_factory':'''Factory for default value called by __missing__().''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.fromkeys':'''dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
v defaults to None.''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.get':'''D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.has_key':'''D.has_key(k) -> True if D has a key k, else False''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.items':'''D.items() -> list of D's (key, value) pairs, as 2-tuples''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.iteritems':'''D.iteritems() -> an iterator over the (key, value) items of D''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.iterkeys':'''D.iterkeys() -> an iterator over the keys of D''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.itervalues':'''D.itervalues() -> an iterator over the values of D''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.keys':'''D.keys() -> list of D's keys''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.pop':'''D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.popitem':'''D.popitem() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.setdefault':'''D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.update':'''D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k in F: D[k] = F[k]''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.values':'''D.values() -> list of D's values''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.viewitems':'''D.viewitems() -> a set-like object providing a view on D's items''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.viewkeys':'''D.viewkeys() -> a set-like object providing a view on D's keys''',
	'sqlite3.sqlite3.dbapi2.collections.defaultdict.viewvalues':'''D.viewvalues() -> an object providing a view on D's values''',
	'sqlite3.sqlite3.dbapi2.collections.deque':'''deque([iterable[, maxlen]]) --> deque object

Build an ordered collection with optimized access from its endpoints.''',
	'sqlite3.sqlite3.dbapi2.collections.deque.append':'''Add an element to the right side of the deque.''',
	'sqlite3.sqlite3.dbapi2.collections.deque.appendleft':'''Add an element to the left side of the deque.''',
	'sqlite3.sqlite3.dbapi2.collections.deque.clear':'''Remove all elements from the deque.''',
	'sqlite3.sqlite3.dbapi2.collections.deque.count':'''D.count(value) -> integer -- return number of occurrences of value''',
	'sqlite3.sqlite3.dbapi2.collections.deque.extend':'''Extend the right side of the deque with elements from the iterable''',
	'sqlite3.sqlite3.dbapi2.collections.deque.extendleft':'''Extend the left side of the deque with elements from the iterable''',
	'sqlite3.sqlite3.dbapi2.collections.deque.maxlen':'''maximum size of a deque or None if unbounded''',
	'sqlite3.sqlite3.dbapi2.collections.deque.pop':'''Remove and return the rightmost element.''',
	'sqlite3.sqlite3.dbapi2.collections.deque.popleft':'''Remove and return the leftmost element.''',
	'sqlite3.sqlite3.dbapi2.collections.deque.remove':'''D.remove(value) -- remove first occurrence of value.''',
	'sqlite3.sqlite3.dbapi2.collections.deque.reverse':'''D.reverse() -- reverse *IN PLACE*''',
	'sqlite3.sqlite3.dbapi2.collections.deque.rotate':'''Rotate the deque n steps to the right (default n=1).  If n is negative, rotates left.''',
	'sqlite3.sqlite3.dbapi2.collections.namedtuple':'''Returns a new subclass of tuple with named fields.

>>> Point = namedtuple('Point', ['x', 'y'])
>>> Point.__doc__                   # docstring for the new class
'Point(x, y)'
>>> p = Point(11, y=22)             # instantiate with positional args or keywords
>>> p[0] + p[1]                     # indexable like a plain tuple
33
>>> x, y = p                        # unpack like a regular tuple
>>> x, y
(11, 22)
>>> p.x + p.y                       # fields also accessable by name
33
>>> d = p._asdict()                 # convert to a dictionary
>>> d['x']
11
>>> Point(**d)                      # convert from a dictionary
Point(x=11, y=22)
>>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
Point(x=100, y=22)''',
	'sqlite3.sqlite3.dbapi2.complete_statement':'''complete_statement(sql)

Checks if a string contains a complete SQL statement. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.connect':'''connect(database[, timeout, isolation_level, detect_types, factory])

Opens a connection to the SQLite database file *database*. You can use
":memory:" to open a database connection to a database that resides in
RAM instead of on disk.''',
	'sqlite3.sqlite3.dbapi2.date':'''date(year, month, day) --> date object''',
	'sqlite3.sqlite3.dbapi2.date.ctime':'''Return ctime() style string.''',
	'sqlite3.sqlite3.dbapi2.date.day':'''''',
	'sqlite3.sqlite3.dbapi2.date.fromordinal':'''int -> date corresponding to a proleptic Gregorian ordinal.''',
	'sqlite3.sqlite3.dbapi2.date.fromtimestamp':'''timestamp -> local date from a POSIX timestamp (like time.time()).''',
	'sqlite3.sqlite3.dbapi2.date.isocalendar':'''Return a 3-tuple containing ISO year, week number, and weekday.''',
	'sqlite3.sqlite3.dbapi2.date.isoformat':'''Return string in ISO 8601 format, YYYY-MM-DD.''',
	'sqlite3.sqlite3.dbapi2.date.isoweekday':'''Return the day of the week represented by the date.
Monday == 1 ... Sunday == 7''',
	'sqlite3.sqlite3.dbapi2.date.month':'''''',
	'sqlite3.sqlite3.dbapi2.date.replace':'''Return date with new specified fields.''',
	'sqlite3.sqlite3.dbapi2.date.strftime':'''format -> strftime() style string.''',
	'sqlite3.sqlite3.dbapi2.date.timetuple':'''Return time tuple, compatible with time.localtime().''',
	'sqlite3.sqlite3.dbapi2.date.today':'''Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).''',
	'sqlite3.sqlite3.dbapi2.date.toordinal':'''Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.''',
	'sqlite3.sqlite3.dbapi2.date.weekday':'''Return the day of the week represented by the date.
Monday == 0 ... Sunday == 6''',
	'sqlite3.sqlite3.dbapi2.date.year':'''''',
	'sqlite3.sqlite3.dbapi2.datetime':'''Fast implementation of the datetime type.''',
	'sqlite3.sqlite3.dbapi2.datetime.astimezone':'''tz -> convert to local time in new timezone tz''',
	'sqlite3.sqlite3.dbapi2.datetime.combine':'''date, time -> datetime with same date and time fields''',
	'sqlite3.sqlite3.dbapi2.datetime.ctime':'''Return ctime() style string.''',
	'sqlite3.sqlite3.dbapi2.datetime.date':'''date(year, month, day) --> date object''',
	'sqlite3.sqlite3.dbapi2.datetime.date.ctime':'''Return ctime() style string.''',
	'sqlite3.sqlite3.dbapi2.datetime.date.day':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.date.fromordinal':'''int -> date corresponding to a proleptic Gregorian ordinal.''',
	'sqlite3.sqlite3.dbapi2.datetime.date.fromtimestamp':'''timestamp -> local date from a POSIX timestamp (like time.time()).''',
	'sqlite3.sqlite3.dbapi2.datetime.date.isocalendar':'''Return a 3-tuple containing ISO year, week number, and weekday.''',
	'sqlite3.sqlite3.dbapi2.datetime.date.isoformat':'''Return string in ISO 8601 format, YYYY-MM-DD.''',
	'sqlite3.sqlite3.dbapi2.datetime.date.isoweekday':'''Return the day of the week represented by the date.
Monday == 1 ... Sunday == 7''',
	'sqlite3.sqlite3.dbapi2.datetime.date.month':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.date.replace':'''Return date with new specified fields.''',
	'sqlite3.sqlite3.dbapi2.datetime.date.strftime':'''format -> strftime() style string.''',
	'sqlite3.sqlite3.dbapi2.datetime.date.timetuple':'''Return time tuple, compatible with time.localtime().''',
	'sqlite3.sqlite3.dbapi2.datetime.date.today':'''Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).''',
	'sqlite3.sqlite3.dbapi2.datetime.date.toordinal':'''Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.''',
	'sqlite3.sqlite3.dbapi2.datetime.date.weekday':'''Return the day of the week represented by the date.
Monday == 0 ... Sunday == 6''',
	'sqlite3.sqlite3.dbapi2.datetime.date.year':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime':'''datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints or longs.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.astimezone':'''tz -> convert to local time in new timezone tz''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.combine':'''date, time -> datetime with same date and time fields''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.ctime':'''Return ctime() style string.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.date':'''Return date object with same year, month and day.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.day':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.dst':'''Return self.tzinfo.dst(self).''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.fromordinal':'''int -> date corresponding to a proleptic Gregorian ordinal.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.fromtimestamp':'''timestamp[, tz] -> tz's local time from POSIX timestamp.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.hour':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.isocalendar':'''Return a 3-tuple containing ISO year, week number, and weekday.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.isoformat':'''[sep] -> string in ISO 8601 format, YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM].

sep is used to separate the year from the time, and defaults to 'T'.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.isoweekday':'''Return the day of the week represented by the date.
Monday == 1 ... Sunday == 7''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.microsecond':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.minute':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.month':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.now':'''[tz] -> new datetime with tz's local day and time.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.replace':'''Return datetime with new specified fields.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.second':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.strftime':'''format -> strftime() style string.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.strptime':'''string, format -> new datetime parsed from a string (like time.strptime()).''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.time':'''Return time object with same time but with tzinfo=None.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.timetuple':'''Return time tuple, compatible with time.localtime().''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.timetz':'''Return time object with same time and tzinfo.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.today':'''Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.toordinal':'''Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.tzinfo':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.tzname':'''Return self.tzinfo.tzname(self).''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.utcfromtimestamp':'''timestamp -> UTC datetime from a POSIX timestamp (like time.time()).''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.utcnow':'''Return a new datetime representing UTC day and time.''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.utcoffset':'''Return self.tzinfo.utcoffset(self).''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.utctimetuple':'''Return UTC time tuple, compatible with time.localtime().''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.weekday':'''Return the day of the week represented by the date.
Monday == 0 ... Sunday == 6''',
	'sqlite3.sqlite3.dbapi2.datetime.datetime.year':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.day':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.dst':'''Return self.tzinfo.dst(self).''',
	'sqlite3.sqlite3.dbapi2.datetime.fromordinal':'''int -> date corresponding to a proleptic Gregorian ordinal.''',
	'sqlite3.sqlite3.dbapi2.datetime.fromtimestamp':'''timestamp[, tz] -> tz's local time from POSIX timestamp.''',
	'sqlite3.sqlite3.dbapi2.datetime.hour':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.isocalendar':'''Return a 3-tuple containing ISO year, week number, and weekday.''',
	'sqlite3.sqlite3.dbapi2.datetime.isoformat':'''[sep] -> string in ISO 8601 format, YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM].

sep is used to separate the year from the time, and defaults to 'T'.''',
	'sqlite3.sqlite3.dbapi2.datetime.isoweekday':'''Return the day of the week represented by the date.
Monday == 1 ... Sunday == 7''',
	'sqlite3.sqlite3.dbapi2.datetime.microsecond':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.minute':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.month':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.now':'''[tz] -> new datetime with tz's local day and time.''',
	'sqlite3.sqlite3.dbapi2.datetime.replace':'''Return datetime with new specified fields.''',
	'sqlite3.sqlite3.dbapi2.datetime.second':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.strftime':'''format -> strftime() style string.''',
	'sqlite3.sqlite3.dbapi2.datetime.strptime':'''string, format -> new datetime parsed from a string (like time.strptime()).''',
	'sqlite3.sqlite3.dbapi2.datetime.time':'''time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object

All arguments are optional. tzinfo may be None, or an instance of
a tzinfo subclass. The remaining arguments may be ints or longs.''',
	'sqlite3.sqlite3.dbapi2.datetime.time.dst':'''Return self.tzinfo.dst(self).''',
	'sqlite3.sqlite3.dbapi2.datetime.time.hour':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.time.isoformat':'''Return string in ISO 8601 format, HH:MM:SS[.mmmmmm][+HH:MM].''',
	'sqlite3.sqlite3.dbapi2.datetime.time.microsecond':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.time.minute':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.time.replace':'''Return time with new specified fields.''',
	'sqlite3.sqlite3.dbapi2.datetime.time.second':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.time.strftime':'''format -> strftime() style string.''',
	'sqlite3.sqlite3.dbapi2.datetime.time.tzinfo':'''''',
	'sqlite3.sqlite3.dbapi2.datetime.time.tzname':'''Return self.tzinfo.tzname(self).''',
	'sqlite3.sqlite3.dbapi2.datetime.time.utcoffset':'''Return self.tzinfo.utcoffset(self).''',
	'sqlite3.sqlite3.dbapi2.datetime.timedelta':'''Difference between two datetime values.''',
	'sqlite3.sqlite3.dbapi2.datetime.timedelta.days':'''Number of days.''',
	'sqlite3.sqlite3.dbapi2.datetime.timedelta.microseconds':'''Number of microseconds (>= 0 and less than 1 second).''',
	'sqlite3.sqlite3.dbapi2.datetime.timedelta.seconds':'''Number of seconds (>= 0 and less than 1 day).''',
	'sqlite3.sqlite3.dbapi2.datetime.timedelta.total_seconds':'''Total seconds in the duration.''',
	'sqlite3.sqlite3.dbapi2.datetime.timetuple':'''Return time tuple, compatible with time.localtime().''',
	'sqlite3.sqlite3.dbapi2.datetime.timetz':'''Return time object with same time and tzinfo.''',
	'sqlite3.sqlite3.dbapi2.datetime.today':'''Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).''',
	'sqlite3.sqlite3.dbapi2.datetime.toordinal':'''Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.''',
	'sqlite3.sqlite3.dbapi2.datetime.tzinfo':'''Abstract base class for time zone info objects.''',
	'sqlite3.sqlite3.dbapi2.datetime.tzinfo.dst':'''datetime -> DST offset in minutes east of UTC.''',
	'sqlite3.sqlite3.dbapi2.datetime.tzinfo.fromutc':'''datetime in UTC -> datetime in local time.''',
	'sqlite3.sqlite3.dbapi2.datetime.tzinfo.tzname':'''datetime -> string name of time zone.''',
	'sqlite3.sqlite3.dbapi2.datetime.tzinfo.utcoffset':'''datetime -> minutes east of UTC (negative for west of UTC).''',
	'sqlite3.sqlite3.dbapi2.datetime.tzname':'''Return self.tzinfo.tzname(self).''',
	'sqlite3.sqlite3.dbapi2.datetime.utcfromtimestamp':'''timestamp -> UTC datetime from a POSIX timestamp (like time.time()).''',
	'sqlite3.sqlite3.dbapi2.datetime.utcnow':'''Return a new datetime representing UTC day and time.''',
	'sqlite3.sqlite3.dbapi2.datetime.utcoffset':'''Return self.tzinfo.utcoffset(self).''',
	'sqlite3.sqlite3.dbapi2.datetime.utctimetuple':'''Return UTC time tuple, compatible with time.localtime().''',
	'sqlite3.sqlite3.dbapi2.datetime.weekday':'''Return the day of the week represented by the date.
Monday == 0 ... Sunday == 6''',
	'sqlite3.sqlite3.dbapi2.datetime.year':'''''',
	'sqlite3.sqlite3.dbapi2.enable_callback_tracebacks':'''enable_callback_tracebacks(flag)

Enable or disable callback functions throwing errors to stderr.''',
	'sqlite3.sqlite3.dbapi2.enable_shared_cache':'''enable_shared_cache(do_enable)

Enable or disable shared cache mode for the calling thread.
Experimental/Non-standard.''',
	'sqlite3.sqlite3.dbapi2.register_adapter':'''register_adapter(type, callable)

Registers an adapter with pysqlite's adapter registry. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.register_converter':'''register_converter(typename, callable)

Registers a converter with pysqlite. Non-standard.''',
	'sqlite3.sqlite3.dbapi2.time':'''This module provides various functions to manipulate time values.

There are two standard representations of time.  One is the number
of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
or a floating point number (to represent fractions of seconds).
The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
The actual value can be retrieved by calling gmtime(0).

The other representation is a tuple of 9 integers giving local time.
The tuple items are:
  year (four digits, e.g. 1998)
  month (1-12)
  day (1-31)
  hours (0-23)
  minutes (0-59)
  seconds (0-59)
  weekday (0-6, Monday is 0)
  Julian day (day in the year, 1-366)
  DST (Daylight Savings Time) flag (-1, 0 or 1)
If the DST flag is 0, the time is given in the regular time zone;
if it is 1, the time is given in the DST time zone;
if it is -1, mktime() should guess based on the date and time.

Variables:

timezone -- difference in seconds between UTC and local standard time
altzone -- difference in  seconds between UTC and local DST time
daylight -- whether local time should reflect DST
tzname -- tuple of (standard time zone name, DST time zone name)

Functions:

time() -- return current time in seconds since the Epoch as a float
clock() -- return CPU time since process start as a float
sleep() -- delay for a number of seconds given as a float
gmtime() -- convert seconds since Epoch to UTC tuple
localtime() -- convert seconds since Epoch to local time tuple
asctime() -- convert time tuple to string
ctime() -- convert time in seconds to string
mktime() -- convert local time tuple to seconds since Epoch
strftime() -- convert time tuple to string according to format specification
strptime() -- parse string to time tuple according to format specification
tzset() -- change the local timezone''',
	'sqlite3.sqlite3.dbapi2.time.asctime':'''asctime([tuple]) -> string

Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
When the time tuple is not present, current time as returned by localtime()
is used.''',
	'sqlite3.sqlite3.dbapi2.time.clock':'''clock() -> floating point number

Return the CPU time or real time since the start of the process or since
the first call to clock().  This has as much precision as the system
records.''',
	'sqlite3.sqlite3.dbapi2.time.ctime':'''ctime(seconds) -> string

Convert a time in seconds since the Epoch to a string in local time.
This is equivalent to asctime(localtime(seconds)). When the time tuple is
not present, current time as returned by localtime() is used.''',
	'sqlite3.sqlite3.dbapi2.time.dst':'''Return self.tzinfo.dst(self).''',
	'sqlite3.sqlite3.dbapi2.time.gmtime':'''gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                       tm_sec, tm_wday, tm_yday, tm_isdst)

Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
GMT).  When 'seconds' is not passed in, convert the current time instead.''',
	'sqlite3.sqlite3.dbapi2.time.hour':'''''',
	'sqlite3.sqlite3.dbapi2.time.isoformat':'''Return string in ISO 8601 format, HH:MM:SS[.mmmmmm][+HH:MM].''',
	'sqlite3.sqlite3.dbapi2.time.localtime':'''localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                          tm_sec,tm_wday,tm_yday,tm_isdst)

Convert seconds since the Epoch to a time tuple expressing local time.
When 'seconds' is not passed in, convert the current time instead.''',
	'sqlite3.sqlite3.dbapi2.time.microsecond':'''''',
	'sqlite3.sqlite3.dbapi2.time.minute':'''''',
	'sqlite3.sqlite3.dbapi2.time.mktime':'''mktime(tuple) -> floating point number

Convert a time tuple in local time to seconds since the Epoch.''',
	'sqlite3.sqlite3.dbapi2.time.replace':'''Return time with new specified fields.''',
	'sqlite3.sqlite3.dbapi2.time.second':'''''',
	'sqlite3.sqlite3.dbapi2.time.sleep':'''sleep(seconds)

Delay execution for a given number of seconds.  The argument may be
a floating point number for subsecond precision.''',
	'sqlite3.sqlite3.dbapi2.time.strftime':'''strftime(format[, tuple]) -> string

Convert a time tuple to a string according to a format specification.
See the library reference manual for formatting codes. When the time tuple
is not present, current time as returned by localtime() is used.''',
	'sqlite3.sqlite3.dbapi2.time.strptime':'''strptime(string, format) -> struct_time

Parse a string to a time tuple according to a format specification.
See the library reference manual for formatting codes (same as strftime()).''',
	'sqlite3.sqlite3.dbapi2.time.struct_time':'''The time value as returned by gmtime(), localtime(), and strptime(), and
accepted by asctime(), mktime() and strftime().  May be considered as a
sequence of 9 integers.

Note that several fields' values are not the same as those defined by
the C language standard for struct tm.  For example, the value of the
field tm_year is the actual year, not year - 1900.  See individual
fields' descriptions for details.''',
	'sqlite3.sqlite3.dbapi2.time.struct_time.tm_hour':'''hours, range [0, 23]''',
	'sqlite3.sqlite3.dbapi2.time.struct_time.tm_isdst':'''1 if summer time is in effect, 0 if not, and -1 if unknown''',
	'sqlite3.sqlite3.dbapi2.time.struct_time.tm_mday':'''day of month, range [1, 31]''',
	'sqlite3.sqlite3.dbapi2.time.struct_time.tm_min':'''minutes, range [0, 59]''',
	'sqlite3.sqlite3.dbapi2.time.struct_time.tm_mon':'''month of year, range [1, 12]''',
	'sqlite3.sqlite3.dbapi2.time.struct_time.tm_sec':'''seconds, range [0, 61])''',
	'sqlite3.sqlite3.dbapi2.time.struct_time.tm_wday':'''day of week, range [0, 6], Monday is 0''',
	'sqlite3.sqlite3.dbapi2.time.struct_time.tm_yday':'''day of year, range [1, 366]''',
	'sqlite3.sqlite3.dbapi2.time.struct_time.tm_year':'''year, for example, 1993''',
	'sqlite3.sqlite3.dbapi2.time.time':'''time() -> floating point number

Return the current time in seconds since the Epoch.
Fractions of a second may be present if the system clock provides them.''',
	'sqlite3.sqlite3.dbapi2.time.tzinfo':'''''',
	'sqlite3.sqlite3.dbapi2.time.tzname':'''Return self.tzinfo.tzname(self).''',
	'sqlite3.sqlite3.dbapi2.time.utcoffset':'''Return self.tzinfo.utcoffset(self).''',
	'sqlite3.time':'''This module provides various functions to manipulate time values.

There are two standard representations of time.  One is the number
of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
or a floating point number (to represent fractions of seconds).
The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
The actual value can be retrieved by calling gmtime(0).

The other representation is a tuple of 9 integers giving local time.
The tuple items are:
  year (four digits, e.g. 1998)
  month (1-12)
  day (1-31)
  hours (0-23)
  minutes (0-59)
  seconds (0-59)
  weekday (0-6, Monday is 0)
  Julian day (day in the year, 1-366)
  DST (Daylight Savings Time) flag (-1, 0 or 1)
If the DST flag is 0, the time is given in the regular time zone;
if it is 1, the time is given in the DST time zone;
if it is -1, mktime() should guess based on the date and time.

Variables:

timezone -- difference in seconds between UTC and local standard time
altzone -- difference in  seconds between UTC and local DST time
daylight -- whether local time should reflect DST
tzname -- tuple of (standard time zone name, DST time zone name)

Functions:

time() -- return current time in seconds since the Epoch as a float
clock() -- return CPU time since process start as a float
sleep() -- delay for a number of seconds given as a float
gmtime() -- convert seconds since Epoch to UTC tuple
localtime() -- convert seconds since Epoch to local time tuple
asctime() -- convert time tuple to string
ctime() -- convert time in seconds to string
mktime() -- convert local time tuple to seconds since Epoch
strftime() -- convert time tuple to string according to format specification
strptime() -- parse string to time tuple according to format specification
tzset() -- change the local timezone''',
	'sqlite3.time.asctime':'''asctime([tuple]) -> string

Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
When the time tuple is not present, current time as returned by localtime()
is used.''',
	'sqlite3.time.clock':'''clock() -> floating point number

Return the CPU time or real time since the start of the process or since
the first call to clock().  This has as much precision as the system
records.''',
	'sqlite3.time.ctime':'''ctime(seconds) -> string

Convert a time in seconds since the Epoch to a string in local time.
This is equivalent to asctime(localtime(seconds)). When the time tuple is
not present, current time as returned by localtime() is used.''',
	'sqlite3.time.dst':'''Return self.tzinfo.dst(self).''',
	'sqlite3.time.gmtime':'''gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                       tm_sec, tm_wday, tm_yday, tm_isdst)

Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
GMT).  When 'seconds' is not passed in, convert the current time instead.''',
	'sqlite3.time.hour':'''''',
	'sqlite3.time.isoformat':'''Return string in ISO 8601 format, HH:MM:SS[.mmmmmm][+HH:MM].''',
	'sqlite3.time.localtime':'''localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                          tm_sec,tm_wday,tm_yday,tm_isdst)

Convert seconds since the Epoch to a time tuple expressing local time.
When 'seconds' is not passed in, convert the current time instead.''',
	'sqlite3.time.microsecond':'''''',
	'sqlite3.time.minute':'''''',
	'sqlite3.time.mktime':'''mktime(tuple) -> floating point number

Convert a time tuple in local time to seconds since the Epoch.''',
	'sqlite3.time.replace':'''Return time with new specified fields.''',
	'sqlite3.time.second':'''''',
	'sqlite3.time.sleep':'''sleep(seconds)

Delay execution for a given number of seconds.  The argument may be
a floating point number for subsecond precision.''',
	'sqlite3.time.strftime':'''strftime(format[, tuple]) -> string

Convert a time tuple to a string according to a format specification.
See the library reference manual for formatting codes. When the time tuple
is not present, current time as returned by localtime() is used.''',
	'sqlite3.time.strptime':'''strptime(string, format) -> struct_time

Parse a string to a time tuple according to a format specification.
See the library reference manual for formatting codes (same as strftime()).''',
	'sqlite3.time.struct_time':'''The time value as returned by gmtime(), localtime(), and strptime(), and
accepted by asctime(), mktime() and strftime().  May be considered as a
sequence of 9 integers.

Note that several fields' values are not the same as those defined by
the C language standard for struct tm.  For example, the value of the
field tm_year is the actual year, not year - 1900.  See individual
fields' descriptions for details.''',
	'sqlite3.time.struct_time.tm_hour':'''hours, range [0, 23]''',
	'sqlite3.time.struct_time.tm_isdst':'''1 if summer time is in effect, 0 if not, and -1 if unknown''',
	'sqlite3.time.struct_time.tm_mday':'''day of month, range [1, 31]''',
	'sqlite3.time.struct_time.tm_min':'''minutes, range [0, 59]''',
	'sqlite3.time.struct_time.tm_mon':'''month of year, range [1, 12]''',
	'sqlite3.time.struct_time.tm_sec':'''seconds, range [0, 61])''',
	'sqlite3.time.struct_time.tm_wday':'''day of week, range [0, 6], Monday is 0''',
	'sqlite3.time.struct_time.tm_yday':'''day of year, range [1, 366]''',
	'sqlite3.time.struct_time.tm_year':'''year, for example, 1993''',
	'sqlite3.time.time':'''time() -> floating point number

Return the current time in seconds since the Epoch.
Fractions of a second may be present if the system clock provides them.''',
	'sqlite3.time.tzinfo':'''''',
	'sqlite3.time.tzname':'''Return self.tzinfo.tzname(self).''',
	'sqlite3.time.utcoffset':'''Return self.tzinfo.utcoffset(self).''',
}
