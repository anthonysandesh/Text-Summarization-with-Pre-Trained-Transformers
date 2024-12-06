import streamlit as st
from transformers import pipeline


MODEL_NAME = "HakunaMatata007/gigaword_model_t5_small" 

# Load the summarization pipeline
@st.cache_resource
def get_summarization_pipeline(model_name):
    summarizer = pipeline("summarization", model=model_name, tokenizer=model_name)
    return summarizer

# Streamlit app
def main():
    st.title("Summarize Your Text")
    st.subheader("Using Hugging Face Transformer Models")
    st.write("Enter a paragraph, and this app will summarize it for you.")

    # Load the summarization pipeline
    summarizer = get_summarization_pipeline(MODEL_NAME)

    # Text input from the user
    text_input = st.text_area("Paste your text here:", height=200)

    if st.button("Generate Summary"):
        if text_input.strip():
            with st.spinner("Generating summary..."):
                # Perform summarization
                summary = summarizer(
                    text_input,
                    # max_length=max_len,
                    # min_length=min_len,
                    length_penalty=2.0,
                    num_beams=4
                )[0]['summary_text']
            st.success("Summary Generated!")
            st.write("### Your Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

if __name__ == "__main__":
    main()