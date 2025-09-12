# Pizza Ordering System

Welcome to the **Pizza Ordering System**! In this project, you'll learn about **creational design patterns** in Python and practice **Git**.
In this project, you'll learn about **creational design patterns** in Python and practice **Git**.

This repo is structured so you can practice **Singleton**, **Factory Method**, and **Abstract Factory**, manage orders, and track changes with Git.

---

## Learning Goals

By the end of this exercise, you will:

1. Understand **Singleton** (one instance of a class - `OrderManager`).
2. Understand **Factory Method** (creating objects in a clean, centralized way - `PizzaFactory`).
3. Understand **Abstract Factory** (creating families of related objects - Italian vs American pizzas).
4. Work with Python objects and track **object state** (`prepared` vs `not prepared`).
5. Learn Git basics: clone, branch, add, commit, push.

---

## Project Structure

```
pizza_ordering_system/
│
├─ pizza.py        # Contains Pizza class and PizzaFactories
├─ order.py        # Contains Singleton OrderManager
└─ README.md
```

---

## How to Run

1. **Clone the repo**:

```bash
git clone https://github.com/ami232/pizza_ordering_system.git
cd pizza_ordering_system
```

2. **Create your own branch**:

```bash
git branch yourname_branch
git checkout yourname_branch
# pro tip: you can combine both steps into
git checkout -b yourname_branch
```

3. **Run Python code** to test orders:

```python
from pizza import PizzaFactory, ItalianPizzaFactory, AmericanPizzaFactory
from order import OrderManager

factory = PizzaFactory()
manager = OrderManager()

# Factory Method
pizza = factory.create_margherita()
manager.add_order([pizza])
manager.list_orders()
manager.prepare_order(1)

# Abstract Factory
italian_factory = ItalianPizzaFactory()
american_factory = AmericanPizzaFactory()

italian_pizza = italian_factory.create_margherita()
american_pizza = american_factory.create_margherita()

manager.add_order([italian_pizza])
manager.add_order([american_pizza])
manager.list_orders()
```


## Tasks / Exercises

### Deliverables
Upload a screenshots of your git graph and PRs to blackboard at the end of the class.

### Step 0 - If you make changes to the codebase, commit your work before the next step

* Stage your changes:

```bash
git add .
```

* Commit with a message:

```bash
git commit -m "Add {describe new functionality}"
```

* Push your branch:

```bash
git push origin yourname_branch
```

### Step 1 - Place Orders

* Use `PizzaFactory` to create pizzas (`Margherita`, `Pepperoni`, `Veggie`).
* Add them to `OrderManager`.
* Check order status with `manager.list_orders()`.

### Step 2 - Add a New Pizza Type

* Extend `PizzaFactory` to include a new pizza: **Hawaiian**.
* Test adding and preparing your new pizza.

### Step 3 - Pull changes from main into your branch
```bash
git checkout yourname_branch
git merge origin/main
```
And fix conflicts

### Step 3 - Prepare Orders

* Implement `manager.prepare_order(order_id)` to prepare pizzas.
* Confirm the `prepared` state is updated correctly.

### Step 4 - Abstract Factory
* Create a new branch `yourname_pizza_factory`
* Implement a new concrete factory `{YourName}PizzaFactory` using `PizzaFactoryAbstract`
* Add a new type of pizza you want your factory to have
* Push your changes to the git server (GitHub) and open a PR between `yourname_pizza_factory` and main.
* Pick a classmate and review each other's PRs, leaving comments and approving if applicable.
* Let the professor know when you're done for PR approval.
* Merge your changes into main.

### Step 5 - Extra functionality (bonus)

* Implement extra functionality of your choice in a branch called `yourname_extra_{functionality}`
* Follow similar steps to those in Step 4.

---

