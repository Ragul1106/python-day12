def apply_discount(subtotal):
    if subtotal >= 500:
        print("🎉 Offer Applied: ₹50 off on orders above ₹500")
        return 50
    return 0
