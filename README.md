This is a simple python program which finds the kaprekar's routine for a 4 digit number 
*given the input is properly given for a digit kaprekar's routine*
to see it in action visit this google collab notebook:
  https://colab.research.google.com/drive/1-FGoLsGIfv9R2RrvwoEewDzWHClevQeU?usp=sharing
How the Routine Works (Step-by-Step)
  1. Pick a number: Choose any 4-digit number that has at least two distinct digits (leading zeros like 0042 are allowed).

  2. Sort descending: Rearrange the digits from largest to smallest to form the highest possible number.

  3. Sort ascending: Rearrange the digits from smallest to largest to form the lowest possible number.

  4. Subtract: Subtract the smaller number from the larger number.

  5. Repeat: Take the resulting answer and perform steps 2–4 again. If the result drops below 4 digits, pad it with leading zeros (e.g., 998 becomes 0998).
