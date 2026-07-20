# 1.3 — Problem Framing Statement

> **Objective:** Frame your ML problem in ONE precise sentence using the universal template.
> Reference: Slide 1.3 of `phase1_system_design.html`

---

## The Universal Template

```
Given  [input features available at prediction time]
Predict [target variable with type and unit]
For    [end user or downstream system]
At     [decision time / latency requirement]
To     [business outcome this prediction drives]
```

Every blank forces a specific design decision. Skip any blank, and you're building blind.

---

## House Prices: Filled-In Template

```
Given   82 property features (sqft, bedrooms, bathrooms, overall quality,
        year built, neighborhood, garage size, basement finish, lot size,
        and 72 other attributes available at listing time)

Predict SalePrice in USD (continuous value, regression problem)

For     Real estate agents evaluating property listings and home buyers
        making purchase decisions

At      < 500ms latency (during web page load — the estimate appears
        as the user browses the listing)

To      Help buyers make informed offers within 5% of fair market value,
        reducing negotiation time by 30% and increasing agent close rate
```

---

## Why Each Blank Matters

| Blank | Wrong Answer | Consequence |
|-------|-------------|-------------|
| **Given** | Using features not available at prediction time | Train/serve skew — model expects data it can't get |
| **Predict** | Wrong type (classification instead of regression) | Wrong algorithm, wrong loss function |
| **For** | "Everyone" or undefined user | Wrong interface, wrong metrics, wrong product |
| **At** | No latency requirement | Might build a slow-but-accurate model that's unusable |
| **To** | No business outcome | Can't measure success — model might work but deliver no value |

---

## Your Turn

```
Given   _________________________________________________________________
Predict _________________________________________________________________
For     _________________________________________________________________
At      _________________________________________________________________
To      _________________________________________________________________
```

**Check:** Did you fill ALL five blanks with specifics? "Reduce costs" is not specific enough — by how much? For whom?

---

## Anti-Patterns to Avoid

- ❌ "Given data, predict outcome" — too vague
- ❌ "To improve the business" — not measurable
- ❌ "For everyone" — who specifically uses this prediction?
- ❌ "At some point" — what's the latency budget?
