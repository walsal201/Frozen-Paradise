import streamlit as st

# App title
st.title("🍹 Welcome to Frozen Paradize")

# Customer name
name = st.text_input("What is your name?", "")

if name:
    st.write(f"Hello {name}, thank you so much for coming in today! 😊")

    # Menu and pricing
    menu = {
        "Mango Juice": 10,
        "Apple Juice": 10,
        "Avocado Juice": 12,
        "Pineapple Juice": 11,
        "Strawberry Juice": 10,
        "Cocktail Juice": 15
    }

    st.write("Here's what we're serving today:")

    # Create input fields for each item
    order_summary = {}
    for item, price in menu.items():
        qty = st.number_input(f"{item} (${price}) - Quantity:", min_value=0, step=1, key=item)
        if qty > 0:
            order_summary[item] = {"quantity": qty, "price": price}

    # Calculate total
    if order_summary:
        st.subheader("🧾 Your Order Summary")
        total = 0
        for item, details in order_summary.items():
            item_total = details["quantity"] * details["price"]
            total += item_total
            st.write(f"{details['quantity']} x {item} = ${item_total}")

        st.markdown(f"### ✅ Total: **${total}**")
        st.success(f"Thanks {name}! We'll have your order ready shortly 🍹")

    else:
        st.info("Select at least one item to place your order.")
