# Assignment for Week 3: Discount Calculator

 ## Overview
 This Python application determines an item's final cost after a discount is applied.  A user interface for entering price and discount values is part of the solution, as is a function that only applies a discount if it is 20% or more.

 ## Function for Implementation ###: `calculate_discount(price, discount_percent)`
 **Parameters**:
   - `price`: The item's initial price (float)
   - `discount_percent`: Discount percentage (float)
 **Logic**:
   Discount is only applied if `discount_percent` is 20% or greater.
   If the condition is met, the discounted price is returned; otherwise, the original price is charged.
 **Formula**:  
   Price * (1 - discount_percent / 100) = discounted_price Flow of User Interaction
 1. Asks the user to input:
    The item's original price and the percentage of the discount
 2. Uses user input to call `calculate_discount()`
 3. Prints either
    The final discounted price, if the discount is greater than 20%
    The original price (if the discount is less than 20%)

 ## Operating Instructions: 1. Save