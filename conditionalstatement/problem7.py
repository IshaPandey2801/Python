"""
Write a conditional expression for:
- if a<10 b = 20, else b = 30
- print morning if time<12, otherwise print afternoon
- if marks>=70, set remarks to true, otherwise false
"""
a= int(input("Enter value of a : "))
if a<10:
    b = 20
else:
    b=30

print("Value of b :", b)


time =input("Enter time (e.g 7:00 AM): ").lower()

hours = int(time.split(":")[0])
if "am" in time and hours < 12:
    print('Morning')
elif "pm" in time:
    print('Afternoon')
else:
    print("Check input")


"""

## 🔍 The code:

```python
hour = int(time.split(":")[0])
```

---

## 🧠 Step-by-step meaning

Assume:

```python
time = "7:00 am"
```

---

### 1️⃣ `time.split(":")`

```python
time.split(":")
```

👉 Splits the string wherever `:` appears

Result:

```python
['7', '00 am']
```

---

### 2️⃣ `[0]` (indexing)

```python
time.split(":")[0]
```

👉 Takes the **first part** of the list

Result:

```python
'7'
```

---

### 3️⃣ `int(...)`

```python
int('7')
```

👉 Converts string `'7'` into number `7`

---

## ✅ Final result:

```python
hour = 7
```

---

## 📦 In one line:

👉 **“Take the hour part from the time string and convert it into an integer.”**

---

## 🔁 Another example

If:

```python
time = "12:30 pm"
```

Then:

```python
time.split(":") → ['12', '30 pm']
time.split(":")[0] → '12'
int('12') → 12
```

---

## ⚠️ Important note

This works only if the format is:

```
hour:minutes am/pm
```

Example:

* ✅ "9:15 am"
* ❌ "9 am" (no colon → will break)

---

## ✅ Simple summary

* `split(":")` → breaks string into parts
* `[0]` → picks hour
* `int()` → converts to number

---

If you want, I can show a safer version that handles **all formats without crashing** 👍
"""

marks = float(input("Enter marks of student : "))

if marks>=70:
    print("Remarks : True")
else:
    print("Remarks : False")