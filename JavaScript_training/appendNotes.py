input_raw_notes = r"JavaScript_training\inputs\raw_notes.txt"
output_readme = r"JavaScript_training\readme.md"

section_title = ""

with open(input_raw_notes, 'r') as read_f:
    with open(output_readme, 'a') as write_f:
        for line in read_f.readlines():
            if line.startswith("file:"):
                continue
            if line.strip() == "":
                continue            
            trim_line = line.strip().strip(",").strip("-")
            trim_line = trim_line.strip().strip(",").strip("-")
            trim_line = trim_line.strip().strip(",").strip("-")
            
            if section_title=="":
                section_title = trim_line
                write_f.write(f"- {trim_line}\n")
            else:
                write_f.write(f"  - {trim_line}\n")
