
import streamlit as st
import pandas as pd
st.title("Merge Excel trực tiếp từ Streamlit Cloud")

# Upload nhiều file Excel
uploaded_files = st.file_uploader("Upload file Excel (có thể nhiều file)", type=["xlsx"], accept_multiple_files=True)

# Cột chuẩn
columns_standard = [
    "線別","生產日期","品名代碼","投入鋼捲號碼","產出鋼捲號碼","訂單號碼",
    "標準板編號","塗料編號","製造批號","顏色","正面漆膜厚","Minimum thickness 正面",
    "NORTH_TOP_FILM_THICK","SOUTH_TOP_FILM_THICK","Avergage Thickness (µm)正面",
    "光澤60度反射(下限)","光澤60度反射(上限)","光澤","NORTH_TOP_BLANCH","SOUTH_TOP_BLANCH",
    "NORTH_BACK_BLANCH","SOUTH_BACK_BLANCH","Average value 產出光澤正面","Status1",
    "NORTH_TOP_DELTA_E","NORTH_TOP_DELTA_L","NORTH_TOP_DELTA_A","NORTH_TOP_DELTA_B",
    "SOUTH_TOP_DELTA_E","SOUTH_TOP_DELTA_L","SOUTH_TOP_DELTA_A","SOUTH_TOP_DELTA_B",
    "Average value ∆E 正面","Average value ∆L 正面","Average value ∆a 正面","Average value ∆b 正面",
    "入料檢測 ∆L 正面","入料檢測 ∆a 正面","入料檢測 ∆b 正面"
]

def read_excel(file):
    df = pd.read_excel(file)
    for col in columns_standard:
        if col not in df.columns:
            df[col] = ""
    df = df[columns_standard]
    df['Nguồn File'] = file.name
    return df

if st.button("Tạo file tổng hợp"):
    if not uploaded_files:
        st.warning("Vui lòng upload ít nhất 1 file Excel")
    else:
        df_list = [read_excel(f) for f in uploaded_files]
        df_total = pd.concat(df_list, ignore_index=True)
        output_file = "tong_hop.xlsx"
        df_total.to_excel(output_file, index=False)
        st.success(f"Đã tạo file tổng hợp: {output_file}")
        st.download_button("Download file tổng hợp", data=open(output_file, "rb"), file_name=output_file)
