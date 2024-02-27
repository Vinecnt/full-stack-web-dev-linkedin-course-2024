input_html = r"JavaScript_training\inputs\draft_index.html"
output_html = r"JavaScript_training\outputs\index.html"
raw_transcript = r"JavaScript_training\inputs\raw_transcript.txt"

with open(input_html, 'r') as read_f:
    draft_html = read_f.read()
    with open(raw_transcript, 'r') as raw_transcript_f:
        transcript = raw_transcript_f.read()
        transcript = transcript.replace("\n", "<br>")
        transcript = transcript.replace(". ", ". <br>- ")
        with open(output_html, 'w') as write_f:
            replaced_html = draft_html.replace("replacement_text", transcript)
            write_f.write(replaced_html)