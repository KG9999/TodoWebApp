import streamlit as st
import Functions

st.write("<i><b>My todo App</i></b>",unsafe_allow_html=True)

todos=Functions.get_data()
for index,todo in enumerate(todos):
    checked = st.checkbox(todo, key=todo)
    if checked:
        todos.remove(todo)
        Functions.write_data(todos)
        del st.session_state[todo]
        st.rerun()

def add_todo():
    new_item=st.session_state["new_todo"]
    print(new_item)
    todos.append(new_item+"\n")
    Functions.write_data(todos)
    st.rerun()



st.text_input(label="",placeholder="Enter a todo",on_change=add_todo,key="new_todo")


