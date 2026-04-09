
import streamlit as st
from graphviz import Digraph
import re
from first_follow import compute_first, compute_follow

st.set_page_config(layout="wide")
st.title("💀 FINAL BOSS Compiler IDE")

menu = st.sidebar.selectbox("Modules", [
"Lexical Analyzer",
"FIRST & FOLLOW",
"Infix to Postfix",
"NFA Visualizer",
"DAG Visualizer",
"LR(0) Items"
])

if menu == "Lexical Analyzer":
    code = st.text_area("Enter Code")
    tokens = re.findall(r'[a-zA-Z_]+|\d+|==|!=|<=|>=|\S', code)
    st.write(tokens)

elif menu == "FIRST & FOLLOW":
    grammar = {"E":["TR"],"T":["id"]}
    st.write("Grammar:", grammar)
    st.write("FIRST:", compute_first(grammar))
    st.write("FOLLOW:", compute_follow(grammar,"E"))

elif menu == "Infix to Postfix":
    precedence={'+':1,'-':1,'*':2,'/':2}
    expr=st.text_input("Expression")
    if expr:
        stack=[]; output=""
        for ch in expr:
            if ch.isalnum(): output+=ch
            else:
                while stack and precedence.get(stack[-1],0)>=precedence[ch]:
                    output+=stack.pop()
                stack.append(ch)
        while stack: output+=stack.pop()
        st.success(output)

elif menu == "NFA Visualizer":
    dot = Digraph()
    dot.node("q0"); dot.node("q1")
    dot.edge("q0","q1", label="a")
    st.graphviz_chart(dot)

elif menu == "DAG Visualizer":
    dot = Digraph()
    dot.node("+"); dot.node("a"); dot.node("b")
    dot.edge("+","a"); dot.edge("+","b")
    st.graphviz_chart(dot)

elif menu == "LR(0) Items":
    st.write(["E -> .E+T", "E -> E.+T"])
