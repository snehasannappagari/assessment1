book1_price = 499.00
book2_price = 855.00
book3_price = 645.00
 

gst_rate = 0.12
delivery_charge = 250.00

subtotal = book1_price + book2_price + book3_price
taxes = subtotal * gst_rate 
total_delivery_charges = delivery_charge
total = subtotal + taxes + total_delivery_charges
#print the invoice
print("Invoice:")
print("======")
print(f"Book - Introduction to Python Programming : Rs {book1_price:.2f}")
print(f"Book - Python Libraries Cookbook          : Rs {book2_price:.2f}")
print(f"Book - Data Science in Python             : Rs {book3_price:.2f}")
print(f"Subototal                                 : Rs {taxes:.2f}")
print(f"GST ({gst_rate*100:.0f}%)                 : Rs {taxes:.2f}")
print(f"delivery_charge                           : Rs {total_delivery_charges:.2f}")
print(f"Total                                     : Rs {total:.2f}")                   


