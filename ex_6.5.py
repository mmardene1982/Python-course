#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.


text = "X-DSPAM-Confidence:    0.8475 fepaioja  "
num= '0.8'
num_pos = text.find(num, 0, len(text))
print(num_pos)
value = text[num_pos:]
print(value)
