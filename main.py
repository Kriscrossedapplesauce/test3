from pyscript import document

grade_7 = {"Alice Blue", "Anita Bath"}
grade_8 = {"Billy Sparks", "Eileen Dover", "Ella Vator"}
grade_9 = {"Francisco Portero", "Joe Kerr", "Josua Ortiz"}
grade_10 = {"Juanito Lakarin", "Justin Case", "Ligaya Anonuevo", "Paige Turner", "Restituto Fruto", "Sheldon Cooper", "Tam Nguyen"}

def add_member(event):
    f_name = document.getElementById("first-name").value.strip()
    l_name = document.getElementById("last-name").value.strip()
    

    new_member_full = f"{f_name} {l_name}"
    
    new_member_set = {new_member_full} if f_name and l_name else set()

    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_member_set

    sorted_members = sorted(master_set)
    formatted_members = "<br>".join([name for name in sorted_members])

    total_count = len(master_set)

    result_html = f"""
    <p class="fw-bold mb-2">All members:</p>
    <div class="mb-3">{formatted_members}</div>
    <p class="fw-bold mb-0">Total members: {total_count}</p>
    """

    document.getElementById("output-box").innerHTML = result_html