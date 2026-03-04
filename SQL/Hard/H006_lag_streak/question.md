# Amazon SQL Interview Question

## Problem
Find products whose **price increased for at least 3 consecutive updates**.

## Table Structure

ProductPrices(
    product_id,
    update_date,
    price
)

## Requirements

1. Price must be **strictly increasing** across updates.
2. Updates must be **consecutive updates for that product** (dates may have gaps).
3. If a product has **3 consecutive price increases**, include that product.
4. Return:

product_id

## Example

| product_id | update_date | price |
|-------------|-------------|-------|
| A | Jan1 | 10 |
| A | Jan2 | 12 |
| A | Jan3 | 15 |
| A | Jan4 | 20 |

Price increases:

10 → 12  
12 → 15  
15 → 20  

This product should be returned.
