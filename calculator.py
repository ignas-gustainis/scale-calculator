import streamlit as st

st.title("Scale calculator")

participants = st.slider("Participant count", 0, 2000, 20)
proposer_perc = st.slider("Proposers (\% of participants)", 0, 100, 10)
time_to_train = st.slider("Slowest time to train (s)", 1, 600, 10)
time_to_evaluate = st.slider("Slowest time to evaluate (s)", 1, 600, 10)
slowest_bandwidth = st.slider("Slowest bandwidth (MB/s)", 0.1, 100.0, 1.0, step=0.1)
block_time = st.slider("Block time (s) (2s for Polygon)", 1, 15, 2)
parameter_size = st.slider("Parameter size (MB)", 1, 100, 15)

proposers = participants * proposer_perc // 100


def calc_round_duration():
    time_to_download_model = parameter_size / slowest_bandwidth
    proposer_duration = time_to_download_model + time_to_train + block_time
    voter_duration = time_to_download_model * proposers + time_to_evaluate + block_time
    return proposer_duration + voter_duration


st.metric("round_duration", calc_round_duration())
