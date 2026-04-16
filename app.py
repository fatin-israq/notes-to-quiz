import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator
from PIL import Image

# Title
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()

with st.sidebar:
    st.header("controls")

    # Image upload
    images = st.file_uploader(
        "Upload the pictures of your note",
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True
    )

    pil_images = [Image.open(img) for img in images]

    if images:
        if len(images) > 5:
            st.error("Upload at max 3 images")
        else:
            col = st.columns(len(images))

            st.subheader("Uploaded images")
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)

    # Difficulty Selection
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy", "Medium", "Hard"),
        index=None
    )

    if selected_option:
        st.markdown(f"You selected {selected_option} as difficulty for the quiz")

    # Button
    pressed = st.button("Click the button to initiate AI", type="primary")


if pressed:
    if not images:
        st.warning("No image uploaded, you must upload 1 image")
    if not selected_option:
        st.warning("You must select a difficulty for the quiz")

    if images and selected_option:
        # Note
        with st.container(border=True):
            st.subheader("Your notes (Summarized)")

            with st.spinner("AI is summarizing the notes for you"):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)

        # Audio Transcript
        with st.container(border=True):
            st.subheader("Audio Transcription")

            with st.spinner("AI is transcripting the audio"):
                
                # cleaning some markdown
                generated_notes = generated_notes.replace("#", "")
                generated_notes = generated_notes.replace("*", "")
                generated_notes = generated_notes.replace("-", "")
                generated_notes = generated_notes.replace("`", "")

                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)

        # Note
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option})")

            with st.spinner("Quiz is being prepared"):
                quiz = quiz_generator(pil_images, selected_option)
                st.markdown(quiz)