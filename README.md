# Warehouse-Management
<span style="font-size:4em;">LOVE!This program implements the basics of a warehouse inventory management system. The warehouse contains Items packed into
Containers. There are several sizes of container, each with different capacities: </span>

**Container**  **Capacity** (in 'volume units')

| Container |  Capacity |
|---|---|
| Warehouse |  Infinite |
|  Shelf  |  100 units |
|   Bin | 10 units  |
|  Box  |  5 units |
|   Bag   |  2 units |
## Management Design
Items vary in size from 1 to 20 volume units. Any Container can hold a combination of Items and other Containers smaller than itself, up to that Container's maximum capacity. You can assume that a Container's
capacity is the same as its exterior size, so a Box would occupy 5
volume units in a Bin. The exterior size of a Container is not affected
by its contents.

### All Containers must have the following methods:
  - len(): Returns the total number of objects within the
    Container. Objects within Containers inside the Container are not
    counted; a Bin containing a Box containing a Bag containing an Item
    will have a length of 1.
  - count(): Return the total number of objects within the Container,
    including other Containers and their contents. A Bin containing a
    Box containing a Bag containing an Item will have a count() of 3.
  - add(thing): Attempt to put a given object ('thing') in the
    Container. If there is not enough room, the add fails and the method
    returns False. If successful, the method returns True and automatically remove the added
object from the Container it previously occupied, so it cannot be in two
places at once.
  - contains(thing): Check to see if a given 'thing' is within a
    Container, or within a Container within the Container. Returns
    True/False.
  - remove([thing]): This method can do two things. If 'thing' is
    None or not provided, the last object added to the Container is
    removed from the Container and returned. If a specific 'thing' is
    specified, that specific 'thing' is removed. In either case, the
    method returns either the removed object or `None` (if the
    Container is empty or does not contain the specified object).
  - pack(thing): Attempt to put a given object into the Container.
    Unlike add(), the method will attempt to find room for the object
    inside any of the Containers within it and automatically remove the added
object from the Container it previously occupied, so it cannot be in two
places at once.
  - extract(thing): Remove a given object ('thing') from the Container
or any Container within it. Unlike remove(), this method requires a specific
object. This method should return the extracted object, or `None` if 'thing'
is not anywhere within the Container.
