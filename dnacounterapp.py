import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
from Bio.SeqUtils import GC

image=Image.open('/Users/danielaquijano/Desktop/dnalogo.png')

st.image(image, use_column_width=True)

st.header("""
DNA Nucleotide Counter App

This application is able to count DNA nucleotides from an input sequence""")


st.subheader('Enter your query sequence')

sequence_input=">DNA Query\nGAAATTCCTTC"

sequence=(st.text_area('Sequence input:',sequence_input, height=50))
sequence=sequence.splitlines()
sequence=sequence[1:]
sequence=''.join(sequence)

st.write("""
***
""")

st.subheader('The sequence you entered was:')
sequence

st.subheader('The nucleotide count for your sequence is:')

def DNA_nucleotide_count(seq):
    d=dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('C',seq.count('C')),
        ('G',seq.count('G'))
    ])
    return d

X=DNA_nucleotide_count(sequence)

X_label=list(X)
X_values=list(X.values())

X
#Make df
st.subheader('The following is the nucleotide count summary:')
df=pd.DataFrame.from_dict(X,orient='index')
df=df.rename({0:'Count'}, axis='columns')
df.reset_index(inplace=True)
df=df.rename(columns={'index':'Nucleotide'})
st.write(df)

#Make Bar chart 
p=alt.Chart(df).mark_bar().encode(
    x='Nucleotide',
    y='Count',
    color=alt.condition(
           alt.datum.nucleotide=='x',
           alt.value('blue'),
           alt.value('magenta'),
           )
    )
p=p.properties(width=alt.Step(140))
st.write('The bar graph below visualizes the nucleotide counts:')
st.write(p)


#Make GC content pie chart
#GC=((sequence.count('C')+sequence.count('G'))/(len(sequence))
st.write('The GC content of the sequence you entered was:')
st.write(GC(sequence))
source = pd.DataFrame({"Nucleotide": ['A, T','C, G'], "Count": [sequence.count('A')+sequence.count('T'),sequence.count('C')+sequence.count('G')]})
q=alt.Chart(source).mark_arc().encode(
    theta=alt.Theta(field="Count", type="quantitative"),
    color=alt.Color(field="Nucleotide", type="nominal"),
)
st.write(q)



