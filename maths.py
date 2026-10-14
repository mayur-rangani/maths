
import streamlit as st
import itertools
import math
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Permutation and Combination",
    page_icon="🔢",
    layout="wide"
)

st.title("Permutation & Combination Studio")
st.caption("Foundation of Mathematics | Unit: Combinatorics")

st.markdown("""
<style>
.stApp {
    background-color: #f5f7ff;
}
div.stButton > button {
    border-radius: 10px;
    font-weight: bold;
    min-height: 42px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar menu
with st.sidebar:
    st.title("FM Mathematics")

    page = option_menu(
        menu_title="Main Menu",
        options=[
            "Home",
            "Permutation",
            "Combination",
            "Learn Mathematics"
        ],
        icons=[
            "house",
            "arrow-left-right",
            "grid-3x3-gap",
            "book"
        ],
        menu_icon="calculator",
        default_index=0,
        orientation="vertical"
    )

    st.divider()
    st.caption("Innovative Assignment")
    st.caption("Topic: Combinatorics")


# HOME PAGE
if page == "Home":

    st.header("Welcome to Combinatorics Studio!")

    st.write(
        "Calculate permutations and combinations using numbers, "
        "characters, words, or other items."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Permutation")
        st.latex(r"{}^nP_r = \frac{n!}{(n-r)!}")
        st.write("Permutation means arrangement of items.")
        st.info("Order matters: AB and BA are different.")

    with col2:
        st.subheader("Combination")
        st.latex(r"{}^nC_r = \frac{n!}{r!(n-r)!}")
        st.write("Combination means selection of items.")
        st.info("Order does not matter: AB and BA are the same selection.")

    st.divider()

    st.subheader("How to Use")
    st.markdown("""
    1. Select Permutation or Combination from the sidebar.
    2. Choose number input or character/item input.
    3. Enter n and r, or enter your items.
    4. Select whether repetition is allowed.
    5. Calculate the answer or generate possible results.
    """)


# PERMUTATION PAGE
elif page == "Permutation":

    st.header("Permutation Calculator")
    st.write("Permutation: order matters.")
    st.latex(r"{}^nP_r = \frac{n!}{(n-r)!}")
    st.latex(r"\text{With repetition: } n^r")

    mode = st.selectbox(
        "Choose Input Type",
        ["Numbers (n and r)", "Characters / Words / Items"],
        key="perm_mode"
    )

    repetition = st.selectbox(
        "Repetition",
        ["Without repetition", "With repetition"],
        key="perm_repeat"
    )

    if mode == "Numbers (n and r)":

        n = st.number_input(
            "Enter n (total number)",
            min_value=1,
            max_value=1000,
            value=5,
            step=1,
            key="perm_n"
        )

        if repetition == "Without repetition":
            max_r = int(n)
        else:
            max_r = 20

        r = st.number_input(
            "Enter r (positions/items)",
            min_value=1,
            max_value=max_r,
            value=min(3, max_r),
            step=1,
            key="perm_r"
        )

        if st.button("Calculate Permutation", type="primary"):

            n = int(n)
            r = int(r)

            if repetition == "Without repetition":

                answer = math.perm(n, r)

                st.latex(
                    rf"{{}}^{n}P_{r} = "
                    rf"\frac{{{n}!}}{{({n}-{r})!}} = {answer}"
                )

            else:

                answer = n ** r

                st.latex(rf"{{}}^{n}P_{r} = {n}^{r} = {answer}")

            st.success(f"Final Answer: {answer}")

    else:

        user_text = st.text_input(
            "Enter characters or comma-separated items",
            value="ABCD",
            key="perm_items",
            help="Examples: ABCD, 1234, A,2,B,5, red,blue,green"
        )

        if "," in user_text:
            items = [
                item.strip()
                for item in user_text.split(",")
                if item.strip()
            ]
        else:
            items = list(user_text.replace(" ", ""))

        # Remove duplicate items
        unique_items = []
        for item in items:
            if item not in unique_items:
                unique_items.append(item)

        items = unique_items
        n = len(items)

        if n == 0:

            st.warning("Please enter some items.")

        elif n > 8:

            st.warning("Enter no more than 8 unique items.")

        else:

            st.write("Your items:", ", ".join(items))

            if repetition == "Without repetition":
                max_r = n
            else:
                max_r = 8

            r = st.number_input(
                "Enter r (positions/items)",
                min_value=1,
                max_value=max_r,
                value=min(2, max_r),
                step=1,
                key="perm_item_r"
            )

            if st.button("Generate Permutations", type="primary"):

                r = int(r)

                if repetition == "Without repetition":

                    answer = math.perm(n, r)
                    generated = itertools.permutations(items, r)

                    st.latex(
                        rf"{{}}^{n}P_{r} = "
                        rf"\frac{{{n}!}}{{({n}-{r})!}} = {answer}"
                    )

                else:

                    answer = n ** r
                    generated = itertools.product(items, repeat=r)

                    st.latex(rf"{n}^{r} = {answer}")

                st.metric("Total Possible Results", f"{answer:,}")

                st.subheader("Generated Permutations")

                results = list(itertools.islice(generated, 100))

                for result in results:

                    if all(len(item) == 1 for item in result):
                        result_text = "".join(result)
                    else:
                        result_text = " | ".join(result)

                    st.write(result_text)

                if answer > 100:
                    st.caption("Showing the first 100 results.")


# COMBINATION PAGE
elif page == "Combination":

    st.header("Combination Calculator")
    st.write("Combination: order does not matter.")
    st.latex(r"{}^nC_r = \frac{n!}{r!(n-r)!}")
    st.latex(r"\text{With repetition: } \binom{n+r-1}{r} = \frac{(n+r-1)!}{r!(n-1)!}")

    mode = st.selectbox(
        "Choose Input Type",
        ["Numbers (n and r)", "Characters / Words / Items"],
        key="comb_mode"
    )

    repetition = st.selectbox(
        "Repetition",
        ["Without repetition", "With repetition"],
        key="comb_repeat"
    )

    if mode == "Numbers (n and r)":

        n = st.number_input(
            "Enter n (total number)",
            min_value=1,
            max_value=1000,
            value=5,
            step=1,
            key="comb_n"
        )

        if repetition == "Without repetition":
            max_r = int(n)
        else:
            max_r = 20

        r = st.number_input(
            "Enter r (items to select)",
            min_value=1,
            max_value=max_r,
            value=min(3, max_r),
            step=1,
            key="comb_r"
        )

        if st.button("Calculate Combination", type="primary"):

            n = int(n)
            r = int(r)

            if repetition == "Without repetition":

                answer = math.comb(n, r)

                st.latex(
                    rf"{{}}^{n}C_{r} = "
                    rf"\frac{{{n}!}}{{{r}!({n}-{r})!}} = {answer}"
                )

            else:

                answer = math.comb(n + r - 1, r)

                st.latex(
                    rf"\binom{{{n}+{r}-1}}{{{r}}} = \frac{{({n}+{r}-1)!}}{{{r}!({n}-1)!}} = {answer}"
                )

            st.success(f"Final Answer: {answer}")

    else:

        user_text = st.text_input(
            "Enter characters or comma-separated items",
            value="ABCD",
            key="comb_items",
            help="Examples: ABCD, 1234, A,2,B,5, red,blue,green"
        )

        if "," in user_text:
            items = [
                item.strip()
                for item in user_text.split(",")
                if item.strip()
            ]
        else:
            items = list(user_text.replace(" ", ""))

        # Remove duplicate items
        unique_items = []
        for item in items:
            if item not in unique_items:
                unique_items.append(item)

        items = unique_items
        n = len(items)

        if n == 0:

            st.warning("Please enter some items.")

        elif n > 8:

            st.warning("Enter no more than 8 unique items.")

        else:

            st.write("Your items:", ", ".join(items))

            if repetition == "Without repetition":
                max_r = n
            else:
                max_r = 8

            r = st.number_input(
                "Enter r (items to select)",
                min_value=1,
                max_value=max_r,
                value=min(2, max_r),
                step=1,
                key="comb_item_r"
            )

            if st.button("Generate Combinations", type="primary"):

                r = int(r)

                if repetition == "Without repetition":

                    answer = math.comb(n, r)
                    generated = itertools.combinations(items, r)

                    st.latex(
                        rf"{{}}^{n}C_{r} = "
                        rf"\frac{{{n}!}}{{{r}!({n}-{r})!}} = {answer}"
                    )

                else:

                    answer = math.comb(n + r - 1, r)

                    generated = itertools.combinations_with_replacement(
                        items, r
                    )

                    st.latex(
                        rf"\binom{{{n}+{r}-1}}{{{r}}} = \frac{{({n}+{r}-1)!}}{{{r}!({n}-1)!}} = {answer}"
                    )

                st.metric("Total Possible Results", f"{answer:,}")

                st.subheader("Generated Combinations")

                results = list(itertools.islice(generated, 100))

                for result in results:

                    if all(len(item) == 1 for item in result):
                        result_text = "".join(result)
                    else:
                        result_text = " | ".join(result)

                    st.write(result_text)

                if answer > 100:
                    st.caption("Showing the first 100 results.")


# LEARN MATHEMATICS PAGE
elif page == "Learn Mathematics":

    st.header("Learn the Mathematics")

    st.subheader("1. Factorial")
    st.latex(r"4! = 4 \times 3 \times 2 \times 1 = 24")

    st.subheader("2. Permutation Without Repetition")
    st.latex(r"{}^nP_r = \frac{n!}{(n-r)!}")

    st.subheader("3. Permutation With Repetition")
    st.latex(r"n^r")

    st.subheader("4. Combination Without Repetition")
    st.latex(r"{}^nC_r = \frac{n!}{r!(n-r)!}")

    st.subheader("5. Combination With Repetition")
    st.latex(r"\binom{n+r-1}{r}")

    st.divider()

    st.subheader("Applications")
    st.markdown("""
    - Permutation: arranging items in different orders.
    - Combination: selecting groups of items.
    - Computing: calculating possible codes and selections.
    - Mathematics: counting possible arrangements and selections.
    """)

    st.subheader("Conclusion")
    st.write(
        "This application demonstrates permutations and combinations "
        "using Python and Streamlit. It calculates answers and displays "
        "possible results, with or without repetition."
    )


st.divider()
st.caption("Foundation of Mathematics | Innovative Assignment | Combinatorics")
