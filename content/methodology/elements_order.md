# 🧠 **What Should You Create First When Writing Code?**

**Interface? Unit? Test? Implementation? What’s the right order?**

This is a great question — the order depends on your development approach and personal or team coding style. Below are some common strategies and their recommended workflows:

---

## ✅ **1. Test-Driven Development (TDD)**

**Order: Test ➡ Interface ➡ Implementation**

1. **Write a test first** – It will fail at first because the functionality doesn't exist yet.
2. **Define the interface** – Create the minimum structure needed so the test compiles or runs.
3. **Write the implementation** – Make the code work until the test passes.

🔁 Then you refactor and move on to the next test.

🟢 **Advantages**:

* You build only what’s needed.
* Code is always testable and verified.
* Encourages modularity and thoughtful design.

---

## ✅ **2. Interface-first / API-first Approach**

**Order: Interface ➡ Test ➡ Implementation**

1. **Define the public interface or contract** – e.g., a class, function signature, or API endpoint.
2. **Write tests against that interface**.
3. **Implement the functionality to fulfill the contract**.

🟢 **Advantages**:

* Encourages good API design.
* Great for teamwork — others can start using the interface even before it’s implemented.

---

## ❌ **3. Classic Approach (Implementation First)**

**Order: Implementation ➡ Test (optional) ➡ Interface (if needed)**

1. **Write the code** to solve the problem directly.
2. **Maybe add tests** afterward.
3. **The interface** evolves as a side effect.

🔴 **Disadvantages**:

* Tests may be harder to write later.
* Code often ends up tightly coupled or messy.
* Less thoughtful design.

---

## ✅ **Best Practice Recommendation:**

* Use **TDD** for critical or logic-heavy components.
* Use **API-first** for services, libraries, or systems with external consumers.
* Always try to **write tests early**, before or alongside your implementation — not as an afterthought.

---

## Example: Building a `UserService`

1. ✍️ **Write a test**:

   ```python
   def test_create_user():
       service = UserService()
       user = service.create_user("John", "john@example.com")
       assert user.name == "John"
   ```

2. ✍️ **Define the interface** (`UserService` with a `create_user` method).

3. ✍️ **Write the implementation** of the method.

---

Would you like to see a full working example using TDD or API-first? I can put one together for you.
