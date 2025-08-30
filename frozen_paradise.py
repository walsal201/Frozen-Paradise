import streamlit as st

# App title
st.title("🍹 Welcome to Frozen Paradize")

# Get user's name
name = st.text_input("What is your name?", "")

if name:
    st.write(f"Hello {name}, thank you so much for coming in today! 😊")

    # Menu options
    menu_items = [
        "Mango Juice", "Apple Juice", "Avocado Juice",
        "Pineapple Juice", "Strawberry Juice", "Cocktail Juice"
    ]

    # Show menu and take order
    order = st.selectbox(f"{name}, what would you like from our menu today?", menu_items)

    # Quantity input
    quantity = st.number_input("How many juices would you like?", min_value=1, step=1)

    # Price and total
    price = 10
    total = price * quantity

    # Display total and confirmation
    st.write(f"🧾 Thank you so much! Your total is: **${total}**")
    st.success(f"Sounds good {name}, we will have your {quantity} {order}(s) ready for you in a moment! 🍹")
