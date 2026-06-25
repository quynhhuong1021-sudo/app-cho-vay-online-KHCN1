import streamlit as st

st.title("App cho vay online khách hàng cá nhân_ Nguyễn Hoàng Quỳnh Huơng- đề tài 3")

# Nhập dữ liệu
STV = st.number_input(
    "Nhập số tiền muốn vay (triệu đồng)",
    min_value=0.0,
    value=500.0
)

TGV = st.number_input(
    "Nhập thời gian vay (số năm)",
    min_value=1.0,
    value=5.0
)

LSV = st.number_input(
    "Nhập lãi suất cho vay (ví dụ: 0.12 = 12%)",
    min_value=0.0,
    value=0.12,
    format="%.4f"
)

TN = st.number_input(
    "Nhập thu nhập hàng tháng (triệu đồng/tháng)",
    min_value=0.0,
    value=20.0
)

SNTGD = st.number_input(
    "Nhập số người trong gia đình",
    min_value=1,
    value=4
)

PTMC = st.number_input(
    "Nhập số tiền phải trả cho khoản vay cũ (triệu đồng/tháng)",
    min_value=0.0,
    value=0.0
)

GTTSDB = st.number_input(
    "Giá trị tài sản đảm bảo (triệu đồng)",
    min_value=1.0,
    value=1000.0
)

STKH = st.number_input(
    "Nhập số tuổi khách hàng",
    min_value=0,
    value=25
)

# Chi phí sinh hoạt mặc định
CPSH = 5

if st.button("Đánh giá khoản vay"):

    # Tiền phải trả mỗi tháng
    PTMM = (STV / (TGV * 12)) + (STV * (LSV / 12))

    # Chỉ số DTI
    thu_nhap_con_lai = TN - (SNTGD * CPSH)

    if thu_nhap_con_lai <= 0:
        st.error("Thu nhập còn lại không hợp lệ!")
    else:
        DTI = (PTMC + PTMM) / thu_nhap_con_lai

        # Chỉ số LTV
        LTV = STV / GTTSDB

        st.write(f"### Chỉ số DTI: {DTI*100:.2f}%")
        st.write(f"### Chỉ số LTV: {LTV*100:.2f}%")

        # Điều kiện xét duyệt
        if DTI <= 0.7 and LTV <= 0.7 and STKH >= 18:
            st.success("✅ ĐƯỢC CHO VAY")
        else:
            st.error("❌ KHÔNG ĐƯỢC CHO VAY")
import streamlit as st

st.set_page_config(
    page_title="Đánh giá khả năng vay vốn",
    page_icon="🏦"
)

