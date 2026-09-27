import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# ----------------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state
# ----------------------------------------------------
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# ----------------------------------------------------
# 2. ฟังก์ชันเริ่มเกมใหม่
# ----------------------------------------------------
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# 3. ฟังก์ชันแสดงผลลัพธ์
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog():
    st.balloons()

    score = 0

    # ดึงคำตอบจาก session_state
    u_ans1 = st.session_state.ans1_val.strip().lower()
    u_ans2 = st.session_state.ans2_val.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 1: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{u_ans1}')"
        )

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(
            f"❌ ข้อ 2: ยังไม่ถูกต้อง "
            f"(คุณตอบ '{u_ans2}')"
        )

    st.info(f"🏆 ได้คะแนนรวม: {score} / 2 คะแนน")

    if score == 2:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")

    if st.button("🔄 เล่นอีกครั้ง"):
        reset_game()
        st.rerun()


# ----------------------------------------------------
# 4. ปุ่มเริ่มเกม
# ----------------------------------------------------
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# ----------------------------------------------------
# 5. แสดงเวลานับถอยหลัง
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    elapsed = time.time() - st.session_state.start
    time_left = max(0, int(30 - elapsed))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ----------------------------------------------------
# 6. ช่องกรอกคำตอบ
# ----------------------------------------------------
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    key="ans1_val"
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    key="ans2_val"
)


# ----------------------------------------------------
# 7. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    # อัปเดตหน้าจอทุก 1 วินาที
    time.sleep(1)
    st.rerun()


# ----------------------------------------------------
# 8. แสดง Dialog เมื่อจบเกม
# ----------------------------------------------------
if st.session_state.is_ended:
    show_result_dialog()


st.divider()

st.write("นางสาวภิภัทรภรณ์สมพันธ์ เลขที่ 26 ม.4/15")
