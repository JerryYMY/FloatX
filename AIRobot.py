import streamlit as st
import time

# --- 1. 页面配置 ---
st.set_page_config(page_title="FloatX AI Assistant", page_icon="💎")

# 侧边栏
with st.sidebar:
    st.header("当前市场热度")
    st.metric(label="OpenAI", value="\$145.20", delta="+5.2%")
    st.metric(label="SpaceX", value="\$98.50", delta="+1.1%")
    st.info("💡 提示：这是一个 Demo，目前使用关键词匹配逻辑。请尝试问 '投资流程'、'Blockchain' 或 'Difference'。")

# --- 2. 标题 ---
st.title("💬 FloatX 智能投资顾问 (V2)")
st.caption("已升级：支持中英文识别")

# --- 3. 初始化聊天记录 ---
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant",
         "content": "您好！我是 FloatX AI。我已经升级了词库，现在可以回答关于 'Blockchain'、'流程' 或 '区别' 的问题了。请试着问我！"}
    ]

# --- 4. 显示历史消息 ---
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# --- 5. 处理用户输入 ---
if prompt := st.chat_input():
    # 显示用户输入
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # 模拟思考
    with st.spinner("Thinking..."):
        time.sleep(0.5)

    # --- 升级后的逻辑 (支持中英文) ---
    response = ""
    p = prompt.lower()  # 把输入转成小写，方便匹配

    # 1. 匹配“区别 / 优势 / Difference”
    if any(w in p for w in ["区别", "优势", "不同", "difference", "competitor", "compare", "other platform"]):
        response = """
        **FloatX vs. Traditional Platforms (区别):**

        1.  **Lower Entry (低门槛)**: We allow investment starting from **1,000**, unlike the typical 100k+.
        2.  **Instant Settlement (T+0)**: Blockchain enables instant ownership transfer, no weeks of paperwork.
        3.  **Liquidity (流动性)**: You can sell fractional shares anytime on our marketplace.
        """

    # 2. 匹配“区块链 / Blockchain”
    elif any(w in p for w in ["区块链", "技术", "blockchain", "tech", "chain"]):
        response = """
        **Why Blockchain? (为什么使用区块链)**

        We use blockchain not for hype, but for **efficiency**:
        * **Transparency**: Your ownership is recorded on a distributed ledger, immutable and visible.
        * **Fractionalization**: It allows us to split a \$10M stock block into \$100 tokens.
        * **Automation**: Smart contracts handle compliance and settlement automatically.
        """

    # 3. 匹配“流程 / 怎么做 / How to / Process”
    elif any(w in p for w in ["流程", "怎么", "步骤", "process", "how", "steps", "do for me"]):
        response = """
        **Investment Process (投资流程):**

        1.  **Sign Up**: Create an account in 30 seconds.
        2.  **KYC**: Verify your identity (and accreditation status if required).
        3.  **Fund Wallet**: Deposit USDC or Fiat currency.
        4.  **Trade**: Place a bid on companies like SpaceX or OpenAI instantly.
        """

    # 4. 匹配“公司 / 买 / OpenAI / SpaceX”
    elif any(w in p for w in ["openai", "spacex", "stripe", "buy", "invest", "买", "价格"]):
        response = """
        **Market Opportunity:**

        * **SpaceX**: Trading around \$98.50. High demand.
        * **OpenAI**: Trading around \$145.20. Limited supply.

        👉 **[Click here to View Live Order Book](#)**
        """

    # 5. 兜底回复 (依然没匹配到)
    else:
        response = f"I'm listening! You mentioned '{prompt}', but my demo keywords are limited. Try asking about 'Blockchain', 'Fees', or 'Process'."

    # 发送回复
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
