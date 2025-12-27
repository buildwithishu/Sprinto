# 🧩 Application Purpose (Clear & Real)

You are building an **internal work management system** for companies where:

* Each **company (organization)** manages its teams
* Employees work on tasks
* Work is tracked using **priority, deadlines, and effort points**
* Access depends on **job role**

Think of it as a **lightweight Jira for internal teams**.

---

## 1️⃣ What the Application Does (At a High Level)

Each organization can:

* Create teams
* Add employees
* Assign work
* Track effort vs delivery
* Monitor workload and performance

Each organization’s data is **completely isolated**.

---

## 2️⃣ Main Entities (What Exists in the System)

### Organization

* Represents one company
* Owns all data below it
* No data is shared with other organizations

---

### Employee

* A person working in the organization
* Belongs to one organization
* Can be part of multiple teams
* Receives tasks

---

### Team

* A group inside an organization
* Used to organize employees by function (Backend, Frontend, QA, etc.)
* Exists only inside one organization

---

### Task

* A unit of work
* Assigned to **one employee**
* Belongs to **one team**
* Has delivery expectations

---

## 3️⃣ Task Properties (What We Track)

Each task has:

* **Title & description**
* **Priority**

  * Low
  * Medium
  * High
* **Deadline**
* **Story points** (estimated effort)
* **Dev points** (actual effort taken)
* **Status**

  * Open
  * In progress
  * Completed

This helps measure:

* Workload
* Delivery accuracy
* Team velocity

---

## 4️⃣ Roles (Very Clearly Defined)

### 1. Owner

**Who they are**

* Founder / top-level authority

**What they can do**

* Create organization
* Add/remove employees
* Create teams
* Assign managers
* See everything

---

### 2. Admin

**Who they are**

* HR / operations

**What they can do**

* Add/remove employees
* Create teams
* Assign employees to teams
* View all tasks
* Cannot delete organization

---

### 3. Manager

**Who they are**

* Team lead / project lead

**What they can do**

* Create tasks
* Assign tasks to employees
* Change task priority and deadlines
* View tasks of their teams
* Track team workload

---

### 4. Employee

**Who they are**

* Individual contributor / developer

**What they can do**

* View their own tasks
* Update task status
* Fill dev points after completion
* Cannot assign tasks
* Cannot view others’ tasks

---

## 5️⃣ How Work Flows (Realistic Scenario)

1. Owner creates organization
2. Admin adds employees
3. Admin creates teams
4. Employees are added to teams
5. Manager creates tasks
6. Manager assigns tasks to employees
7. Employee works on task
8. Employee marks task completed
9. System records:

   * Deadline vs completion
   * Story points vs dev points

---

## 6️⃣ What the Organization Gets From This

### For Management

* Who is overloaded
* Which team is slow or fast
* Estimation accuracy
* Task completion trends

### For Employees

* Clear responsibilities
* No confusion about ownership
* Fair workload tracking

---

## 7️⃣ Why Multi-Tenant Matters Here

* One system serves many companies
* Each company sees **only its own data**
* Same rules, same structure, different organizations
* Scales easily

---

## 8️⃣ What This Project Teaches You (Without Code)

You will learn:

* How real companies structure work
* How roles affect access
* How data ownership works
* How to design systems before coding

This is **how backend engineers think**.

---

## Final Summary (In One Paragraph)

> This application is a multi-organization work management system where companies manage teams, employees, and tasks. Work is assigned through managers, executed by employees, and tracked using priority, deadlines, and effort points. Access is strictly role-based, ensuring data security and accountability while providing meaningful insights into productivity and workload.

