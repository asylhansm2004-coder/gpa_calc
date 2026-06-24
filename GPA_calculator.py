import streamlit as st

st.set_page_config(
    page_title="Калькулятор GPA",
    layout="centered",
)

st.title("Калькулятор  GPA")
st.markdown(
    "Введите данные за основное обучение и интернатуру — "
    "итоговый GPA считается автоматически."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Основное обучение (5 лет)")
    credits_5 = st.number_input(
        "Кредиты за 5 лет",
        min_value=0.0,
        step=0.5,
        format="%.1f",
        key="credits_5",
    )
    gpa_5 = st.number_input(
        "GPA за 5 лет",
        min_value=0.0,
        step=0.01,
        format="%.2f",
        key="gpa_5",
    )

with col2:
    st.subheader("Интернатура")
    credits_int = st.number_input(
        "Кредиты за интернатуру",
        min_value=0.0,
        step=0.5,
        format="%.1f",
        key="credits_int",
    )
    gpa_int = st.number_input(
        "GPA за интернатуру",
        min_value=0.0,
        step=0.01,
        format="%.2f",
        key="gpa_int",
    )

st.divider()

total_credits = credits_5 + credits_int

if total_credits == 0:
    st.info("Введите кредиты и GPA, чтобы увидеть результат.")
else:
    weighted_gpa = (credits_5 * gpa_5 + credits_int * gpa_int) / total_credits
    st.metric(
        label="Средневзвешенный GPA",
        value=f"{weighted_gpa:.4f}",
    )
    with st.expander("Показать расчёт"):
        st.latex(
            r"\text{GPA} = \frac{C_1 \times G_1 + C_2 \times G_2}{C_1 + C_2}"
        )
        st.code(
            f"({credits_5} × {gpa_5} + {credits_int} × {gpa_int}) "
            f"/ ({credits_5} + {credits_int}) = {weighted_gpa:.4f}"
        )
