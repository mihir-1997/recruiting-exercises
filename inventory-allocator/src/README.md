# Solution

Terms used for output

* `fulfilled_order` Items that can be shipped as there is enough inventory in warehouse(s)
* `pending_order` Items that cannot be shipped due to shortage 

## Directory Structure

```
.
├── InventoryAllocator
│   ├── __init__.py
│   └── inventory_allocator.py
├── Makefile
├── README.md
└── unittests.py
```

## How to run?

`Makefile` inside `src` folder can be used to test the solution. It has three commands

1. `make run` to run single file `inventory_allocator.py`
2. `make test` to run all unittests
3. `make help` to get help 

### Steps

1. Switch directory to `src`
2. (Optional) `make run`
3. `make test`