# Warehouse-Management
This program implements the basics of a warehouse inventory management system. The warehouse contains Items packed into
Containers. There are several sizes of container, each with different capacities:

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
