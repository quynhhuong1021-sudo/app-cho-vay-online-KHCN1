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

st.title("🏦 Hệ Thống Đánh Giá Khả Năng Vay Vốn")

st.subheader("Thông tin khách hàng")

# Thông tin khoản vay
STV = st.number_input(
    "Số tiền muốn vay (triệu đồng)",
    min_value=1.0,
    value=500.0
)

TGV = st.number_input(
    "Thời gian vay (năm)",
    min_value=1,
    value=10
)

LSV = st.number_input(
    "Lãi suất năm (%)",
    min_value=0.0,
    value=12.0
)

TN = st.number_input(
    "Thu nhập hàng tháng (triệu đồng)",
    min_value=0.0,
    value=30.0
)

SNTGD = st.number_input(
    "Số người trong gia đình",
    min_value=1,
    value=4
)

PTMC = st.number_input(
    "Khoản trả nợ cũ hàng tháng (triệu đồng)",
    min_value=0.0,
    value=0.0
)

GTTSDB = st.number_input(
    "Giá trị tài sản đảm bảo (triệu đồng)",
    min_value=1.0,
    value=1000.0
)

STKH = st.number_input(
    "Tuổi khách hàng",
    min_value=18,
    max_value=100,
    value=30
)

if st.button("Đánh Giá Khoản Vay"):

    # Chi phí sinh hoạt bình quân
    CPSH = 5

    # Lãi suất tháng
    lai_suat_thang = (LSV / 100) / 12

    # Khoản trả hàng tháng (đơn giản)
    goc_thang = STV / (TGV * 12)
    lai_thang = STV * lai_suat_thang

    PTMM = goc_thang + lai_thang

    # Thu nhập khả dụng
    thu_nhap_con_lai = TN - (SNTGD * CPSH)

    if thu_nhap_con_lai <= 0:
        st.error("Thu nhập không đủ để trang trải chi phí sinh hoạt.")
    else:

        DTI = (PTMC + PTMM) / thu_nhap_con_lai
        LTV = STV / GTTSDB

        st.subheader("Kết quả phân tích")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("DTI", f"{DTI*100:.2f}%")

        with col2:
            st.metric("LTV", f"{LTV*100:.2f}%")

        with col3:
            st.metric(
                "Trả hàng tháng",
                f"{PTMM:.2f} triệu"
            )

        st.write("---")

        # Đánh giá DTI
        if DTI <= 0.4:
            st.success("DTI tốt")
        elif DTI <= 0.6:
            st.warning("DTI ở mức chấp nhận được")
        else:
            st.error("DTI quá cao")

        # Đánh giá LTV
        if LTV <= 0.7:
            st.success("LTV đạt yêu cầu")
        else:
            st.error("LTV vượt ngưỡng cho phép")

        # Đánh giá tuổi
        if 18 <= STKH <= 65:
            st.success("Tuổi khách hàng phù hợp")
        else:
            st.error("Tuổi khách hàng không phù hợp")

        st.write("---")

        # Quyết định cuối cùng
        if (
            DTI <= 0.6
            and LTV <= 0.7
            and 18 <= STKH <= 65
        ):
            st.success("🎉 KẾT QUẢ: ĐƯỢC ĐỀ XUẤT CHO VAY")
        else:
            st.error("❌ KẾT QUẢ: KHÔNG ĐỦ ĐIỀU KIỆN CHO VAY")
# Giải thích
        st.subheader("Giải thích")

        st.write(f"• Số tiền phải trả hàng tháng: **{PTMM:.2f} triệu đồng**")
        st.write(f"• Thu nhập khả dụng: **{thu_nhap_con_lai:.2f} triệu đồng**")
        st.write(f"• Tỷ lệ DTI: **{DTI*100:.2f}%**")
        st.write(f"• Tỷ lệ LTV: **{LTV*100:.2f}%**")
